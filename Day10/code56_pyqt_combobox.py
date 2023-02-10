# 콤보박스
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() # self는 클래스 함수 자신을 의미.

    def initUI(self):
        # 
        self.lblOption = QLabel('\'조민재\'', self)
        self.lblOption.move(20, 20)

        cbOption = QComboBox(self)
        cbOption.addItem('찬양한다')
        cbOption.addItem('받든다')
        cbOption.addItem('전율한다')
        cbOption.addItem('감사를 드린다')
        cbOption.addItem('충성을 맹세한다')
        cbOption.move(20, 40)
        cbOption.activated[str].connect(self.onActivated)

        # 필수 설정
        self.setWindowTitle('콤보 박스')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onActivated(self, text):
        self.lblOption.setText('\'신\' : ' + text)
        self.lblOption.adjustSize() # 글자수만큼 라벨넓이를 설정 

    def checkKorea(self, state):
        if state == Qt.CheckState.Checked: # QT.Checked 도 사용가능
            self.setWindowTitle('나는 한국인')
        else:
            self.setWindowTitle('나는 뭐지')

    def changeTitle(self, state):
        if state == Qt.CheckState.Checked: # QT.Checked 도 사용가능
            self.setWindowTitle('체크박스 체크')
        else:
            self.setWindowTitle('체크박스 체크해제')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
