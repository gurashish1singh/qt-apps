from unittest import TestCase

from parameterized import parameterized
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton

from app.utilities import create_button, create_label
from tests.common import press_event


test_app = QApplication([""])


class TestUtilites(TestCase):

    @parameterized.expand([
        ("test_button", "", None),
        ("test_button", "second_test", press_event),
    ])
    def test_create_button(self, label, object_name, connector):
        actual_buton = create_button(label, object_name, connector)
        self.assertIsInstance(actual_buton, QPushButton)
        self.assertEqual(actual_buton.text(), label)
        self.assertEqual(actual_buton.objectName(), object_name)
        self.assertFalse(actual_buton.isCheckable())
        self.assertFalse(actual_buton.isChecked())
        actual_buton.click()

    @parameterized.expand([
        ("",),
        ("test_label",),
    ])
    def test_create_label(self, label):
        actual_label = create_label(label)
        self.assertIsInstance(actual_label, QLabel)
        self.assertEqual(actual_label.text(), label)
