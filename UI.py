import sys

import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 517)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(384, 462, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Рисовать."))

class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.outp)
        self.cor = []
        self.what_draw = ''

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
        qp.setBrush(QColor(*self.get_rondom_color()))
        qp.drawEllipse(self.cor[0], self.cor[1], self.cor[2], self.cor[3])

    def mouseMoveEvent(self, event):
        self.coord = event.x(), event.y()

    def get_xy(self, x, y):
        n = random.randint(10, 250)
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
    sys.exit(app.exec())

