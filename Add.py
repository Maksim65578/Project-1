from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from database import data


class Add(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Design/Add.ui", self)

        self.click = True

        self.close_form.clicked.connect(self.closing)
        self.add_info.clicked.connect(self.add_to_data)

        self.info = ()

    def add_to_data(self):
        name = self.name.text()
        price = self.price.text()
        number = self.number.text()
        description = self.description.toPlainText()
        print(1)
        self.info = name, price, number, description
        self.click = False
        self.closing()

    def closing(self):
        self.close()
