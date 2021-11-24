import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        uic.loadUi(
            'C:\\Users\\Софья\\PycharmProjects\\git\\q.ui',
            self)
        self.pushButton.clicked.connect(self.paintEvent)


    def paintEvent(self):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        a = random.randint(10, 100)
        qp.drawEllipse(50, 50, a, a)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
