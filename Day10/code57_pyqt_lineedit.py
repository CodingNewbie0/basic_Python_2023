# 라인에디트 - textbox
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblResult = QLabel(self)
        self.lblResult.move(20, 20)

        txtInput = QLineEdit(self)
        txtInput.setEchoMode(2) # 패스워드 모드
        txtInput.move(20, 40)
        txtInput.textChanged[str].connect(self.onChanged) # 텍스트 안의 글자가 바뀌면 박스안의 글자도 바뀜

        # 필수설정
        self.setWindowTitle('라인에디트')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onChanged(self, text):
        self.lblResult.setText('입력값 : ' + text)
        self.lblResult.adjustSize() # 라벨사이즈 자동


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())