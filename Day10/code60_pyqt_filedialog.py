# 다이얼로그, 메세지박스
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('새파일 열기')
        openFile.triggered.connect(self.showDialog)

        menuber = self.menuBar()
        menuber.setNativeMenuBar(False)
        fileMenu = menuber.addMenu('&File')
        fileMenu.addAction(openFile)

        # 필수설정
        self.setWindowTitle('파일 다이얼로그')
        self.setGeometry(300, 300, 300, 300)
        self.show() # self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, '파일열기', './')

        if fname[0]: # 파일을 선택했다면
            f = open(fname[0], 'rt', encoding='utf-8') # 읽기모드로 파일열기

            with f:
                data = f.read()
                self.textEdit.setText(data)

            f.close()
    # 메세지 박스 1
        QMessageBox.about(self, '성공', '로드했습니다.') 
    # 메세지 박스 2
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '종료', '정말 종료하시겠습니까?', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept() # 프로그램 종료
        else:
            event.ignore() # 프로그램 계속 진행

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())