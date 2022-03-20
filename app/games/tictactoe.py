from functools import cached_property

from PyQt6.QtWidgets import QPushButton, QGridLayout, QVBoxLayout, QWidget

from app.utilities import create_button, create_label


class TicTacToe(QWidget):

    RESET_LABEL_STATE = "X goes first"
    START_OVER = "Start Over"
    START_OVER_STYLE = (
        "color: #080307"
    )
    TAC_BUTTONS = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        "9": (2, 2),
    }
    WINNER_STYLE = (
        "color: #c70aba"
    )
    WINNER_WINNER_CHICKEN_DINNER = {
        "across": (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9)
        ),
        "down": (
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9)
        ),
        "diagnal": (
            (1, 5, 9),
            (3, 5, 7)
        )
    }

    def __init__(self) -> None:
        super().__init__()
        # Vertical layout for labels and reset button
        vbox = QVBoxLayout()
        # Grid layout for tac buttons
        tac_grid = QGridLayout()

        # Using a simple counter to switch between X and O
        self.counter = 0
        for index, (x, y) in self.TAC_BUTTONS.items():
            button = create_button("", object_name=f"button_{index}", connector=self.clicker)
            tac_grid.addWidget(button, x, y)
        self.player = create_label(self.RESET_LABEL_STATE)
        reset_button = create_button(self.START_OVER, connector=self.start_over)

        vbox.addItem(tac_grid)
        vbox.addWidget(self.player)
        vbox.addWidget(reset_button)
        self.setLayout(vbox)

    def clicker(self) -> None:
        button_clicked = self.sender()
        if self.counter % 2 == 0:
            button_clicked.setText("X")
            self.player.setText("O goes next")
        else:
            button_clicked.setText("O")
            self.player.setText("X goes next")
        self.counter += 1
        button_clicked.setEnabled(False)
        self.check_winner()

    def check_winner(self) -> None:
        for _, combinations in self.WINNER_WINNER_CHICKEN_DINNER.items():
            for index_1, index_2, index_3 in combinations:
                one = self.applicable_buttons[index_1 - 1]
                two = self.applicable_buttons[index_2 - 1]
                three = self.applicable_buttons[index_3 - 1]
                if one.text() != "" and (one.text() == two.text() == three.text()):
                    self.winner(one, two, three)

        if all(not button.isEnabled() for button in self.applicable_buttons):
            self.player.setText("DRAW! Start over!")

    @cached_property
    def applicable_buttons(self) -> list[QPushButton]:
        applicable_buttons = [
            button for button in self.children() if isinstance(button, QPushButton) and button.text() != self.START_OVER
        ]
        return applicable_buttons

    def winner(self, button_one: QPushButton, button_two: QPushButton, button_three: QPushButton) -> None:
        button_one.setStyleSheet(self.WINNER_STYLE)
        button_two.setStyleSheet(self.WINNER_STYLE)
        button_three.setStyleSheet(self.WINNER_STYLE)
        self.player.setText(f"{button_one.text()} Wins!")
        self.disable_input()

    def disable_input(self):
        for button in self.applicable_buttons:
            button.setEnabled(False)

    def start_over(self) -> None:
        for button in self.applicable_buttons:
            button.setText("")
            button.setEnabled(True)
            button.setStyleSheet(self.START_OVER_STYLE)
        self.player.setText(self.RESET_LABEL_STATE)
        self.counter = 0
