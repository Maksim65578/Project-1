from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class Add(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Design/Add.ui", self)

        self.close_form.clicked.connect(self.closing)
        self.add.clicked.connect(self.add_to_data)

    def add_to_data(self):
        name = self.name.text()
        price = self.price.text()
        number = self.number.text()
        descryption = self.description.toPlainText()
        print(name, price, number, descryption)
        self.close()

    def closing(self):
        self.close()

