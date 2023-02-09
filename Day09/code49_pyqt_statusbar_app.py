import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

class MyApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 메뉴바 - 액션
        actSave = QAction(QIcon('./Day09/save.png'), '그의 탄생신화를 기록한다.', self)
        actSave.setShortcut('Ctrl+s')
        actSave.setStatusTip('더마이마이 그를 찬양해야 한다.')

        actpeople = QAction(QIcon('./Day09/people.png'), '찬양한다', self)
        actpeople.setStatusTip('찬양한다.')
        actpeople1 = QAction(QIcon('./Day09/baseball-player.png'), '찬양한다', self)
        actpeople1.setStatusTip('찬양한다.')
        actpeople2 = QAction(QIcon('./Day09/happiness.png'), '찬양한다', self)
        actpeople2.setStatusTip('찬양한다.')
        actpeople3 = QAction(QIcon('./Day09/happy.png'), '찬양한다', self)
        actpeople3.setStatusTip('찬양한다.')
        actpeople4 = QAction(QIcon('./Day09/success.png'), '찬양한다', self)
        actpeople4.setStatusTip('찬양한다.')

        actExit = QAction(QIcon('./Day09/exit.png'), '차단', self)
        actExit.setShortcut('Ctrl+0') # 단축키 지정
        actExit.setStatusTip('나가!!!!!!!!!')
        actExit.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&조')
        filemenu.addAction(actSave)
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar') # 툴바 타이틀은 없어도 됨.
        toolbar.addAction(actSave)
        toolbar.addAction(actpeople)
        toolbar.addAction(actpeople1)
        toolbar.addAction(actpeople2)
        toolbar.addAction(actpeople3)
        toolbar.addAction(actpeople4)
        toolbar.addAction(actExit)

        # 상태바
        now = QDate.currentDate() # 현재 일자
        time = QTime.currentTime() # 현재 시간
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') + ' ' + time.toString('hh:mm:ss'))
        self.setWindowIcon(QIcon('./Day09/ball-bearing.png')) # Icon 불러와서 경로설정
        # GUI 화면 설정
        self.setGeometry(900, 200, 400, 200)
        self.setWindowTitle('조더마이') # 상태창 이름설정
        self.setCenter()
        self.show() # 상태창을 띄움

    # 화면 중심 세팅
    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())