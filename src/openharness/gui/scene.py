from PySide6.QtWidgets import QGraphicsScene


class HarnessScene(QGraphicsScene):
    def __init__(self) -> None:
        super().__init__()
        self.setSceneRect(-10000, -10000, 20000, 20000)