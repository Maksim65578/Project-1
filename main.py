import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget
from Design.Add import Add
from Design.Detailed import Detailed
from Design.Change import Change
from database import data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Design/MainWindow.ui", self)
        self.loadTable()

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

    def loadTable(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels(["№", "Название", "Цена за 1 шт.", "Количество", "Итого"],)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
