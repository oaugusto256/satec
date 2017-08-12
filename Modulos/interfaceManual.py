# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceManual.ui'
#
# Created: Tue May 27 16:32:54 2014
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setMinimumSize(QtCore.QSize(483, 290))
        Dialog.setMaximumSize(QtCore.QSize(483, 290))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.checkBox.setFont(font)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "SATEC - Manual do usuário", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Manual do usuário", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:600; font-style:italic;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-style:normal;\">1.</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\"> Clique no assunto desejado para ser estudado na arvore &quot;assuntos&quot;. Seu conteudo será carregado nas abas ao lado  direito.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\"> <br /></span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-style:normal;\">2</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">. Caso necessite pesquisar um assunto que queira estudar, digite-o no campo de pesquisa. Após a pesquisa, caso exista algum conteudo relacionado a ele, o mesmo será carregado nas abas ao lado direito.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\"><br /></span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-style:normal;\">3.</span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\"> Caso tenha alguma dúvida, sugestão, critica e reportar algum bug. Por favor utilize o menu ajuda e clique em sobre para contatar os desenvolvedores. </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\"><br /><br />Bom estudo !</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Dialog", "Marque caso não queira que esta mensagem abra novamente ao iniciar.", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

