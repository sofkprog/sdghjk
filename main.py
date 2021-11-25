from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QBrush
import sys
import random


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.flag = False

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Супрематизм')
        self.btn = QPushButton("Кнопка", self)
        self.btn.move(400, 400)
        self.btn.clicked.connect(self.onClicked)
        self.show()

    def onClicked(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag:
            a = random.randint(10, 500)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(10, 10, a, a)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
