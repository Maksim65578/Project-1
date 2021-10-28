from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Change(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Design/Change.ui", self)

        self.close.clicked.connect(self.close_form)

    def close_form(self):
        self.close()