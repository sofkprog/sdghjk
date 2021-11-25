import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('q.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.pushButton.clicked.connect(self.pain)

    def pain(self):
        title1 = self.connection.cursor().execute(f"""SELECT id FROM Shows
                WHERE title = '{self.sender().text()}'""").fetchall()
        title2 = self.connection.cursor().execute(f"""SELECT title FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        state = self.connection.cursor().execute(f"""SELECT [степень обжарки] FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        seria = self.connection.cursor().execute(f"""SELECT [молотый/в зернах] FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        nomer = self.connection.cursor().execute(f"""SELECT [описание вкуса] FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        massa = self.connection.cursor().execute(f"""SELECT цена FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        level = self.connection.cursor().execute(f"""SELECT [объем упаковки] FROM Shows
                        WHERE title = '{self.sender().text()}'""").fetchall()
        self.label_8.setText(*title1[0])
        self.label_9.setText(*title2[0])
        self.label_10.setText(*state[0])
        self.label_11.setText(*seria[0])
        self.label_12.setText(str(*nomer[0]))
        self.label_13.setText(str(*massa[0]))
        self.label_14.setText(*level[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
