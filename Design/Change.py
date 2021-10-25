from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Change(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Change.ui", self)