from PySide6.QtWidgets import QApplication, QLabel
import sys

from PySide6.QtWidgets import QApplication

from openharness.app import OpenHarnessApplication


def main():

    app = QApplication(sys.argv)

    application = OpenHarnessApplication(app)

    application.run()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()