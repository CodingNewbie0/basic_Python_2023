import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # GUI 화면 설정
        btn = QPushButton('안녕히.....', self)
        btn.move(80, 120)
        btn.resize(btn.sizeHint())
        # 버튼 툴팁
        btn.setToolTip('누르면<b>안대</b>!!!!!!!')
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        btn = QPushButton('가세요.....', self)
        btn.move(240, 120)
        btn.resize(btn.sizeHint())
        btn.setToolTip('누르면<b>안대</b>!!!!!!!')
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setGeometry(900, 200, 400, 200)
        self.setWindowTitle('snom') # 상태창 이름설정
        self.setWindowIcon(QIcon('./Day09/snom.jpg')) # Icon 불러와서 경로설정
        self.show() # 상태창을 띄움

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())