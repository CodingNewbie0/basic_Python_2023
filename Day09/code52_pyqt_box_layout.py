# 박스 레이아웃
import sys
from PyQt5.QtWidgets import *

class Yourapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOk = QPushButton('OK')
        btnCancal = QPushButton('Cancal')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btnOk)
        hbox.addWidget(btnCancal)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # 필수 설정
        self.setWindowTitle('절대 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yourapp()
    sys.exit(app.exec_())
