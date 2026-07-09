from PySide6.QtWidgets import QMainWindow, QStatusBar

from openharness.gui.graphics_view import GraphicsView
from openharness.gui.scene import HarnessScene


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("OpenHarness V0.1.0")
        self.resize(1400, 900)

        self.scene = HarnessScene()
        self.view = GraphicsView(self.scene)

        self.setCentralWidget(self.view)

        self._create_menu()
        self._create_statusbar()

    def _create_menu(self) -> None:
        menu = self.menuBar()
        menu.addMenu("File")
        menu.addMenu("Edit")
        menu.addMenu("View")
        menu.addMenu("Import")
        menu.addMenu("Export")
        menu.addMenu("Help")

    def _create_statusbar(self) -> None:
        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)