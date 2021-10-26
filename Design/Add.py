from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class Add(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Design/Add.ui", self)

