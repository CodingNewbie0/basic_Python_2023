import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('snom') # 상태창 이름설정
        self.setWindowIcon(QIcon('./Day09/snom.jpg')) # Icon 불러와서 경로설정
        self.resize(400, 200) # 상태창의 크기
        self.show() # 상태창을 띄움

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
