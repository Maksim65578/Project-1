import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QHeaderView
from Add import Add
from Detailed import Detailed
from Change import Change
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
        self.table.selectionModel().selectionChanged.connect(self.do_some_fackin_magic)

        self.detailed_click = False
        self.change_click = False
        self.info = ()

    def add_to_data(self, info):
        data.add(info)
        print(info)

    def initTable(self, inf):
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Название", "Цена за 1 шт.", "Количество", "Итого"])
        self.table.setRowCount(0)
        items = inf
        for i, row in enumerate(items):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(list(row)):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))
            self.table.setItem(i, 3, QTableWidgetItem(str(row[1] * row[2])))

    def do_some_fackin_magic(self, selected):
        for numb, ix in enumerate(selected.indexes()):
            row, column = ix.row(), ix.column()
            if numb == 1:
                print(2222)
                return
            print(row, column)

        inf = data.get_row(row)[0]

        if self.change_click:
            self.change.show()
            self.change_click = False
        if self.detailed_click:
            self.detailed.show()
            self.detailed_click = False

        self.line_name.setText(inf[0])
        self.line_price.setText(str(inf[1]))
        self.line_number.setText(str(inf[2]))
        self.line_total.setText(str(inf[1] * inf[2]))

    def add_form(self):
        self.add = Add()
        self.add.show()

    def detailed_form(self):
        self.detailed = True
        self.detailed = Detailed()

    def change_form(self):
        self.change_click = True
        self.change = Change()

    def closing(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
