from PySide6.QtCore import QRectF
from PySide6.QtGui import QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import QGraphicsItem

from openharness.model.connector import ConnectorHousing


class ConnectorItem(QGraphicsItem):
    PIN_SPACING = 28
    WIDTH = 220
    HEADER_HEIGHT = 58
    LEFT_MARGIN = 22

    def __init__(self, connector: ConnectorHousing) -> None:
        super().__init__()

        self.connector = connector
        self.setPos(connector.x, connector.y)

        self.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable
            | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable
            | QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges
        )

    def boundingRect(self) -> QRectF:
        height = self.HEADER_HEIGHT + max(1, len(self.connector.contacts)) * self.PIN_SPACING + 20
        return QRectF(0, 0, self.WIDTH, height)

    def paint(self, painter: QPainter, option, widget=None) -> None:
        rect = self.boundingRect()

        border_color = QColor(80, 150, 255) if self.isSelected() else QColor(180, 180, 180)
        painter.setPen(QPen(border_color, 2))
        painter.setBrush(QColor(38, 38, 38))
        painter.drawRoundedRect(rect, 6, 6)

        painter.setPen(QPen(QColor(230, 230, 230)))
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(10)
        painter.setFont(title_font)

        lines = self.connector.display_name.split("\n")
        painter.drawText(12, 22, lines[0])

        if len(lines) > 1:
            sub_font = QFont()
            sub_font.setPointSize(8)
            painter.setFont(sub_font)
            painter.setPen(QPen(QColor(190, 190, 190)))
            painter.drawText(12, 42, lines[1])

        painter.setPen(QPen(QColor(90, 90, 90), 1))
        painter.drawLine(0, self.HEADER_HEIGHT, self.WIDTH, self.HEADER_HEIGHT)

        pin_font = QFont()
        pin_font.setPointSize(8)
        painter.setFont(pin_font)

        y = self.HEADER_HEIGHT + 22

        for contact in self.connector.contacts:
            painter.setPen(QPen(QColor(210, 210, 210), 1))
            painter.setBrush(QColor(24, 24, 24))
            painter.drawEllipse(self.LEFT_MARGIN, y - 7, 14, 14)

            painter.setPen(QPen(QColor(230, 230, 230)))
            painter.drawText(48, y + 5, str(contact.number))

            signal = contact.signal or "N.C"
            painter.setPen(QPen(QColor(180, 210, 255)))
            painter.drawText(82, y + 5, signal)

            if contact.part_number:
                painter.setPen(QPen(QColor(160, 160, 160)))
                painter.drawText(145, y + 5, contact.part_number)

            y += self.PIN_SPACING