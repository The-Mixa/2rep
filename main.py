from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import sys

class CurcleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 450)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 400, 361, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.paint)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Рисовать круг"))

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
        qp.setBrush(QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(200 - r, 200 - r, r * 2, r * 2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = CurcleDrawer()
    ex.show()
    sys.exit(app.exec())