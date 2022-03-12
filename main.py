import sys

from PyQt6.QtWidgets import QApplication, QWidget

STYLE = (
    "background-color: #f57f7f"
)


class Window(QWidget):

    def __init__(self) -> None:
        super().__init__()
        print(self.__dir__())
        self.setWindowTitle("Basic App")
        self.setGeometry(500, 400, 300, 400)
        self.setStyleSheet(STYLE)


def create_application():
    app = QApplication([""])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    create_application()
