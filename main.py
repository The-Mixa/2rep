from PyQt5 import QtCore, QtGui, QtWidgets, uic
from random import randint
import sys

class CurcleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)


    def paintEvent(self, event):
        if self.do_paint:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.draw_curcle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_curcle(self, qp):
        r = randint(50, 200)
        qp.setBrush(QtGui.QColor(255, 255, 0))
        qp.drawEllipse(200 - r, 200 - r, r * 2, r * 2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = CurcleDrawer()
    ex.show()
    sys.exit(app.exec())