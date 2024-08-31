

import src,login_page
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_sign_up(object):
    def message(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def show_login(self):
        self.window=login_page.QtWidgets.QDialog()
        self.ui=login_page.Ui_LOGIN()
        self.ui.setupUi(self.window)
        self.window.show()
    

    def message(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, sign_up):
        sign_up.setObjectName("sign_up")
        sign_up.resize(500, 591)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sign_up.sizePolicy().hasHeightForWidth())
        sign_up.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/SOURCE/SOURCE/SIGN-UP LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sign_up.setWindowIcon(icon)
        sign_up.setStyleSheet("QWidget#sign_up{\n"
                              "background-color: rgb(255, 255, 127);\n"
                              "\n"
                              "}")
        self.bg_tabWidget = QtWidgets.QTabWidget(sign_up)
        self.bg_tabWidget.setGeometry(QtCore.QRect(20, 140, 441, 391))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bg_tabWidget.sizePolicy().hasHeightForWidth())
        self.bg_tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bg_tabWidget.setFont(font)
        self.bg_tabWidget.setStyleSheet("QFrame#bg_frame{\n"
                                        "background-color: rgb(170, 255, 255);\n"
                                        "border-radius:35px;\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "    border-color: rgb(0, 0, 0);\n"
                                        "}")
        self.bg_tabWidget.setObjectName("bg_tabWidget")
        self.bg_tabWidgetPage1 = QtWidgets.QWidget()
        self.bg_tabWidgetPage1.setObjectName("bg_tabWidgetPage1")
        self.form_frame = QtWidgets.QFrame(self.bg_tabWidgetPage1)
        self.form_frame.setGeometry(QtCore.QRect(40, 30, 371, 51))
        self.form_frame.setStyleSheet("QFrame#form_frame{\n"
                                      "background-color: rgb(217, 255, 250);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-radius:15px;\n"
                                      "}")
        self.form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame.setObjectName("form_frame")
        self.faculty_username_logo = QtWidgets.QLabel(self.form_frame)
        self.faculty_username_logo.setGeometry(QtCore.QRect(10, 5, 41, 41))
        self.faculty_username_logo.setText("")
        self.faculty_username_logo.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/person icon.png"))
        self.faculty_username_logo.setScaledContents(True)
        self.faculty_username_logo.setObjectName("faculty_username_logo")
        self.faculty_username_txt = QtWidgets.QLineEdit(self.form_frame)
        self.faculty_username_txt.setGeometry(QtCore.QRect(70, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_username_txt.setFont(font)
        self.faculty_username_txt.setObjectName("faculty_username_txt")
        self.form_frame_2 = QtWidgets.QFrame(self.bg_tabWidgetPage1)
        self.form_frame_2.setGeometry(QtCore.QRect(40, 101, 371, 51))
        self.form_frame_2.setStyleSheet("QFrame#form_frame_2{\n"
                                        "background-color: rgb(217, 255, 250);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-radius:15px;\n"
                                        "}")
        self.form_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame_2.setObjectName("form_frame_2")
        self.faculty_phone_logo = QtWidgets.QLabel(self.form_frame_2)
        self.faculty_phone_logo.setGeometry(QtCore.QRect(10, 5, 41, 41))
        self.faculty_phone_logo.setText("")
        self.faculty_phone_logo.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/phone icon.png"))
        self.faculty_phone_logo.setScaledContents(True)
        self.faculty_phone_logo.setObjectName("faculty_phone_logo")
        self.faculty_phone_txt = QtWidgets.QLineEdit(self.form_frame_2)
        self.faculty_phone_txt.setGeometry(QtCore.QRect(70, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_phone_txt.setFont(font)
        self.faculty_phone_txt.setObjectName("faculty_phone_txt")
        self.form_frame_3 = QtWidgets.QFrame(self.bg_tabWidgetPage1)
        self.form_frame_3.setGeometry(QtCore.QRect(40, 172, 371, 51))
        self.form_frame_3.setStyleSheet("QFrame#form_frame_3{\n"
                                        "background-color: rgb(217, 255, 250);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-radius:15px;\n"
                                        "}")
        self.form_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame_3.setObjectName("form_frame_3")
        self.faculty_email_logo = QtWidgets.QLabel(self.form_frame_3)
        self.faculty_email_logo.setGeometry(QtCore.QRect(10, 5, 41, 41))
        self.faculty_email_logo.setText("")
        self.faculty_email_logo.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/email icon.png"))
        self.faculty_email_logo.setScaledContents(True)
        self.faculty_email_logo.setObjectName("faculty_email_logo")
        self.faculty_email_txt = QtWidgets.QLineEdit(self.form_frame_3)
        self.faculty_email_txt.setGeometry(QtCore.QRect(70, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_email_txt.setFont(font)
        self.faculty_email_txt.setObjectName("faculty_email_txt")
        self.form_frame_4 = QtWidgets.QFrame(self.bg_tabWidgetPage1)
        self.form_frame_4.setGeometry(QtCore.QRect(40, 243, 371, 51))
        self.form_frame_4.setStyleSheet("QFrame#form_frame_4{\n"
                                        "background-color: rgb(217, 255, 250);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-radius:15px;\n"
                                        "}")
        self.form_frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame_4.setObjectName("form_frame_4")
        self.faculty_password_logo = QtWidgets.QLabel(self.form_frame_4)
        self.faculty_password_logo.setGeometry(QtCore.QRect(10, 5, 41, 41))
        self.faculty_password_logo.setText("")
        self.faculty_password_logo.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/lock icon.png"))
        self.faculty_password_logo.setScaledContents(True)
        self.faculty_password_logo.setObjectName("faculty_password_logo")
        self.faculty_password_txt = QtWidgets.QLineEdit(self.form_frame_4)
        self.faculty_password_txt.setGeometry(QtCore.QRect(70, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_password_txt.setFont(font)
        self.faculty_password_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.faculty_password_txt.setObjectName("faculty_password_txt")
        self.faculty_register_btn = QtWidgets.QPushButton(
            self.bg_tabWidgetPage1)
        self.faculty_register_btn.setGeometry(QtCore.QRect(150, 310, 157, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_register_btn.setFont(font)
        self.faculty_register_btn.setStyleSheet("QPushButton#faculty_register_btn{\n"
                                                "background-color: rgb(170, 85, 127);\n"
                                                "border-style:solid;\n"
                                                "border-width:1px;\n"
                                                "border-radius:15px;\n"
                                                "    border-color: rgb(0, 0, 0);\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton#faculty_register_btn:hover{\n"
                                                "\n"
                                                "    background-color: rgb(170, 21, 150);\n"
                                                "}\n"
                                                "QPushButton#faculty_register_btn:pressed{\n"
                                                "background-color: rgb(0, 0, 127);\n"
                                                "}")
        self.faculty_register_btn.setObjectName("faculty_register_btn")
        self.faculty_register_btn.clicked.connect(self.facuity_reg)
        self.faculty_frame = QtWidgets.QFrame(self.bg_tabWidgetPage1)
        self.faculty_frame.setGeometry(QtCore.QRect(0, 0, 441, 371))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.faculty_frame.sizePolicy().hasHeightForWidth())
        self.faculty_frame.setSizePolicy(sizePolicy)
        self.faculty_frame.setStyleSheet("QFrame#faculty_frame{\n"
                                         "\n"
                                         "    background-color: rgb(170, 255, 255);\n"
                                         "}")
        self.faculty_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faculty_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faculty_frame.setObjectName("faculty_frame")
        self.faculty_frame.raise_()
        self.form_frame.raise_()
        self.form_frame_2.raise_()
        self.form_frame_3.raise_()
        self.form_frame_4.raise_()
        self.faculty_register_btn.raise_()
        self.bg_tabWidget.addTab(self.bg_tabWidgetPage1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.admin_frame = QtWidgets.QFrame(self.tab)
        self.admin_frame.setGeometry(QtCore.QRect(0, 0, 441, 371))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_frame.sizePolicy().hasHeightForWidth())
        self.admin_frame.setSizePolicy(sizePolicy)
        self.admin_frame.setStyleSheet("QFrame#admin_frame{\n"
                                       "\n"
                                       "    background-color: rgb(170, 255, 255);\n"
                                       "}")
        self.admin_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.admin_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_frame.setObjectName("admin_frame")
        self.form_frame_5 = QtWidgets.QFrame(self.admin_frame)
        self.form_frame_5.setGeometry(QtCore.QRect(40, 30, 371, 51))
        self.form_frame_5.setStyleSheet("QFrame#form_frame_5{\n"
                                        "background-color: rgb(217, 255, 250);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-radius:15px;\n"
                                        "}")
        self.form_frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame_5.setObjectName("form_frame_5")
        self.admin_username_logo = QtWidgets.QLabel(self.form_frame_5)
        self.admin_username_logo.setGeometry(QtCore.QRect(10, 5, 41, 41))
        self.admin_username_logo.setText("")
        self.admin_username_logo.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/person icon.png"))
        self.admin_username_logo.setScaledContents(True)
        self.admin_username_logo.setObjectName("admin_username_logo")
        self.admin_username_txt = QtWidgets.QLineEdit(self.form_frame_5)
        self.admin_username_txt.setGeometry(QtCore.QRect(70, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.admin_username_txt.setFont(font)
        self.admin_username_txt.setObjectName("admin_username_txt")
        self.form_frame_6 = QtWidgets.QFrame(self.admin_frame)
        self.form_frame_6.setGeometry(QtCore.QRect(40, 101, 371, 51))
        self.form_frame_6.setStyleSheet("QFrame#form_frame_6{\n"
                                        "background-color: rgb(217, 255, 250);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-radius:15px;\n"
                                        "}")
        self.form_frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame_6.setObjectName("form_frame_6")
        self.admin_phone_logo = QtWidgets.QLabel(self.form_frame_6)
        self.admin_phone_logo.setGeometry(QtCore.QRect(10, 5, 41, 41))
        self.admin_phone_logo.setText("")
        self.admin_phone_logo.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/phone icon.png"))
        self.admin_phone_logo.setScaledContents(True)
        self.admin_phone_logo.setObjectName("admin_phone_logo")
        self.admin_phone_txt = QtWidgets.QLineEdit(self.form_frame_6)
        self.admin_phone_txt.setGeometry(QtCore.QRect(70, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.admin_phone_txt.setFont(font)
        self.admin_phone_txt.setObjectName("admin_phone_txt")
        self.form_frame_7 = QtWidgets.QFrame(self.admin_frame)
        self.form_frame_7.setGeometry(QtCore.QRect(40, 172, 371, 51))
        self.form_frame_7.setStyleSheet("QFrame#form_frame_7{\n"
                                        "background-color: rgb(217, 255, 250);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-radius:15px;\n"
                                        "}")
        self.form_frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame_7.setObjectName("form_frame_7")
        self.admin_email_logo = QtWidgets.QLabel(self.form_frame_7)
        self.admin_email_logo.setGeometry(QtCore.QRect(10, 5, 41, 41))
        self.admin_email_logo.setText("")
        self.admin_email_logo.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/email icon.png"))
        self.admin_email_logo.setScaledContents(True)
        self.admin_email_logo.setObjectName("admin_email_logo")
        self.admin_email_txt = QtWidgets.QLineEdit(self.form_frame_7)
        self.admin_email_txt.setGeometry(QtCore.QRect(70, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.admin_email_txt.setFont(font)
        self.admin_email_txt.setObjectName("admin_email_txt")
        self.form_frame_8 = QtWidgets.QFrame(self.admin_frame)
        self.form_frame_8.setGeometry(QtCore.QRect(40, 243, 371, 51))
        self.form_frame_8.setStyleSheet("QFrame#form_frame_8{\n"
                                        "background-color: rgb(217, 255, 250);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-radius:15px;\n"
                                        "}")
        self.form_frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame_8.setObjectName("form_frame_8")
        self.admin_password_logo = QtWidgets.QLabel(self.form_frame_8)
        self.admin_password_logo.setGeometry(QtCore.QRect(10, 5, 41, 41))
        self.admin_password_logo.setText("")
        self.admin_password_logo.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/lock icon.png"))
        self.admin_password_logo.setScaledContents(True)
        self.admin_password_logo.setObjectName("admin_password_logo")
        self.admin_password_txt = QtWidgets.QLineEdit(self.form_frame_8)
        self.admin_password_txt.setGeometry(QtCore.QRect(70, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.admin_password_txt.setFont(font)
        self.admin_password_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_password_txt.setObjectName("admin_password_txt")
        self.admin_register_btn = QtWidgets.QPushButton(self.admin_frame)
        self.admin_register_btn.setGeometry(QtCore.QRect(150, 310, 157, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.admin_register_btn.setFont(font)
        self.admin_register_btn.setStyleSheet("\n"
                                              "\n"
                                              "QPushButton#admin_register_btn{\n"
                                              "background-color: rgb(170, 85, 127);\n"
                                              "border-style:solid;\n"
                                              "border-width:1px;\n"
                                              "border-radius:15px;\n"
                                              "    border-color: rgb(0, 0, 0);\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton#admin_register_btn:hover{\n"
                                              "\n"
                                              "    background-color: rgb(170, 21, 150);\n"
                                              "}\n"
                                              "QPushButton#admin_register_btn:pressed{\n"
                                              "background-color: rgb(0, 0, 127);\n"
                                              "}")
        self.admin_register_btn.setObjectName("admin_register_btn")
        self.admin_register_btn.clicked.connect(self.connect_db)
        self.bg_tabWidget.addTab(self.tab, "")
        self.BACK_LOGIN_BTN = QtWidgets.QCommandLinkButton(sign_up)
        self.BACK_LOGIN_BTN.setGeometry(QtCore.QRect(310, 540, 185, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BACK_LOGIN_BTN.setFont(font)
        self.BACK_LOGIN_BTN.setObjectName("BACK_LOGIN_BTN")
        self.BACK_LOGIN_BTN.clicked.connect(self.show_login)
        self.BACK_LOGIN_BTN.clicked.connect(sign_up.close)

        self.signup_label = QtWidgets.QLabel(sign_up)
        self.signup_label.setGeometry(QtCore.QRect(160, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet("QLabel#signup_label{\n"
                                        "border-style:groove;\n"
                                        "border-width:5px;\n"
                                        "    border-color: rgb(170, 170, 127);\n"
                                        "border-radius:15px;\n"
                                        "}")
        self.signup_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_label.setObjectName("signup_label")

        self.retranslateUi(sign_up)
        self.bg_tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(sign_up)

    def retranslateUi(self, sign_up):
        _translate = QtCore.QCoreApplication.translate
        sign_up.setWindowTitle(_translate("sign_up", "SIGN-UP"))
        self.faculty_username_txt.setPlaceholderText(
            _translate("sign_up", "   NAME"))
        self.faculty_phone_txt.setPlaceholderText(
            _translate("sign_up", "   PHONE NUMBER"))
        self.faculty_email_txt.setPlaceholderText(
            _translate("sign_up", "    E-MAIL"))
        self.faculty_password_txt.setPlaceholderText(
            _translate("sign_up", "    PASSWORD"))
        self.faculty_register_btn.setText(_translate("sign_up", "REGISTER"))
        self.bg_tabWidget.setTabText(self.bg_tabWidget.indexOf(
            self.bg_tabWidgetPage1), _translate("sign_up", "FACULTY"))
        self.admin_username_txt.setPlaceholderText(
            _translate("sign_up", "   NAME"))
        self.admin_phone_txt.setPlaceholderText(
            _translate("sign_up", "   PHONE NUMBER"))
        self.admin_email_txt.setPlaceholderText(
            _translate("sign_up", "    E-MAIL"))
        self.admin_password_txt.setPlaceholderText(
            _translate("sign_up", "    PASSWORD"))
        self.admin_register_btn.setText(_translate("sign_up", "REGISTER"))
        self.bg_tabWidget.setTabText(self.bg_tabWidget.indexOf(
            self.tab), _translate("sign_up", "ADMIN"))
        self.BACK_LOGIN_BTN.setText(_translate("sign_up", "Back To Login"))
        self.signup_label.setText(_translate("sign_up", "SIGN-UP"))

    def connect_db(self):
        try:
            name = self.admin_username_txt.text()
            passwd = self.admin_password_txt.text()
            email = self.admin_email_txt.text()
            phone_num = self.admin_phone_txt.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )
            self.faculty_email_txt.setText("hello")
            print("hi")
            mycursor = mydb.cursor()
            query = ("SELECT * FROM signup_admin_info where name ='"+name+"'and password ='"+passwd+"'")
            mycursor.execute(query)
            result = mycursor.fetchone()
            self.admin_username_txt.setText("")
            self.admin_password_txt.setText("")
            self.admin_email_txt.setText("")
            self.admin_phone_txt.setText("")

            if result:

                self.message("WARNNING!!","YOU ARE ARlREADY REGISTERED!!")

            else:
                mycursor.execute("insert into signup_admin_info values('" +name+"','"+passwd+"','"+email+"','"+phone_num+"')")
                mydb.commit()
                self.message("CONGRATULATION!!","YOU ARE NOW REGISTERED!!")
        except mc.Error as e:
            print("error has occured")
    
    def facuity_reg(self):
        try:
            name = self.faculty_username_txt.text()
            passwd = self.faculty_password_txt.text()
            email = self.faculty_email_txt.text()
            phone_num = self.faculty_phone_txt.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )
            print("hi")
            mycursor = mydb.cursor()
            query = ("SELECT * FROM faculty_signup_info where name ='"+name+"'and password ='"+passwd+"'")
            mycursor.execute(query)
            result = mycursor.fetchone()
            self.faculty_username_txt.setText("")
            self.faculty_password_txt.setText("")
            self.faculty_email_txt.setText("")
            self.faculty_phone_txt.setText("")

            if result:
                
                self.message("WARNNING!!","YOU ARE ARlREADY REGISTERED!!")
                print("alrady regustered")

            else:
                mycursor.execute("insert into faculty_signup_info values('" +name+"','"+passwd+"','"+email+"','"+phone_num+"')")
                mydb.commit()
                self.message("WARNNING!!","YOU ARE NOW REGISTERED!!")
                
        except mc.Error as e:
            print("error has occured")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sign_up = QtWidgets.QWidget()
    ui = Ui_sign_up()
    ui.setupUi(sign_up)
    sign_up.show()
    sys.exit(app.exec_())
