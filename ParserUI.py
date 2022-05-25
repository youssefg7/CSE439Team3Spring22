from PyQt5 import QtWidgets, uic, QtGui, QtWebEngineWidgets, QtCore
import sys
import os.path

from Parser import Parser

class ParserUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(ParserUi,self).__init__()
        uic.loadUi('ui\ParserGUI.ui',self)
        #self.setFixedSize(804, 156)
        self.validSyntaxGroup.hide()
        self.invalidSyntaxGroup.hide()            
        self.parsingResultGroup.hide()

        self.parser = Parser()
        self.parseCodePushButton.clicked.connect(self.onClickParse)
        self.showParsingTableAction.triggered.connect(self.onClickShowParsingTable)
        self.show()

    def onClickParse(self):
        input_code = str(self.inputCodeTextEdit.toPlainText()).strip()
        print(input_code)
        if input_code == "":
            self.errorMessageLabel.setText("Empty input!")
            self.validSyntaxGroup.hide()
            self.invalidSyntaxGroup.hide()
            self.parsingResultGroup.hide()
        else:
            parsing_result, error_message = self.parser.parse(input_code)
            if(parsing_result):
                self.validSyntaxGroup.show()
                self.invalidSyntaxGroup.hide()            
                self.parsingResultGroup.show()
                self.parseTreeWebEngineView.load(QtCore.QUrl.fromLocalFile(os.path.abspath("Parse Tree.html")))
            else:
                self.errorMessageLabel.setText(error_message)
                self.validSyntaxGroup.hide()
                self.invalidSyntaxGroup.show()            
                self.parsingResultGroup.show()
                self.parseTreeWebEngineView.load(QtCore.QUrl.fromLocalFile(os.path.abspath("Parse Tree.html")))

    def onClickShowParsingTable(self):
        tableDialog = TableDialog()
        #tableDialog.exec()
        #tableDialog.show()

class TableDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui\TableDialog.ui',self)
        #self.setFixedSize(self.width, self.height)
        self.okPushButton.clicked.connect(self.hide)
        self.exec()
                


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ParserUi()
    app.exec_()