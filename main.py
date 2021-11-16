from PyQt5.QtGui import QPainter, QColor
from random import sample
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.a = False
        self.pushButton.clicked.connect(self.circle)

    def circle(self):
        self.a = True
        self.update()

    def paintEvent(self, event):
        if self.a:
            qp = QPainter()
            qp.begin(self)
            self.do(qp)
            qp.end()

    def do(self, qp):
        self.coords = sample(range(500), 2)
        self.coords_x = sample(range(200), 1)
        self.sq = sample(range(10, 100, 2), 1)
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(self.coords[0] + self.coords_x[0], self.coords[1], self.sq[0], self.sq[0])
        self.a = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
