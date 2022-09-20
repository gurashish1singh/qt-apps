from typing import Callable

from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
)


def create_button(label: str, object_name: str = "", connector: Callable = None) -> QPushButton:
    button = QPushButton(label)
    if connector:
        button.clicked.connect(connector)
    button.setObjectName(object_name)
    return button


def create_label(text: str) -> QLabel:
    label = QLabel(text)
    return label
