import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('엑박') # 상태창 이름설정
        # self.move(720, 360) # 모니터 화면상의 상태창 위치설정(왼쪽 위 대각선 기준)
        self.move(1440 // 2 - 200, 900 // 2 - 100) # 정중앙 위치잡기
        self.resize(400, 200) # 상태창의 크기
        self.show() # 상태창을 띄움

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())