# 박스 레이아웃
import sys
from PyQt5.QtWidgets import *

class Yourapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title : '), 0, 0)
        grid.addWidget(QLabel('Author : '), 1, 0)
        grid.addWidget(QLabel('Review : '), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1) # 0행 1렬
        grid.addWidget(QLineEdit(), 1, 1) # 1행 1렬
        grid.addWidget(QTextEdit(), 2, 1) # 2행 1렬

        btnOk = QPushButton('OK')
        btnCancal = QPushButton('Cancal')

        grid.addWidget(btnOk, 3, 1)
        # grid.addWidget(btnCancal, 3, 1) # 이미 ok버튼이 들어가있는 자리임

        # 필수 설정
        self.setWindowTitle('박스 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yourapp()
    sys.exit(app.exec_())
