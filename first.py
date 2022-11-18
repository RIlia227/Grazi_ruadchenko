import math
import sys

import random

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QDialog


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.cor = []
        self.pushButton.clicked.connect(self.outp)

    def outp(self):
        print(678678)
        self.cor = self.get_xy(200, 200)
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag_3(qp)
        qp.end()

    def draw_flag_3(self, qp):
        qp.setBrush(QColor(250, 40, 170))
        qp.drawEllipse(self.cor[0], self.cor[1], self.cor[2], self.cor[3])

    def get_xy(self, x, y):
        n = random.randint(10, 100)
        sp_xy = []
        sp_xy.append(x - n)
        sp_xy.append(y - n)
        sp_xy.append(n)
        sp_xy.append(n)
        return sp_xy

    def get_rondom_color(self):
        color = []
        for i in range(3):
            color.append(random.randint(0, 255))
        return color


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())