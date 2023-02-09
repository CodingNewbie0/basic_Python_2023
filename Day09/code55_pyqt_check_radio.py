# 체크박스, 라디오버튼
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 체크박스(다중선택)
        cbshowTitle = QCheckBox('Show title', self)
        cbshowTitle.move(20, 20)
        cbshowTitle.toggle()
        # signal 종류 stateChanged
        # connect() 매개변수 -> 슬롯함수
        cbshowTitle.stateChanged.connect(self.changeTitle)

        cbKorea = QCheckBox('한국', self)
        cbKorea.move(20, 40)
        cbKorea.stateChanged.connect(self.checkKorea)

        # 라디오버튼(단일선택)
        rbtn1 = QRadioButton('남성', self)
        rbtn1.move(150, 20)
        rbtn1.setChecked(True)
        rbtn1 = QRadioButton('여성', self)
        rbtn1.move(150, 40)


        # 필수 설정
        self.setWindowTitle('체크 박스')
        self.setGeometry(300, 300, 300, 300)
        self.show()

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
