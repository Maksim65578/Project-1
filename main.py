import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from Design.Add import Add
from Design.Detailed import Detailed
from Design.Change import Change
from database import data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Design/MainWindow.ui", self)
        self.initTable(data.get())

        self.add.clicked.connect(self.add_form)
        self.detailed.clicked.connect(self.detailed_form)
        self.change.clicked.connect(self.change_form)
        self.close_form.clicked.connect(self.closing)

    def initTable(self, inf):
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Название", "Цена за 1 шт.", "Количество", "Итого"])
        self.table.setRowCount(0)
        items = inf
        for i, row in enumerate(items):
            self.table.setRowCount(self.table.rowCount() + 1)
            print(row)
            for j, elem in enumerate(list(row)):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))
            self.table.setItem(i, 3, QTableWidgetItem(str(row[1] * row[2])))

    def add_form(self):
        self.add = Add()
        self.add.show()

    def detailed_form(self):
        self.detailed = Detailed()
        self.detailed.show()

    def change_form(self):
        self.change = Change()
        self.change.show()

    def closing(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
