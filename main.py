import sys

import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QDialog


class Example(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.outp)
        self.what_draw = random.choice(["RECT", "TRIANGLE"])
        self.setMouseTracking(True)
        self.coord = [30, 30]


    def outp(self):
        x = 300
        y = 300
        self.cor = self.get_xy(x, y)
        self.what_draw = "CERCLE"
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.what_draw == "CERCLE":
            self.draw_flag_3(qp)
        qp.end()

    def draw_flag_3(self, qp):
        qp.setBrush(QColor(250, 50, 170))
        qp.drawEllipse(self.cor[0], self.cor[1], self.cor[2], self.cor[3])

    def mouseMoveEvent(self, event):
        self.coord = event.x(), event.y()

    def get_xy(self, x, y):
        n = random.randint(10, 300)
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
    ex = Example()
    ex.show()
    sys.exit(app.exec())