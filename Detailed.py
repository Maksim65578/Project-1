from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Detailed(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Design/Detailed.ui", self)

        self.close_form.clicked.connect(self.closing)

    def closing(self):
        self.close()