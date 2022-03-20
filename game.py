import sys

from PyQt6.QtWidgets import QApplication

from app.main_window import MainAppWindow
from app.themes.themes import ELEGANT_DARK, MANJARO, MATERIAL, TESTING


if __name__ == "__main__":
    app = QApplication([""])
    # with open(TESTING, "r") as theme:
    #     app.setStyleSheet(theme.read())
    window = MainAppWindow()
    window.show()
    sys.exit(app.exec())
