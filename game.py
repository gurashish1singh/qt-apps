import sys

from PyQt6.QtWidgets import QApplication

from apps.tictactoe import TicTacToe


if __name__ == "__main__":
    app = QApplication([""])
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
