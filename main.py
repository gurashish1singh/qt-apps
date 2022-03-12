import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication, QLabel, QPushButton, QWidget
)

BUTTON_STYLE = (
    "background-color: #befef4"
)
WINDOW_STYLE = (
    "background-color: #f57f7f"
)


class Window(QWidget):

    def __init__(self) -> None:
        super().__init__()
        print(self.__dir__())
        self.setWindowTitle("Basic App")
        self.setGeometry(500, 400, 300, 400)
        self.setStyleSheet(WINDOW_STYLE)
        self.create_widget()

    def create_widget(self):
        # Do not know why this takes self yet
        button = QPushButton("Does this work?", self)
        button.setGeometry(100, 100, 99, 99)
        button.setStyleSheet(BUTTON_STYLE)

        label = QLabel("Lets see if label works", self)
        label.setGeometry(75, 201, 200, 50)
        label.setFont(QFont("Cascadia Code"))


def create_application():
    # usually its sys.argv, need to read up on what it does
    app = QApplication([""])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    create_application()
