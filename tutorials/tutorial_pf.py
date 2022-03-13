import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
)

from tutorial_pf_utils import (
    BUTTON_STYLE, CHECKBOX_STYLE, CLICKED_ME, create_button, create_check_box,
    create_combo_box, create_group_box, create_label, create_line_edit,
    create_list, create_radio_button, create_spin_boxes, LINE_STYLE, LIST_STYLE,
    TABLE_STYLE, WINDOW_STYLE,
)


class ChapterFactory:
    def __init__(self, chapter: int) -> None:
        self.chapter = chapter

    def get(self):
        CHAPTERS = {
            1: ButtonsAndLabels, 2: LayoutManagement,
            3: LineEdits, 4: GroupsAndRadios,
            5: CheckBox, 6: SpinBoxing,
            7: Tables, 8: Lists,
            9: ComboBox
        }
        return CHAPTERS.get(self.chapter)


class ButtonsAndLabels(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Basic App")
        self.setGeometry(500, 400, 300, 400)
        self.setStyleSheet(WINDOW_STYLE)
        self.create_widget()

    def create_widget(self):
        # Do not know why this takes self yet
        button = QPushButton("Does this work?", self)
        button.setGeometry(100, 100, 99, 99)
        button.setStyleSheet(BUTTON_STYLE)
        button.clicked.connect(self.clicked_it)

        self.label = QLabel("Lets see if label works", self)
        self.label.setGeometry(75, 201, 200, 50)
        self.label.setFont(QFont("Cascadia Code"))

    def clicked_it(self):
        self.label.setText("Oh did you click me?")
        self.label.setStyleSheet(CLICKED_ME)


class LayoutManagement(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Testing Layouts")
        self.setGeometry(500, 400, 300, 400)
        self.setStyleSheet(WINDOW_STYLE)

        # Vertical Layout
        vbox = QVBoxLayout()
        V_BUTTONS = {
            "yo yo": str.casefold,
            "he he": str.lower,
            "blah": str.upper
        }
        for label, connector in V_BUTTONS.items():
            button = create_button(label, connector)
            button.setGeometry(100, 100, 99, 99)
            vbox.addWidget(button)
        # self.setLayout(vbox)

        # Horizontal layout
        hbox = QHBoxLayout()
        H_BUTTONS = {
            "yo yo": str.casefold,
            "he he": str.lower,
            "blah": str.upper
        }
        for label, connector in H_BUTTONS.items():
            button = create_button(label, connector)
            button.setGeometry(200, 200, 99, 99)
            hbox.addWidget(button)
        # self.setLayout(hbox)

        # Grid layout
        grid = QGridLayout()
        G_BUTTONS = {
            "ayo": (str.casefold, (0, 0)),
            "he he": (str.lower, (1, 1)),
            "blah": (str.upper, (2, 3))
        }
        for label, (connector, where) in G_BUTTONS.items():
            button = create_button(label, connector)
            button.setGeometry(200, 200, 99, 99)
            grid.addWidget(button, *where)
        self.setLayout(grid)

    def clicked_it(self):
        self.label.setText("Oh did you click me?")
        self.label.setStyleSheet(CLICKED_ME)


class LineEdits(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Line Edits!")
        self.setGeometry(500, 400, 300, 400)
        self.setStyleSheet(WINDOW_STYLE)

        # Grid Layout
        grid = QGridLayout()
        self.line = QLineEdit()
        self.line.setStyleSheet(LINE_STYLE)
        self.line.setFont(QFont("Anonymous Pro Bold"))
        self.line.setPlaceholderText("Que?")
        button = create_button("Click Me!!", self.change_color)
        button.setStyleSheet(BUTTON_STYLE)

        grid.addWidget(self.line, 0, 1)
        grid.addWidget(button, 0, 2)
        self.setLayout(grid)

    def change_color(self):
        self.line.setStyleSheet(CLICKED_ME)


class GroupsAndRadios(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Line Edits!")
        self.setGeometry(500, 400, 300, 400)
        self.setStyleSheet(WINDOW_STYLE)

        RADIO_BUTTONS = {
            "Testing": ("Anonymous Pro Bold", 15),
            "Different": ("Cascadia Code", 16),
            "Fonts": ("Ununtu Mono Italic", 13)
        }
        # Vertical Layout for buttons
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        group_box = create_group_box("Random group box")
        for label, (font, size) in RADIO_BUTTONS.items():
            radio_button = create_radio_button(label, font, size)
            radio_button.toggled.connect(self.change_text)
            hbox.addWidget(radio_button)

        self.label = create_label("HOLA")

        # Adding layouts
        group_box.setLayout(hbox)
        vbox.addWidget(group_box)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def change_text(self):
        radio = self.sender()
        if radio.isChecked():
            self.label.setText(radio.text())
            self.label.setStyleSheet(CLICKED_ME)


class CheckBox(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Check boxes and all!")
        self.setGeometry(500, 400, 300, 400)
        self.setStyleSheet(WINDOW_STYLE)

        CHECKBOXES = {
            "Check me Out!": ("Sansserif", 16),
            "Hola!": ("Times New Roman", 13),
            "Hello": ("Sansserif", 14)
        }
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        for label, (font, size) in CHECKBOXES.items():
            checkbox = create_check_box(label, font, size)
            checkbox.setStyleSheet(CHECKBOX_STYLE)
            checkbox.toggled.connect(self.change_text)
            hbox.addWidget(checkbox)

        self.label = create_label("IS this how this is?")
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def change_text(self):
        checkbox = self.sender()
        if checkbox.isChecked():
            self.label.setText(checkbox.text())
            self.label.setStyleSheet(CLICKED_ME)


class SpinBoxing(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Check boxes and all!")
        self.setGeometry(500, 400, 500, 200)
        self.setStyleSheet(WINDOW_STYLE)

        hbox = QHBoxLayout()
        heading = create_label("Is this Spinnig?", "Cascadia Code", 16)
        self.power = create_line_edit("gimme power", "Times New Roman", 14)
        self.result = create_line_edit("", "Arial", 13)
        self.spinny = create_spin_boxes()
        self.spinny.valueChanged.connect(self.get_power)

        hbox.addWidget(heading)
        hbox.addWidget(self.power)
        hbox.addWidget(self.spinny)
        hbox.addWidget(self.result)
        self.setLayout(hbox)

    def get_power(self):
        if self.power.text():
            dial = int(self.power.text())
            dialled_up = self.spinny.value() * dial
            self.result.setText(str(dialled_up))


class Tables(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Check boxes and all!")
        self.setGeometry(500, 400, 500, 200)
        self.setStyleSheet(WINDOW_STYLE)

        vbox = QVBoxLayout()
        table = QTableWidget()
        table.setRowCount(3)
        table.setColumnCount(3)

        table.setItem(0, 0, QTableWidgetItem("First"))
        table.setItem(0, 1, QTableWidgetItem("Last"))
        table.setItem(0, 2, QTableWidgetItem("Greet"))
        table.setItem(1, 0, QTableWidgetItem("Rob"))
        table.setItem(1, 1, QTableWidgetItem("Idiot"))
        table.setItem(1, 2, QTableWidgetItem("Yo!"))

        table.setStyleSheet(TABLE_STYLE)

        vbox.addWidget(table)
        self.setLayout(vbox)

    def get_power(self):
        if self.power.text() != 0:
            dial = int(self.power.text())
            dialled_up = self.spinny.value() * dial
            self.result.setText(str(dialled_up))


class Lists(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Check boxes and all!")
        self.setGeometry(500, 400, 500, 200)
        self.setStyleSheet(WINDOW_STYLE)

        vbox = QVBoxLayout()
        list_widget = create_list([
            "Hello?", "Does this work", "Eh", "Maybe?"
        ])
        list_widget.setStyleSheet(LIST_STYLE)
        list_widget.clicked.connect(self.change_text)
        self.label = create_label("DOIT list")

        vbox.addWidget(self.label)
        vbox.addWidget(list_widget)
        self.setLayout(vbox)

    def change_text(self):
        item = self.sender().currentItem()
        self.label.setText(item.text())


class ComboBox(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Check boxes and all!")
        self.setGeometry(500, 400, 500, 200)
        self.setStyleSheet(WINDOW_STYLE)

        vbox = QVBoxLayout()
        self.label = create_label("Comboxing it!", size=12)
        cb = create_combo_box(
            ["blah", "more blah", ":too mch"]
        )
        cb.currentTextChanged.connect(self.change_text)

        vbox.addWidget(cb)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def change_text(self):
        item = self.sender().currentText()
        self.label.setText(item)


def create_application(chapter: list[int]):
    chapter = int(chapter[-1]) if len(chapter) == 2 \
                else sys.exit("ERROR. Can only accept 1 argument.")
    # usually its sys.argv, need to read up on what it does
    app = QApplication([""])
    window = ChapterFactory(chapter).get()()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    create_application(sys.argv)
