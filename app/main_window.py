from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QButtonGroup, QDockWidget, QMainWindow, QTextEdit,
    QStackedLayout, QWidget
)

from app.constants import MAIN_WINDOW_TITLE
from app.games import tictactoe
from app.utilities import create_button

GAMES = (
    "TicTacToe",
)


class MainAppWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.setMinimumHeight(250)
        self.setMinimumWidth(500)
        self.add_dock()

        main_layout = QStackedLayout()
        placeholder = QTextEdit()
        placeholder.setText("Why?")
        main_layout.addWidget(placeholder)
        main_layout.addWidget(tictactoe.TicTacToe())

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.button_group.idPressed[int].connect(main_layout.setCurrentIndex)

    def add_dock(self):
        dock = QDockWidget()
        dock.setMinimumWidth(100)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

        self.button_group = QButtonGroup()
        for ind, label in enumerate(GAMES, start=1):
            game_button = create_button(label, label)
            self.button_group.addButton(game_button)
            self.button_group.setId(game_button, ind)
            dock.setWidget(game_button)
