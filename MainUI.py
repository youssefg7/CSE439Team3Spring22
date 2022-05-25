from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
from AnimatedGUI import Ui_MainWindow
from ParserUI import ParserUi

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi,self).__init__()
        uic.loadUi('ui\MainGUI.ui',self)
        #self.setFixedSize(804, 156)

        self.parserPushButton.clicked.connect(self.onClickParser)
        self.scannerPushButton.clicked.connect(self.onClickScanner)
        #self.show()

    def onClickParser(self):
        parserUi = ParserUi()
        stackedWidget.addWidget(parserUi)
        stackedWidget.setGeometry(QtCore.QRect(500,50,1000,1000))
        stackedWidget.setCurrentIndex(stackedWidget.currentIndex() + 1)
    
    def onClickScanner(self):
        scannerUi = Ui_MainWindow()
        stackedWidget.addWidget(scannerUi)
        stackedWidget.setGeometry(QtCore.QRect(500,50,1080,1000))
        stackedWidget.setCurrentIndex(stackedWidget.currentIndex() + 1)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainUi = MainUi()
    stackedWidget = QtWidgets.QStackedWidget()
    stackedWidget.addWidget(mainUi)
    stackedWidget.setGeometry(QtCore.QRect(500,200,820,620))
    stackedWidget.show()
    app.exec_()