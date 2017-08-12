# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceSobre.ui'
#
# Created: Mon Apr 28 13:46:05 2014
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 380)
        Dialog.setMinimumSize(QtCore.QSize(490, 380))
        Dialog.setMaximumSize(QtCore.QSize(490, 380))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(111, 11, 116, 19))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(111, 36, 371, 331))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser.setPalette(palette)
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.labelLogo = QtGui.QLabel(Dialog)
        self.labelLogo.setGeometry(QtCore.QRect(10, 10, 91, 111))
        self.labelLogo.setMaximumSize(QtCore.QSize(145, 177))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("../../.designer/logo_ufpa_sem_fundo.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setObjectName("labelLogo")
        self.buttonOk = QtGui.QPushButton(Dialog)
        self.buttonOk.setGeometry(QtCore.QRect(380, 340, 93, 27))
        self.buttonOk.setObjectName("buttonOk")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonOk, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Sobre - SATEC", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Sobre SATEC", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Esse programa utilizou PyQt4 para o seu desenvolvimento e é totalmente open-source sem nenhum tipo de fim lucrativo.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />O Sistema de Aprendizagem de Telecomunicações visa ser um programa que ajude o aluno, sendo uma ferramenta de auxilio a aprendizagem. Com a exaplanação dos assuntos abordados em sala de aula de uma forma mais didática,clara e direta. Possuindo também video-aulas, exercícios e simulações sobre as mesmas. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Foi desenvolvido na Universidade Federal do Pará (UFPA), no laboratório de processamento de sinais (LaPS), com a coordenação do Prof. Dr. Francisco Müller. </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">Desenvolvedores: Andrey Silva</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">           Hugo Bragança</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">           Otávio Augusto</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">Contato: satec.ufpa@gmail.com</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOk.setText(QtGui.QApplication.translate("Dialog", "&OK", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

