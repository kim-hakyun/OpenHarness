from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QGraphicsView


class GraphicsView(QGraphicsView):
    mouse_position_changed = Signal(float, float)
    zoom_changed = Signal(int)

    MINOR_GRID_SIZE = 25
    MAJOR_GRID_SIZE = 125

    def __init__(self, scene) -> None:
        super().__init__(scene)

        self._zoom_percent = 100
        self._is_panning = False
        self._last_pan_pos = None

        self.setMouseTracking(True)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setBackgroundBrush(QColor(24, 24, 24))

    def drawBackground(self, painter: QPainter, rect) -> None:
        painter.fillRect(rect, QColor(24, 24, 24))

        self._draw_grid(
            painter=painter,
            rect=rect,
            grid_size=self.MINOR_GRID_SIZE,
            color=QColor(45, 45, 45),
            width=1,
        )

        self._draw_grid(
            painter=painter,
            rect=rect,
            grid_size=self.MAJOR_GRID_SIZE,
            color=QColor(75, 75, 75),
            width=1,
        )

        self._draw_origin_axis(painter, rect)

    def _draw_grid(self, painter: QPainter, rect, grid_size: int, color: QColor, width: int) -> None:
        pen = QPen(color)
        pen.setWidth(width)
        painter.setPen(pen)

        left = int(rect.left()) - int(rect.left()) % grid_size
        top = int(rect.top()) - int(rect.top()) % grid_size

        x = left
        while x < rect.right():
            painter.drawLine(x, rect.top(), x, rect.bottom())
            x += grid_size

        y = top
        while y < rect.bottom():
            painter.drawLine(rect.left(), y, rect.right(), y)
            y += grid_size

    def _draw_origin_axis(self, painter: QPainter, rect) -> None:
        pen = QPen(QColor(120, 120, 120))
        pen.setWidth(2)
        painter.setPen(pen)

        if rect.left() <= 0 <= rect.right():
            painter.drawLine(0, rect.top(), 0, rect.bottom())

        if rect.top() <= 0 <= rect.bottom():
            painter.drawLine(rect.left(), 0, rect.right(), 0)

    def wheelEvent(self, event) -> None:
        zoom_in_factor = 1.15
        zoom_out_factor = 1 / zoom_in_factor

        if event.angleDelta().y() > 0:
            self.scale(zoom_in_factor, zoom_in_factor)
            self._zoom_percent = int(self._zoom_percent * zoom_in_factor)
        else:
            self.scale(zoom_out_factor, zoom_out_factor)
            self._zoom_percent = int(self._zoom_percent * zoom_out_factor)

        self.zoom_changed.emit(self._zoom_percent)

    def mouseMoveEvent(self, event) -> None:
        scene_pos = self.mapToScene(event.pos())
        self.mouse_position_changed.emit(scene_pos.x(), scene_pos.y())

        if self._is_panning and self._last_pan_pos is not None:
            delta = event.pos() - self._last_pan_pos
            self._last_pan_pos = event.pos()

            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - delta.x()
            )
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - delta.y()
            )

        super().mouseMoveEvent(event)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.MiddleButton:
            self._is_panning = True
            self._last_pan_pos = event.pos()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            event.accept()
            return

        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.MiddleButton:
            self._is_panning = False
            self._last_pan_pos = None
            self.setCursor(Qt.CursorShape.ArrowCursor)
            event.accept()
            return

        super().mouseReleaseEvent(event)