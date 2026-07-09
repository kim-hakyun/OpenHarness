from openharness.gui.main_window import MainWindow


class OpenHarnessApplication:

    def __init__(self, app):

        self.app = app
        self.window = MainWindow()

    def run(self):

        self.window.show()