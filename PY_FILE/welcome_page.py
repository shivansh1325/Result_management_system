

import src,login_page
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(1000, 650)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)
        window.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        window.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/SOURCE/SOURCE/rms logo new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        window.setAutoFillBackground(False)
        window.setStyleSheet("background-color: rgb(154, 133, 200);")
        self.mgm_text = QtWidgets.QLabel(window)
        self.mgm_text.setGeometry(QtCore.QRect(30, 10, 941, 71))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mgm_text.sizePolicy().hasHeightForWidth())
        self.mgm_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner Semibold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.mgm_text.setFont(font)
        self.mgm_text.setStyleSheet("QLabel#mgm_text{\n"
                                    "color:rgb(255, 224, 102);\n"
                                    "    \n"
                                    "    background-color: rgb(255, 69, 56);\n"
                                    "    background-color: rgb(251, 124, 255);\n"
                                    "    background-color: rgb(223, 58, 255);\n"
                                    "    background-color: rgb(255, 0, 4);\n"
                                    "border-style:groove;\n"
                                    "border-width:4px;\n"
                                    "    border-color: rgb(255, 170, 0);\n"
                                    "\n"
                                    "}")
        self.mgm_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mgm_text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mgm_text.setLineWidth(3)
        self.mgm_text.setMidLineWidth(0)
        self.mgm_text.setTextFormat(QtCore.Qt.PlainText)
        self.mgm_text.setAlignment(QtCore.Qt.AlignCenter)
        self.mgm_text.setObjectName("mgm_text")
        self.btn_login = QtWidgets.QPushButton(window)
        self.btn_login.setGeometry(QtCore.QRect(60, 550, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton#btn_login{\n"
                                     "    \n"
                                     "    background-color: rgb(132, 255, 0);\n"
                                     "    border-color: rgb(0, 0, 0);\n"
                                     "border-radius:7px;\n"
                                     "border-width:4px;\n"
                                     "border-style:solid;\n"
                                     "\n"
                                     "}\n"
                                     "QPushButton#btn_login:hover{\n"
                                     "\n"
                                     "    background-color: rgb(255, 255, 0);\n"
                                     "}\n"
                                     "QPushButton#btn_login:pressed{\n"
                                     "\n"
                                     "    background-color: rgb(255, 85, 0);\n"
                                     "}\n"
                                     "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "../../Documents/Result_management/src/image/login logo.jpg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_login.setIcon(icon1)
        self.btn_login.setIconSize(QtCore.QSize(18, 18))
        self.btn_login.setObjectName("btn_login")
        self.btn_exit = QtWidgets.QPushButton(window)
        self.btn_exit.setGeometry(QtCore.QRect(830, 550, 121, 41))
        self.btn_login.clicked.connect(self.show_login)
        self.btn_login.clicked.connect(window.close)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setMouseTracking(True)
        self.btn_exit.setStyleSheet("QPushButton#btn_exit{\n"
                                    "background-color: rgb(132, 255, 0);\n"
                                    "    border-color: rgb(0, 0, 0);\n"
                                    "border-radius:7px;\n"
                                    "border-width:4px;\n"
                                    "border-style:solid;\n"
                                    "}\n"
                                    "QPushButton#btn_exit:hover{\n"
                                    "\n"
                                    "    background-color: rgb(255, 255, 0);\n"
                                    "}\n"
                                    "QPushButton#btn_exit:pressed{\n"
                                    "\n"
                                    "    background-color: rgb(255, 85, 0);\n"
                                    "}\n"
                                    "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "../../Documents/Result_management/src/image/cross.png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon2)
        self.btn_exit.setIconSize(QtCore.QSize(18, 18))
        self.btn_exit.setDefault(False)
        self.btn_exit.setFlat(False)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.clicked.connect(window.close)
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(80, 100, 841, 391))
        self.label.setStyleSheet("QLabel#label{\n"
                                 "border-style:groove;\n"
                                 "border-width:6px;\n"
                                 "    border-color: rgb(255, 0, 127);\n"
                                 "\n"
                                 "}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/SOURCE/SOURCE/Rms edited.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def show_login(self):
        self.window=login_page.QtWidgets.QDialog()
        self.ui=login_page.Ui_LOGIN()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Result Management system"))
        self.mgm_text.setText(_translate(
            "window", "Desktop Application"))
        self.btn_login.setText(_translate("window", " LOGIN"))
        self.btn_exit.setText(_translate("window", " EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
