from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from tokenization import get_tokens_list
from plot import tiny_transitions


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 230, 150, 50))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 60, 400, 150))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 150, 40))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(550, 60, 400, 320))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 20, 80, 40))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 360, 60, 40))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 300, 260, 40))
        self.label_4.setObjectName("label_4")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(30, 400, 1000, 400))
        self.webEngineView.setObjectName("webEngineView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TINY Language Compiler"))
        self.pushButton.setText(_translate("MainWindow", "Tokenize Code"))
        self.pushButton.clicked.connect(self.onClickTokenize)
        self.label.setText(_translate("MainWindow", "Insert your code here:"))
        
        self.textEdit.setPlaceholderText(
        """Example:
            IF 1 THEN
            x := y;
            ELSE IF 2 THEN
            x := z;
            ELSE
            x:= 0;
            END""")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Token"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Current State"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Next State"))
        self.tableWidget.setColumnWidth(0, 70)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.label_2.setText(_translate("MainWindow", "Tokens List:"))
        self.label_3.setText(_translate("MainWindow", "DFA:"))
        self.label_4.setText(_translate("MainWindow",u"<html><head/><body><h2><span style=\" color:#ff0000;\">Invalid IF statement!!!</span></h2></body></html>"))
        self.label_4.hide()
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))

    def onClickTokenize(self):
        input_code = str(self.textEdit.toPlainText())
        tokens = self.get_tokens_tabledata(input_code)
        if tokens is None:
            self.webEngineView.close()
            self.label_4.show()
            self.tableWidget.setRowCount(0)
        else:
            self.label_4.hide()
            self.webEngineView.load(QtCore.QUrl.fromLocalFile("\DFA.html"))
            self.webEngineView.show()
            self.tableWidget.setRowCount(len(tokens))
            row = 0
            for token in tokens:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(token["token"]))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(token["type"]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(token["current"]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(token["next"]))
                row = row + 1

    def get_tokens_tabledata(self, input_code):
        tokens_list = get_tokens_list(input_code)
        if tokens_list is None:
            return None
        else:
            current = '1'
            for token in tokens_list:
                token["current"] = current
                next = tiny_transitions[current][token["type"]]
                token["next"] = next
                current = next
            return tokens_list
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
