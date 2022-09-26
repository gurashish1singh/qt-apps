from typing import Callable

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QGroupBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QRadioButton,
    QSpinBox,
)


BUTTON_STYLE = "background-color: #befef4"
CHECKBOX_STYLE = "background-color: #7951fb"
CLICKED_ME = "background-color: #e9dc67"
LINE_STYLE = "background-color: #dafbf3"
LIST_STYLE = "background-color: #bedcfe"
TABLE_STYLE = "background-color: #887ccb"
WINDOW_STYLE = "background-color: #3ea8fe"


def create_button(label: str, connector: Callable) -> QPushButton:
    button = QPushButton(label)
    button.setStyleSheet(BUTTON_STYLE)
    button.clicked.connect(connector)
    return button


def create_label(text: str, font: str = "Arial", size: int = 13) -> QLabel:
    label = QLabel(text)
    label.setFont(QFont(font, size))
    return label


def create_group_box(label: str) -> QGroupBox:
    group_box = QGroupBox(label)
    group_box.setFont(QFont("Ubuntu Mono Italic", 14))
    return group_box


def create_radio_button(label: str, font: str, size: int) -> QRadioButton:
    radio_button = QRadioButton(label)
    radio_button.setFont(QFont(font, size))
    return radio_button


def create_check_box(label: str, font: str, size: int) -> QCheckBox:
    check_box = QCheckBox(label)
    check_box.setFont(QFont(font, size))
    return check_box


def create_line_edit(label: str, font: str, size: int) -> QLineEdit:
    line_edit = QLineEdit()
    line_edit.setFont(QFont(font, size))
    return line_edit


def create_spin_boxes() -> QSpinBox:
    spin_box = QSpinBox()
    return spin_box


def create_list(items: list[str]) -> QListWidget:
    list_widget = QListWidget()
    for id, item in enumerate(items):
        list_widget.insertItem(id, item)
        list_widget.setFont(QFont("Monospace", 16))
    return list_widget


def create_combo_box(items: list[str]) -> QComboBox:
    combo_box = QComboBox()
    for item in items:
        combo_box.addItem(item)
    return combo_box
