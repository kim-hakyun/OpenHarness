from PySide6.QtWidgets import QGraphicsScene


class HarnessScene(QGraphicsScene):
    def __init__(self) -> None:
        super().__init__()
        self.setSceneRect(-5000, -5000, 10000, 10000)