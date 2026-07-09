from PySide6.QtWidgets import (
    QMainWindow,
    QGraphicsScene,
    QStatusBar,
)

from openharness.gui.graphics_view import GraphicsView


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("OpenHarness V0.1.0")

        self.resize(1400, 900)

        self._create_scene()

        self._create_view()

        self._create_statusbar()

        self._create_menu()

    def _create_scene(self):

        self.scene = QGraphicsScene()

        self.scene.setSceneRect(-5000, -5000, 10000, 10000)

    def _create_view(self):

        self.view = GraphicsView(self.scene)

        self.setCentralWidget(self.view)

    def _create_statusbar(self):

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)

    def _create_menu(self):

        menu = self.menuBar()

        menu.addMenu("File")

        menu.addMenu("Edit")

        menu.addMenu("View")

        menu.addMenu("Import")

        menu.addMenu("Export")

        menu.addMenu("Help")