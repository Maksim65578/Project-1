from  PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Detailed(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Detailed.ui", self)