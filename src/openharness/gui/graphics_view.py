from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QGraphicsView


class GraphicsView(QGraphicsView):
    GRID_SIZE = 25

    def __init__(self, scene) -> None:
        super().__init__(scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setBackgroundBrush(QColor(30, 30, 30))

    def drawBackground(self, painter: QPainter, rect) -> None:
        painter.fillRect(rect, QColor(30, 30, 30))

        pen = QPen(QColor(55, 55, 55))
        pen.setWidth(1)
        painter.setPen(pen)

        left = int(rect.left()) - int(rect.left()) % self.GRID_SIZE
        top = int(rect.top()) - int(rect.top()) % self.GRID_SIZE

        x = left
        while x < rect.right():
            painter.drawLine(x, rect.top(), x, rect.bottom())
            x += self.GRID_SIZE

        y = top
        while y < rect.bottom():
            painter.drawLine(rect.left(), y, rect.right(), y)
            y += self.GRID_SIZE

    def wheelEvent(self, event) -> None:
        zoom_in_factor = 1.15
        zoom_out_factor = 1 / zoom_in_factor

        if event.angleDelta().y() > 0:
            self.scale(zoom_in_factor, zoom_in_factor)
        else:
            self.scale(zoom_out_factor, zoom_out_factor)