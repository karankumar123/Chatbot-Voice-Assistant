# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUi4.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisUi(object):
    def setupUi(self, jarvisUi):
        jarvisUi.setObjectName("jarvisUi")
        jarvisUi.resize(1588, 966)
        self.centralwidget = QtWidgets.QWidget(jarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.Bg_1 = QtWidgets.QLabel(self.centralwidget)
        self.Bg_1.setGeometry(QtCore.QRect(-20, -50, 1611, 1021))
        self.Bg_1.setText("")
        self.Bg_1.setPixmap(QtGui.QPixmap("jarvis Gui Materail/B.G/Black_Template.jpg"))
        self.Bg_1.setScaledContents(True)
        self.Bg_1.setObjectName("Bg_1")
        self.Bg_2 = QtWidgets.QLabel(self.centralwidget)
        self.Bg_2.setGeometry(QtCore.QRect(10, 10, 611, 431))
        self.Bg_2.setStyleSheet("\n"
"background-color: rgb(0, 255, 255);")
        self.Bg_2.setText("")
        self.Bg_2.setObjectName("Bg_2")
        self.Bg_3 = QtWidgets.QLabel(self.centralwidget)
        self.Bg_3.setGeometry(QtCore.QRect(630, 10, 601, 431))
        self.Bg_3.setStyleSheet("\n"
"background-color: rgb(0, 255, 255);")
        self.Bg_3.setText("")
        self.Bg_3.setObjectName("Bg_3")
        self.Gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_1.setGeometry(QtCore.QRect(30, 20, 571, 411))
        self.Gif_1.setText("")
        self.Gif_1.setPixmap(QtGui.QPixmap("jarvis Gui Materail/B.G/Iron_Template_1.gif"))
        self.Gif_1.setScaledContents(True)
        self.Gif_1.setObjectName("Gif_1")
        self.Gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_2.setGeometry(QtCore.QRect(650, 20, 561, 411))
        self.Gif_2.setText("")
        self.Gif_2.setPixmap(QtGui.QPixmap("jarvis Gui Materail/ExtraGui/live.gif"))
        self.Gif_2.setScaledContents(True)
        self.Gif_2.setObjectName("Gif_2")
        self.Gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_3.setGeometry(QtCore.QRect(-200, 300, 841, 661))
        self.Gif_3.setText("")
        self.Gif_3.setPixmap(QtGui.QPixmap("jarvis Gui Materail/VoiceReg/__1.gif"))
        self.Gif_3.setScaledContents(True)
        self.Gif_3.setObjectName("Gif_3")
        self.text_time = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_time.setGeometry(QtCore.QRect(1250, 330, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.text_time.setFont(font)
        self.text_time.setStyleSheet("background-color: transparent;\n"
"font: 18pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.text_time.setObjectName("text_time")
        self.text_date = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_date.setGeometry(QtCore.QRect(1250, 390, 311, 51))
        self.text_date.setStyleSheet("background-color: Transparent;\n"
"font: 18pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.text_date.setObjectName("text_date")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 890, 131, 41))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 22pt \"Courier New\";\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 890, 111, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"font: 22pt \"Courier New\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(500, 530, 681, 321))
        self.textBrowser.setStyleSheet("background-color: transparent;\n"
"font: 18pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.Bg_4 = QtWidgets.QLabel(self.centralwidget)
        self.Bg_4.setGeometry(QtCore.QRect(1240, 10, 321, 301))
        self.Bg_4.setStyleSheet("\n"
"background-color: rgb(0, 255, 255);")
        self.Bg_4.setText("")
        self.Bg_4.setObjectName("Bg_4")
        self.Gif_4 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_4.setGeometry(QtCore.QRect(1250, 20, 291, 281))
        self.Gif_4.setText("")
        self.Gif_4.setPixmap(QtGui.QPixmap("jarvis Gui Materail/ExtraGui/Earth.gif"))
        self.Gif_4.setScaledContents(True)
        self.Gif_4.setObjectName("Gif_4")
        self.Gif_5 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_5.setGeometry(QtCore.QRect(1210, 530, 361, 321))
        self.Gif_5.setText("")
        self.Gif_5.setPixmap(QtGui.QPixmap("jarvis Gui Materail/ExtraGui/B.G_Template_1.gif"))
        self.Gif_5.setScaledContents(True)
        self.Gif_5.setObjectName("Gif_5")
        self.Bg_1.raise_()
        self.Gif_3.raise_()
        self.Bg_2.raise_()
        self.Bg_3.raise_()
        self.Gif_1.raise_()
        self.Gif_2.raise_()
        self.text_time.raise_()
        self.text_date.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.textBrowser.raise_()
        self.Bg_4.raise_()
        self.Gif_4.raise_()
        self.Gif_5.raise_()
        jarvisUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisUi)
        QtCore.QMetaObject.connectSlotsByName(jarvisUi)

    def retranslateUi(self, jarvisUi):
        _translate = QtCore.QCoreApplication.translate
        jarvisUi.setWindowTitle(_translate("jarvisUi", "MainWindow"))
        self.text_time.setHtml(_translate("jarvisUi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nirmala UI\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.text_date.setHtml(_translate("jarvisUi", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nirmala UI\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.pushButton.setText(_translate("jarvisUi", "Start"))
        self.pushButton_2.setText(_translate("jarvisUi", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisUi = QtWidgets.QMainWindow()
    ui = Ui_jarvisUi()
    ui.setupUi(jarvisUi)
    jarvisUi.show()
    sys.exit(app.exec_())
