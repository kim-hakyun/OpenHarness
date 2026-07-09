from PySide6.QtWidgets import QLabel, QMainWindow, QStatusBar

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
        self._connect_signals()

    def _create_menu(self) -> None:
        menu = self.menuBar()
        menu.addMenu("File")
        menu.addMenu("Edit")
        menu.addMenu("View")
        menu.addMenu("Import")
        menu.addMenu("Export")
        menu.addMenu("Help")

    def _create_statusbar(self) -> None:
        self.status = QStatusBar()

        self.ready_label = QLabel("Ready")
        self.coord_label = QLabel("X: 0.00   Y: 0.00")
        self.zoom_label = QLabel("Zoom: 100%")

        self.status.addWidget(self.ready_label)
        self.status.addPermanentWidget(self.coord_label)
        self.status.addPermanentWidget(self.zoom_label)

        self.setStatusBar(self.status)

    def _connect_signals(self) -> None:
        self.view.mouse_position_changed.connect(self._update_mouse_position)
        self.view.zoom_changed.connect(self._update_zoom)

    def _update_mouse_position(self, x: float, y: float) -> None:
        self.coord_label.setText(f"X: {x:.2f}   Y: {y:.2f}")

    def _update_zoom(self, zoom_percent: int) -> None:
        self.zoom_label.setText(f"Zoom: {zoom_percent}%")