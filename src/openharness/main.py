from PySide6.QtWidgets import QApplication, QLabel
import sys

def main():
    app = QApplication(sys.argv)

    label = QLabel("OpenHarness V0.1.0")
    label.resize(400, 120)
    label.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()