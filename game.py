import sys

from PyQt6.QtWidgets import QApplication

from app.main_window import MainAppWindow


if __name__ == "__main__":
    app = QApplication([""])
    window = MainAppWindow()
    window.show()
    sys.exit(app.exec())
