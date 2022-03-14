import sys

from PyQt6.QtWidgets import QApplication

from apps.game_factory import GameFactory


if __name__ == "__main__":
    app = QApplication([""])
    window = GameFactory().get("tic-tac-toe")
    window.show()
    sys.exit(app.exec())
