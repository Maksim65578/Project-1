from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Change(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Design/Change.ui", self)

        self.close_form.clicked.connect(self.closing)

    def show_info(self):
        self.name.setText(self.name_info)

    def closing(self):
        self.close()