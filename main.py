from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QBrush
import sys
import random
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.flag = False

    def initUI(self):
        uic.loadUi('qwer.ui',
                   self)
        self.pushButton.clicked.connect(self.onClicked)
        self.show()

    def onClicked(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag:
            a = random.randint(10, 200)
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(50, 50, a, a)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
