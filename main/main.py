import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from Add import Add
from Detailed import Detailed
from Change import Change


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainWindow.ui", self)

        self.add.clicked.connect(self.add_form)
        self.detailed.clicked.connect(self.detailed_form)
        self.change.clicked.connect(self.change_form)

    def add_form(self):
        self.add = Add()
        self.add.show()

    def detailed_form(self):
        self.detailed = Detailed()
        self.detailed.show()

    def change_form(self):
        self.change = Change()
        self.change.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

