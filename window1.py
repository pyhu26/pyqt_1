import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

formClass = uic.loadUiType("MainWindow.ui")[0]

class MyWindow(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnSearch.clicked.connect(self.inquiry)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

    def inquiry(self):
        ## 시간
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

        ## BTC 시세 조회
        price = pykorbit.get_current_price("BTC")
        print( price)
        self.txtIndex.setText(str(price))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
