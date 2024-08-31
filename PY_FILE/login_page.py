

import src,details_page
import admin_dashboard_new
import sign_Up_page,mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LOGIN(object):
    def openwindow(self):
        self.window = sign_Up_page.QtWidgets.QMainWindow()
        self.ui = sign_Up_page.Ui_sign_up()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def openadmin_window(self):
        self.window = admin_dashboard_new.QtWidgets.QMainWindow()
        self.ui = admin_dashboard_new.Ui_admin_dashboard()
        self.ui.setupUi(self.window)
        self.window.show()
        


    def opendetails_window(self):
        self.window=details_page.QtWidgets.QMainWindow()
        self.ui=details_page.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def message(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, LOGIN):
        LOGIN.setObjectName("LOGIN")
        LOGIN.resize(500, 591)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LOGIN.sizePolicy().hasHeightForWidth())
        LOGIN.setSizePolicy(sizePolicy)
        LOGIN.setMinimumSize(QtCore.QSize(500, 591))
        LOGIN.setMaximumSize(QtCore.QSize(500, 591))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        LOGIN.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/SOURCE/SOURCE/login logo.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LOGIN.setWindowIcon(icon)
        LOGIN.setStyleSheet("QDialog#LOGIN{\n"
                            "background-color: rgb(15, 67, 116);\n"
                            "}")
        self.tab_login = QtWidgets.QTabWidget(LOGIN)
        self.tab_login.setGeometry(QtCore.QRect(40, 50, 431, 500))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tab_login.sizePolicy().hasHeightForWidth())
        self.tab_login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tab_login.setFont(font)
        self.tab_login.setStyleSheet("")
        self.tab_login.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_login.setDocumentMode(False)
        self.tab_login.setObjectName("tab_login")
        self.tab_faculty = QtWidgets.QWidget()
        self.tab_faculty.setObjectName("tab_faculty")
        self.frame_faculty = QtWidgets.QFrame(self.tab_faculty)
        self.frame_faculty.setGeometry(QtCore.QRect(-90, 0, 521, 550))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_faculty.sizePolicy().hasHeightForWidth())
        self.frame_faculty.setSizePolicy(sizePolicy)
        self.frame_faculty.setStyleSheet("QFrame#frame_faculty{\n"
                                         "    background-color: rgb(220, 220, 220);\n"
                                         "}")
        self.frame_faculty.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_faculty.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_faculty.setObjectName("frame_faculty")
        self.frame_login_faculty = QtWidgets.QFrame(self.frame_faculty)
        self.frame_login_faculty.setGeometry(QtCore.QRect(90, 10, 421, 451))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_login_faculty.sizePolicy().hasHeightForWidth())
        self.frame_login_faculty.setSizePolicy(sizePolicy)
        self.frame_login_faculty.setStyleSheet("QFrame#frame_login_faculty{\n"
                                               "background-color: rgb(231, 231, 231);\n"
                                               "border-color: rgb(0, 0, 0);\n"
                                               "border-style: double;\n"
                                               "border-width: 5px;\n"
                                               "border-radius:5px;\n"
                                               "}")
        self.frame_login_faculty.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login_faculty.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login_faculty.setObjectName("frame_login_faculty")
        self.faculty_login_txt = QtWidgets.QLabel(self.frame_login_faculty)
        self.faculty_login_txt.setGeometry(QtCore.QRect(40, 20, 341, 71))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.faculty_login_txt.sizePolicy().hasHeightForWidth())
        self.faculty_login_txt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_login_txt.setFont(font)
        self.faculty_login_txt.setStyleSheet("QLabel#faculty_login_txt{\n"
                                             "border-width:5px;\n"
                                             "border-style:solid;\n"
                                             "border-radius:30px;\n"
                                             "    \n"
                                             "background-color: rgb(255, 185, 127);\n"
                                             "}")
        self.faculty_login_txt.setScaledContents(True)
        self.faculty_login_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.faculty_login_txt.setObjectName("faculty_login_txt")
        self.faculty_username_txt = QtWidgets.QLabel(self.frame_login_faculty)
        self.faculty_username_txt.setGeometry(QtCore.QRect(10, 120, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.faculty_username_txt.sizePolicy().hasHeightForWidth())
        self.faculty_username_txt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_username_txt.setFont(font)
        self.faculty_username_txt.setStyleSheet("QLabel#faculty_username_txt{\n"
                                                "    color: rgb(85, 0, 0);\n"
                                                "\n"
                                                "}")
        self.faculty_username_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.faculty_username_txt.setObjectName("faculty_username_txt")
        self.faculty_pass_txt = QtWidgets.QLabel(self.frame_login_faculty)
        self.faculty_pass_txt.setGeometry(QtCore.QRect(10, 240, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.faculty_pass_txt.sizePolicy().hasHeightForWidth())
        self.faculty_pass_txt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_pass_txt.setFont(font)
        self.faculty_pass_txt.setStyleSheet("QLabel#faculty_pass_txt{\n"
                                            "    color: rgb(85, 0, 0);\n"
                                            "\n"
                                            "}")
        self.faculty_pass_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.faculty_pass_txt.setObjectName("faculty_pass_txt")
        self.faculty_login_btn = QtWidgets.QPushButton(
            self.frame_login_faculty)
        self.faculty_login_btn.setGeometry(QtCore.QRect(40, 370, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.faculty_login_btn.sizePolicy().hasHeightForWidth())
        self.faculty_login_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_login_btn.setFont(font)
        self.faculty_login_btn.setStyleSheet("QPushButton#faculty_login_btn{\n"
                                             "background-color: rgb(26, 29, 255);\n"
                                             "border-width: 2px;\n"
                                             "border-style: outset;\n"
                                             "border-color: rgb(0, 0, 0);\n"
                                             "    color: rgb(255, 255, 0);\n"
                                             "}\n"
                                             "QPushButton#faculty_login_btn:hover{\n"
                                             "background-color: rgb(85, 170, 0);\n"
                                             "}\n"
                                             "QPushButton#faculty_login_btn:pressed{\n"
                                             "background-color: rgb(255, 170, 0);\n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "}")
        self.faculty_login_btn.setObjectName("faculty_login_btn")
        self.faculty_login_btn.clicked.connect(self.faculty_login)
        self.faculty_login_btn.clicked.connect(LOGIN.close)
        
        self.faculty_sign_up_btn = QtWidgets.QPushButton(
            self.frame_login_faculty)
        self.faculty_sign_up_btn.setGeometry(QtCore.QRect(260, 370, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.faculty_sign_up_btn.sizePolicy().hasHeightForWidth())
        self.faculty_sign_up_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_sign_up_btn.clicked.connect(self.openwindow)
        self.faculty_sign_up_btn.clicked.connect(LOGIN.close)
        
        self.faculty_sign_up_btn.setFont(font)
        self.faculty_sign_up_btn.setStyleSheet("QPushButton#faculty_sign_up_btn{\n"
                                               "background-color: rgb(26, 29, 255);\n"
                                               "border-width: 2px;\n"
                                               "border-style: outset;\n"
                                               "    border-color: rgb(0, 0, 0);\n"
                                               "    color: rgb(255, 255, 0);\n"
                                               "}\n"
                                               "QPushButton#faculty_sign_up_btn:hover{\n"
                                               "\n"
                                               "    background-color: rgb(0, 170, 255);\n"
                                               "}\n"
                                               "QPushButton#faculty_sign_up_btn:pressed{\n"
                                               "background-color: rgb(255, 170, 0);\n"
                                               "    color: rgb(0, 0, 0);\n"
                                               "}")
        self.faculty_sign_up_btn.setObjectName("faculty_sign_up_btn")
        self.faculty_username_inp = QtWidgets.QLineEdit(
            self.frame_login_faculty)
        self.faculty_username_inp.setGeometry(QtCore.QRect(150, 120, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.faculty_username_inp.sizePolicy().hasHeightForWidth())
        self.faculty_username_inp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_username_inp.setFont(font)
        self.faculty_username_inp.setStyleSheet("QLineEdit#faculty_username_inp{\n"
                                                "border-style: outset;\n"
                                                "border-width: 2px;\n"
                                                "border-color:rgb(170, 170, 255);\n"
                                                "    color: rgb(0, 170, 0);\n"
                                                "\n"
                                                "}")
        self.faculty_username_inp.setObjectName("faculty_username_inp")
        self.faculty_pass_inp = QtWidgets.QLineEdit(self.frame_login_faculty)
        self.faculty_pass_inp.setGeometry(QtCore.QRect(150, 240, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.faculty_pass_inp.sizePolicy().hasHeightForWidth())
        self.faculty_pass_inp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.faculty_pass_inp.setFont(font)
        self.faculty_pass_inp.setStyleSheet("QLineEdit#faculty_pass_inp{\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-color:rgb(170, 170, 255);\n"
                                            "    color: rgb(0, 170, 0);\n"
                                            "\n"
                                            "}")
        self.faculty_pass_inp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.faculty_pass_inp.setObjectName("faculty_pass_inp")
        self.faculty_img_label = QtWidgets.QLabel(self.frame_login_faculty)
        self.faculty_img_label.setGeometry(QtCore.QRect(60, 30, 61, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.faculty_img_label.sizePolicy().hasHeightForWidth())
        self.faculty_img_label.setSizePolicy(sizePolicy)
        self.faculty_img_label.setText("")
        self.faculty_img_label.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/faculty logo.png"))
        self.faculty_img_label.setScaledContents(True)
        self.faculty_img_label.setObjectName("faculty_img_label")
        self.label_login = QtWidgets.QLabel(self.frame_login_faculty)
        self.label_login.setGeometry(QtCore.QRect(40, 340, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_login.sizePolicy().hasHeightForWidth())
        self.label_login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("QLabel#label_login{\n"
                                       "\n"
                                       "\n"
                                       "}")
        self.label_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login.setObjectName("label_login")
        self.label_signup = QtWidgets.QLabel(self.frame_login_faculty)
        self.label_signup.setGeometry(QtCore.QRect(250, 340, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_signup.sizePolicy().hasHeightForWidth())
        self.label_signup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_signup.setFont(font)
        self.label_signup.setStyleSheet("QLabel#label_login{\n"
                                        "\n"
                                        "\n"
                                        "}")
        self.label_signup.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signup.setObjectName("label_signup")
        self.tab_login.addTab(self.tab_faculty, "")
        self.tab_admin = QtWidgets.QWidget()
        self.tab_admin.setObjectName("tab_admin")
        self.frame_admin = QtWidgets.QFrame(self.tab_admin)
        self.frame_admin.setGeometry(QtCore.QRect(0, 0, 521, 550))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_admin.sizePolicy().hasHeightForWidth())
        self.frame_admin.setSizePolicy(sizePolicy)
        self.frame_admin.setStyleSheet("QFrame#frame_admin{\n"
                                       "    background-color: rgb(220, 220, 220);\n"
                                       "}")
        self.frame_admin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_admin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_admin.setObjectName("frame_admin")
        self.frame_login_admin = QtWidgets.QFrame(self.frame_admin)
        self.frame_login_admin.setGeometry(QtCore.QRect(0, 10, 421, 451))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_login_admin.sizePolicy().hasHeightForWidth())
        self.frame_login_admin.setSizePolicy(sizePolicy)
        self.frame_login_admin.setStyleSheet("QFrame#frame_login_admin{\n"
                                             "background-color: rgb(231, 231, 231);\n"
                                             "border-color: rgb(0, 0, 0);\n"
                                             "border-style: double;\n"
                                             "border-width: 5px;\n"
                                             "}")
        self.frame_login_admin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login_admin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login_admin.setObjectName("frame_login_admin")
        self.admin_username_txt = QtWidgets.QLabel(self.frame_login_admin)
        self.admin_username_txt.setGeometry(QtCore.QRect(10, 120, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_username_txt.sizePolicy().hasHeightForWidth())
        self.admin_username_txt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.admin_username_txt.setFont(font)
        self.admin_username_txt.setStyleSheet("QLabel#admin_username_txt{\n"
                                              "    color: rgb(85, 0, 0);\n"
                                              "\n"
                                              "}")
        self.admin_username_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.admin_username_txt.setObjectName("admin_username_txt")
        self.admin_pass_txt = QtWidgets.QLabel(self.frame_login_admin)
        self.admin_pass_txt.setGeometry(QtCore.QRect(10, 240, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_pass_txt.sizePolicy().hasHeightForWidth())
        self.admin_pass_txt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.admin_pass_txt.setFont(font)
        self.admin_pass_txt.setStyleSheet("QLabel#admin_pass_txt{\n"
                                          "    color: rgb(85, 0, 0);\n"
                                          "\n"
                                          "}")
        self.admin_pass_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.admin_pass_txt.setObjectName("admin_pass_txt")
        self.admin_login_btn = QtWidgets.QPushButton(self.frame_login_admin)
        self.admin_login_btn.setGeometry(QtCore.QRect(40, 370, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_login_btn.sizePolicy().hasHeightForWidth())
        self.admin_login_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.admin_login_btn.setFont(font)
        self.admin_login_btn.setStyleSheet("\n"
                                           "QPushButton#admin_login_btn{\n"
                                           "background-color: rgb(26, 29, 255);\n"
                                           "border-width: 2px;\n"
                                           "border-style: outset;\n"
                                           "border-color: rgb(0, 0, 0);\n"
                                           "    color: rgb(255, 255, 0);\n"
                                           "}\n"
                                           "QPushButton#admin_login_btn:hover{\n"
                                           "background-color: rgb(85, 170, 0);\n"
                                           "}\n"
                                           "QPushButton#admin_login_btn:pressed{\n"
                                           "background-color: rgb(255, 170, 0);\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}")
        self.admin_login_btn.setObjectName("admin_login_btn")
        self.admin_login_btn.clicked.connect(self.admin_login)
        self.admin_login_btn.clicked.connect(LOGIN.close)
        self.admin_sign_up_btn = QtWidgets.QPushButton(self.frame_login_admin)
        self.admin_sign_up_btn.setGeometry(QtCore.QRect(260, 370, 111, 31))
        self.admin_sign_up_btn.clicked.connect(self.openwindow)
        self.admin_sign_up_btn.clicked.connect(LOGIN.close)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_sign_up_btn.sizePolicy().hasHeightForWidth())
        self.admin_sign_up_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.admin_sign_up_btn.setFont(font)
        self.admin_sign_up_btn.setStyleSheet("\n"
                                             "\n"
                                             "QPushButton#admin_sign_up_btn{\n"
                                             "background-color: rgb(26, 29, 255);\n"
                                             "border-width: 2px;\n"
                                             "border-style: outset;\n"
                                             "    border-color: rgb(0, 0, 0);\n"
                                             "    color: rgb(255, 255, 0);\n"
                                             "}\n"
                                             "QPushButton#admin_sign_up_btn:hover{\n"
                                             "\n"
                                             "    background-color: rgb(0, 170, 255);\n"
                                             "}\n"
                                             "QPushButton#admin_sign_up_btn:pressed{\n"
                                             "background-color: rgb(255, 170, 0);\n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "}")
        self.admin_sign_up_btn.setObjectName("admin_sign_up_btn")
        self.admin_username_inp = QtWidgets.QLineEdit(self.frame_login_admin)
        self.admin_username_inp.setGeometry(QtCore.QRect(150, 120, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_username_inp.sizePolicy().hasHeightForWidth())
        self.admin_username_inp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.admin_username_inp.setFont(font)
        self.admin_username_inp.setStyleSheet("QLineEdit#admin_username_inp{\n"
                                              "border-style: outset;\n"
                                              "border-width: 2px;\n"
                                              "border-color:rgb(170, 170, 255);\n"
                                              "    color: rgb(0, 170, 0);\n"
                                              "\n"
                                              "}")
        self.admin_username_inp.setText("")
        self.admin_username_inp.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.admin_username_inp.setObjectName("admin_username_inp")
        self.admin_pass_inp = QtWidgets.QLineEdit(self.frame_login_admin)
        self.admin_pass_inp.setGeometry(QtCore.QRect(150, 240, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_pass_inp.sizePolicy().hasHeightForWidth())
        self.admin_pass_inp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.admin_pass_inp.setFont(font)
        self.admin_pass_inp.setStyleSheet("QLineEdit#admin_pass_inp{\n"
                                          "border-style: outset;\n"
                                          "border-width: 2px;\n"
                                          "border-color:rgb(170, 170, 255);\n"
                                          "    color: rgb(0, 170, 0);\n"
                                          "\n"
                                          "}")
        self.admin_pass_inp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_pass_inp.setObjectName("admin_pass_inp")
        self.admin_login_txt = QtWidgets.QLabel(self.frame_login_admin)
        self.admin_login_txt.setGeometry(QtCore.QRect(40, 20, 341, 71))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_login_txt.sizePolicy().hasHeightForWidth())
        self.admin_login_txt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.admin_login_txt.setFont(font)
        self.admin_login_txt.setStyleSheet("QLabel#admin_login_txt{\n"
                                           "border-width:5px;\n"
                                           "border-style:solid;\n"
                                           "border-radius:30px;\n"
                                           "    \n"
                                           "background-color: rgb(255, 185, 127);\n"
                                           "}")
        self.admin_login_txt.setScaledContents(True)
        self.admin_login_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.admin_login_txt.setObjectName("admin_login_txt")
        self.admin_img_label = QtWidgets.QLabel(self.frame_login_admin)
        self.admin_img_label.setGeometry(QtCore.QRect(60, 30, 61, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_img_label.sizePolicy().hasHeightForWidth())
        self.admin_img_label.setSizePolicy(sizePolicy)
        self.admin_img_label.setText("")
        self.admin_img_label.setPixmap(
            QtGui.QPixmap(":/SOURCE/SOURCE/admin logo.png"))
        self.admin_img_label.setScaledContents(True)
        self.admin_img_label.setObjectName("admin_img_label")
        self.label_login_2 = QtWidgets.QLabel(self.frame_login_admin)
        self.label_login_2.setGeometry(QtCore.QRect(40, 340, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_login_2.sizePolicy().hasHeightForWidth())
        self.label_login_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_login_2.setFont(font)
        self.label_login_2.setStyleSheet("QLabel#label_login{\n"
                                         "\n"
                                         "\n"
                                         "}")
        self.label_login_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login_2.setObjectName("label_login_2")
        self.label_signup_2 = QtWidgets.QLabel(self.tab_admin)
        self.label_signup_2.setGeometry(QtCore.QRect(250, 350, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_signup_2.sizePolicy().hasHeightForWidth())
        self.label_signup_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_signup_2.setFont(font)
        self.label_signup_2.setStyleSheet("QLabel#label_login{\n"
                                          "\n"
                                          "\n"
                                          "}")
        self.label_signup_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signup_2.setObjectName("label_signup_2")
        self.tab_login.addTab(self.tab_admin, "")

        self.retranslateUi(LOGIN)
        self.tab_login.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(LOGIN)

    def retranslateUi(self, LOGIN):
        _translate = QtCore.QCoreApplication.translate
        LOGIN.setWindowTitle(_translate("LOGIN", "LOGIN"))
        self.faculty_login_txt.setText(
            _translate("LOGIN", "       FACULTY LOGIN"))
        self.faculty_username_txt.setText(_translate("LOGIN", "USERNAME:"))
        self.faculty_pass_txt.setText(_translate("LOGIN", "PASSWORD:"))
        self.faculty_login_btn.setText(_translate("LOGIN", "LOGIN"))
        self.faculty_sign_up_btn.setText(_translate("LOGIN", "SIGN UP"))
        self.faculty_username_inp.setPlaceholderText(
            _translate("LOGIN", "Enter Username here"))
        self.faculty_pass_inp.setPlaceholderText(
            _translate("LOGIN", "Enter Password here"))
        self.label_login.setText(_translate("LOGIN", "Already a user?"))
        self.label_signup.setText(_translate("LOGIN", "Create New Account"))
        self.tab_login.setTabText(self.tab_login.indexOf(
            self.tab_faculty), _translate("LOGIN", "FACULTY"))
        self.admin_username_txt.setText(_translate("LOGIN", "USERNAME:"))
        self.admin_pass_txt.setText(_translate("LOGIN", "PASSWORD:"))
        self.admin_login_btn.setText(_translate("LOGIN", "LOGIN"))
        self.admin_sign_up_btn.setText(_translate("LOGIN", "SIGN UP"))
        self.admin_username_inp.setPlaceholderText(
            _translate("LOGIN", "Enter Username here"))
        self.admin_pass_inp.setPlaceholderText(
            _translate("LOGIN", "Enter Password here"))
        self.admin_login_txt.setText(_translate("LOGIN", "      ADMIN LOGIN"))
        self.label_login_2.setText(_translate("LOGIN", "Already a user?"))
        self.label_signup_2.setText(_translate("LOGIN", "Create New Account"))
        self.tab_login.setTabText(self.tab_login.indexOf(
            self.tab_admin), _translate("LOGIN", "ADMIN"))
    
    def faculty_login(self):
        try:
            name=self.faculty_username_inp.text()
            passwd=self.faculty_pass_inp.text()
            mydb=mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )
            mycursor=mydb.cursor()
            query=("SELECT * FROM faculty_signup_info where name ='"+name+"'and password ='"+passwd+"'")
            mycursor.execute(query)
            result= mycursor.fetchone()
            self.faculty_username_inp.setText("")
            self.faculty_pass_inp.setText("")
            if result:
                
                self.opendetails_window()
                print("logined")

            else:
                self.message("ERROR!!","PLEASE ENTER CORRECT USERNAME OR PASSWORD")
                print('incorrect')
        except mc.Error as e:
            print("error has occured")

    def admin_login(self):
        try:
            name=self.admin_username_inp.text()
            passwd=self.admin_pass_inp.text()
            mydb=mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )
            mycursor=mydb.cursor()
            query=("SELECT * FROM signup_admin_info where name ='"+name+"'and password ='"+passwd+"'")
            mycursor.execute(query)
            result= mycursor.fetchone()
            self.admin_username_inp.setText("")
            self.admin_pass_inp.setText("")
            if result:
                
                self.openadmin_window()
                print("logined")

            else:
                self.message("ERROR!!","PLEASE ENTER CORRECT USERNAME OR PASSWORD")
                print('incorrect')
        except mc.Error as e:
            print("error has occured")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGIN = QtWidgets.QDialog()
    ui = Ui_LOGIN()
    ui.setupUi(LOGIN)
    LOGIN.show()
    sys.exit(app.exec_())
