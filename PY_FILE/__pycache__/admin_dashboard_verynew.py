

import source_file3,details_page
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import mysql.connector as mc


class Ui_admin_dashboard(object):
    def message(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def setupUi(self, admin_dashboard):
        admin_dashboard.setObjectName("admin_dashboard")
        admin_dashboard.resize(1080, 720)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            admin_dashboard.sizePolicy().hasHeightForWidth())
        admin_dashboard.setSizePolicy(sizePolicy)
        admin_dashboard.setMinimumSize(QtCore.QSize(1080, 720))
        admin_dashboard.setMaximumSize(QtCore.QSize(1080, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/source/ADMIN_LOGO.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_dashboard.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(admin_dashboard)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_frame = QtWidgets.QFrame(self.centralwidget)
        self.bg_frame.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bg_frame.sizePolicy().hasHeightForWidth())
        self.bg_frame.setSizePolicy(sizePolicy)
        self.bg_frame.setStyleSheet("QFrame#bg_frame{\n"
                                    "    background-color: rgb(25, 25, 25);\n"
                                    "\n"
                                    "\n"
                                    "}")
        self.bg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg_frame.setObjectName("bg_frame")
        self.label_admin_txt = QtWidgets.QLabel(self.bg_frame)
        self.label_admin_txt.setGeometry(QtCore.QRect(0, 0, 1080, 91))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_admin_txt.sizePolicy().hasHeightForWidth())
        self.label_admin_txt.setSizePolicy(sizePolicy)
        self.label_admin_txt.setMaximumSize(QtCore.QSize(1080, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_admin_txt.setFont(font)
        self.label_admin_txt.setStyleSheet("QLabel#label_admin_txt{\n"
                                           "    color: rgb(255, 255, 0);\n"
                                           "background-color: rgb(25, 25, 25);\n"
                                           "border-style:double;\n"
                                           "border-width:3px;\n"
                                           "    border-color: rgb(0, 255, 255);\n"
                                           "\n"
                                           "}")
        self.label_admin_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_admin_txt.setObjectName("label_admin_txt")
        self.admin_tab = QtWidgets.QTabWidget(self.bg_frame)
        self.admin_tab.setGeometry(QtCore.QRect(0, 90, 1081, 631))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_tab.sizePolicy().hasHeightForWidth())
        self.admin_tab.setSizePolicy(sizePolicy)
        self.admin_tab.setMaximumSize(QtCore.QSize(1081, 631))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.admin_tab.setFont(font)
        self.admin_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.admin_tab.setStyleSheet("QTabWidget#admin_tab{\n"
                                     "\n"
                                     "    background-color: rgb(25, 25, 25);\n"
                                     "    color: rgb(255, 170, 0);\n"
                                     "}")
        self.admin_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.admin_tab.setTabBarAutoHide(False)
        self.admin_tab.setObjectName("admin_tab")
        self.change_tab = QtWidgets.QWidget()
        self.change_tab.setObjectName("change_tab")
        self.change_tab_bg = QtWidgets.QLabel(self.change_tab)
        self.change_tab_bg.setGeometry(QtCore.QRect(0, 0, 1081, 601))
        self.change_tab_bg.setStyleSheet("QLabel#change_tab_bg{\n"
                                         "    color: rgb(85, 0, 127);\n"
                                         "\n"
                                         "\n"
                                         "}")
        self.change_tab_bg.setText("")
        self.change_tab_bg.setPixmap(QtGui.QPixmap(":/src/source/BG_2.jpg"))
        self.change_tab_bg.setScaledContents(True)
        self.change_tab_bg.setObjectName("change_tab_bg")
        self.lbl_dept_txt = QtWidgets.QLabel(self.change_tab)
        self.lbl_dept_txt.setGeometry(QtCore.QRect(50, 160, 211, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lbl_dept_txt.sizePolicy().hasHeightForWidth())
        self.lbl_dept_txt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_dept_txt.setFont(font)
        self.lbl_dept_txt.setStyleSheet("QLabel#lbl_dept_txt{\n"
                                        "\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}")
        self.lbl_dept_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_dept_txt.setObjectName("lbl_dept_txt")
        self.lbl_sem = QtWidgets.QLabel(self.change_tab)
        self.lbl_sem.setGeometry(QtCore.QRect(660, 160, 211, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lbl_sem.sizePolicy().hasHeightForWidth())
        self.lbl_sem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_sem.setFont(font)
        self.lbl_sem.setStyleSheet("QLabel#lbl_sem{\n"
                                   "\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "}")
        self.lbl_sem.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sem.setObjectName("lbl_sem")
        self.dept_combo = QtWidgets.QComboBox(self.change_tab)
        self.dept_combo.setGeometry(QtCore.QRect(270, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.dept_combo.setFont(font)
        self.dept_combo.setStyleSheet("QComboBox#dept_combo{\n"
                                      "\n"
                                      "border-radius:5px;\n"
                                      "}")
        self.dept_combo.setObjectName("dept_combo")
        self.dept_combo.addItem("")
        self.dept_combo.addItem("")
        self.dept_combo.addItem("")
        self.dept_combo.addItem("")
        self.dept_combo.addItem("")
        self.dept_combo.addItem("")
        self.sem_combo = QtWidgets.QComboBox(self.change_tab)
        self.sem_combo.setGeometry(QtCore.QRect(860, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.sem_combo.setFont(font)
        self.sem_combo.setStyleSheet("QComboBox#sem_combo{\n"
                                     "border-radius:5px;\n"
                                     "\n"
                                     "}")
        self.sem_combo.setObjectName("sem_combo")
        self.sem_combo.addItem("")
        self.sem_combo.addItem("")
        self.sem_combo.addItem("")
        self.sem_combo.addItem("")
        self.sem_combo.addItem("")
        self.sem_combo.addItem("")
        self.sem_combo.addItem("")
        self.sem_combo.addItem("")
        self.sem_combo.addItem("")
        self.linedit_file = QtWidgets.QLineEdit(self.change_tab)
        self.linedit_file.setGeometry(QtCore.QRect(270, 290, 381, 41))
        self.linedit_file.setStyleSheet("QLineEdit#linedit_file{\n"
                                        "\n"
                                        "border-radius:5px;\n"
                                        "}\n"
                                        "QLineEdit#linedit_file: hover{\n"
                                        "\n"
                                        "border-radius:5px;\n"
                                        "border-width:3px;\n"
                                        "    border-color: rgb(212, 212, 212);\n"
                                        "}")
        self.linedit_file.setObjectName("linedit_file")
        self.btn_upload = QtWidgets.QPushButton(self.change_tab)
        self.btn_upload.setGeometry(QtCore.QRect(670, 290, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_upload.setFont(font)
        self.btn_upload.setStyleSheet("QPushButton#btn_upload{\n"
                                      "\n"
                                      "    background-color: rgb(0, 170, 255);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "BORDER-RADIUS:10PX;\n"
                                      "border-style:inset;\n"
                                      "    border-color: rgb(218, 218, 218);\n"
                                      "border-width:3px;\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton#btn_upload:hover{\n"
                                      "    background-color: rgb(0, 85, 255);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "BORDER-RADIUS:10PX;\n"
                                      "border-style:inset;\n"
                                      "    border-color: rgb(218, 218, 218);\n"
                                      "border-width:4px;\n"
                                      "\n"
                                      "\n"
                                      "}")
        self.btn_upload.setObjectName("btn_upload")
        self.btn_upload.clicked.connect(self.set_file)
        self.btn_save = QtWidgets.QPushButton(self.change_tab)
        self.btn_save.setGeometry(QtCore.QRect(450, 480, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton#btn_save{\n"
                                    "\n"
                                    "    background-color: rgb(0, 170, 255);\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "BORDER-RADIUS:10PX;\n"
                                    "border-style:inset;\n"
                                    "    border-color: rgb(218, 218, 218);\n"
                                    "border-width:3px;\n"
                                    "\n"
                                    "}\n"
                                    "QPushButton#btn_save:hover{\n"
                                    "    background-color: rgb(0, 85, 255);\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "BORDER-RADIUS:10PX;\n"
                                    "border-style:inset;\n"
                                    "    border-color: rgb(218, 218, 218);\n"
                                    "border-width:4px;\n"
                                    "\n"
                                    "\n"
                                    "}")
        self.btn_save.setObjectName("btn_save")
        self.admin_tab.addTab(self.change_tab, "")
        self.tab_preview = QtWidgets.QWidget()
        self.tab_preview.setObjectName("tab_preview")
        self.preview_bg_lbl = QtWidgets.QLabel(self.tab_preview)
        self.preview_bg_lbl.setGeometry(QtCore.QRect(-580, -80, 1691, 701))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.preview_bg_lbl.sizePolicy().hasHeightForWidth())
        self.preview_bg_lbl.setSizePolicy(sizePolicy)
        self.preview_bg_lbl.setStyleSheet("QLabel#preview_bg_lbl{\n"
                                          "\n"
                                          "}")
        self.preview_bg_lbl.setText("")
        self.preview_bg_lbl.setPixmap(QtGui.QPixmap(":/src/source/bg 3.png"))
        self.preview_bg_lbl.setScaledContents(True)
        self.preview_bg_lbl.setObjectName("preview_bg_lbl")
        self.bg_table_vieew = QtWidgets.QTableWidget(self.tab_preview)
        self.bg_table_vieew.setGeometry(QtCore.QRect(10, 10, 1051, 511))
        self.bg_table_vieew.setStyleSheet("QTableView#bg_table_vieew{\n"
                                          "\n"
                                          "border-radius:10px;\n"
                                          "border-style:solid;\n"
                                          "}")
        self.bg_table_vieew.setObjectName("bg_table_vieew")
        self.bg_table_vieew.setColumnCount(0)
        self.bg_table_vieew.setRowCount(0)
        self.admin_tab.addTab(self.tab_preview, "")
        self.record_tab = QtWidgets.QWidget()
        self.record_tab.setObjectName("record_tab")
        self.record_tab_bg = QtWidgets.QLabel(self.record_tab)
        self.record_tab_bg.setGeometry(QtCore.QRect(0, 0, 1111, 601))
        self.record_tab_bg.setText("")
        self.record_tab_bg.setPixmap(QtGui.QPixmap(":/src/source/bg 3.png"))
        self.record_tab_bg.setScaledContents(True)
        self.record_tab_bg.setObjectName("record_tab_bg")
        self.bg_table_records = QtWidgets.QTableWidget(self.record_tab)
        self.bg_table_records.setGeometry(QtCore.QRect(10, 80, 1051, 501))
        self.bg_table_records.setStyleSheet("QTableView#bg_table_vieew{\n"
                                            "\n"
                                            "border-radius:10px;\n"
                                            "border-style:solid;\n"
                                            "}")
        self.bg_table_records.setObjectName("bg_table_records")
        self.bg_table_records.setColumnCount(0)
        self.bg_table_records.setRowCount(0)
        self.btn_show_records = QtWidgets.QPushButton(self.record_tab)
        self.btn_show_records.setGeometry(QtCore.QRect(860, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        self.btn_show_records.setFont(font)
        self.btn_show_records.setStyleSheet("QPushButton#btn_show_records{\n"
                                            "\n"
                                            "    background-color: rgb(0, 170, 255);\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "BORDER-RADIUS:10PX;\n"
                                            "border-style:inset;\n"
                                            "    border-color: rgb(218, 218, 218);\n"
                                            "border-width:3px;\n"
                                            "\n"
                                            "}\n"
                                            "QPushButton#btn_show_records:hover{\n"
                                            "    background-color: rgb(0, 85, 255);\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "BORDER-RADIUS:10PX;\n"
                                            "border-style:inset;\n"
                                            "    border-color: rgb(218, 218, 218);\n"
                                            "border-width:4px;\n"
                                            "\n"
                                            "\n"
                                            "}")
        self.btn_show_records.setObjectName("btn_show_records")
        self.btn_show_records.clicked.connect(self.get_record)
        self.lbl_dept_txt_2 = QtWidgets.QLabel(self.record_tab)
        self.lbl_dept_txt_2.setGeometry(QtCore.QRect(50, 30, 171, 21))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lbl_dept_txt_2.sizePolicy().hasHeightForWidth())
        self.lbl_dept_txt_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_dept_txt_2.setFont(font)
        self.lbl_dept_txt_2.setStyleSheet("QLabel#lbl_dept_txt{\n"
                                          "\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "}")
        self.lbl_dept_txt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_dept_txt_2.setObjectName("lbl_dept_txt_2")
        self.dept_combo_2 = QtWidgets.QComboBox(self.record_tab)
        self.dept_combo_2.setGeometry(QtCore.QRect(230, 30, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.dept_combo_2.setFont(font)
        self.dept_combo_2.setStyleSheet("QComboBox#dept_combo_2{\n"
                                        "\n"
                                        "border-radius:5px;\n"
                                        "}")
        self.dept_combo_2.setObjectName("dept_combo_2")
        self.dept_combo_2.addItem("")
        self.dept_combo_2.addItem("")
        self.dept_combo_2.addItem("")
        self.dept_combo_2.addItem("")
        self.dept_combo_2.addItem("")
        self.dept_combo_2.addItem("")
        self.lbl_sem_2 = QtWidgets.QLabel(self.record_tab)
        self.lbl_sem_2.setGeometry(QtCore.QRect(470, 25, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lbl_sem_2.sizePolicy().hasHeightForWidth())
        self.lbl_sem_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_sem_2.setFont(font)
        self.lbl_sem_2.setStyleSheet("QLabel#lbl_sem{\n"
                                     "\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "}")
        self.lbl_sem_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sem_2.setObjectName("lbl_sem_2")
        self.sem_combo_2 = QtWidgets.QComboBox(self.record_tab)
        self.sem_combo_2.setGeometry(QtCore.QRect(640, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.sem_combo_2.setFont(font)
        self.sem_combo_2.setStyleSheet("QComboBox#sem_combo_2{\n"
                                       "border-radius:5px;\n"
                                       "\n"
                                       "}")
        self.sem_combo_2.setObjectName("sem_combo_2")
        self.sem_combo_2.addItem("")
        self.sem_combo_2.addItem("")
        self.sem_combo_2.addItem("")
        self.sem_combo_2.addItem("")
        self.sem_combo_2.addItem("")
        self.sem_combo_2.addItem("")
        self.sem_combo_2.addItem("")
        self.sem_combo_2.addItem("")
        self.sem_combo_2.addItem("")
        self.admin_tab.addTab(self.record_tab, "")
        admin_dashboard.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(admin_dashboard)
        self.admin_tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(admin_dashboard)

    def retranslateUi(self, admin_dashboard):
        _translate = QtCore.QCoreApplication.translate
        admin_dashboard.setWindowTitle(_translate(
            "admin_dashboard", "ADMIN DASHBOARD"))
        self.label_admin_txt.setText(_translate(
            "admin_dashboard", "WELCOME ADMIN!"))
        self.lbl_dept_txt.setText(_translate(
            "admin_dashboard", "SELECT DEPARTMENT:"))
        self.lbl_sem.setText(_translate("admin_dashboard", "SELECT SEMESTER:"))
        self.dept_combo.setItemText(0, _translate("admin_dashboard", "SELECT"))
        self.dept_combo.setItemText(1, _translate(
            "admin_dashboard", "INFORMATION TECHNOLOGY"))
        self.dept_combo.setItemText(2, _translate(
            "admin_dashboard", "COMPUTER SCIENCE"))
        self.dept_combo.setItemText(3, _translate("admin_dashboard", "EXTC"))
        self.dept_combo.setItemText(
            4, _translate("admin_dashboard", "MECHANICAL"))
        self.dept_combo.setItemText(
            5, _translate("admin_dashboard", "BIO-MEDICAL"))
        self.sem_combo.setItemText(0, _translate("admin_dashboard", "SELECT"))
        self.sem_combo.setItemText(1, _translate("admin_dashboard", "SEM I"))
        self.sem_combo.setItemText(2, _translate("admin_dashboard", "SEM II"))
        self.sem_combo.setItemText(3, _translate("admin_dashboard", "SEM III"))
        self.sem_combo.setItemText(4, _translate("admin_dashboard", "SEM IV"))
        self.sem_combo.setItemText(5, _translate("admin_dashboard", "SEM V"))
        self.sem_combo.setItemText(6, _translate("admin_dashboard", "SEM VI"))
        self.sem_combo.setItemText(7, _translate("admin_dashboard", "SEM VII"))
        self.sem_combo.setItemText(
            8, _translate("admin_dashboard", "SEM VIII"))
        self.btn_upload.setText(_translate("admin_dashboard", "UPLOAD"))
        self.btn_save.setText(_translate("admin_dashboard", "SAVE"))
        self.admin_tab.setTabText(self.admin_tab.indexOf(
            self.change_tab), _translate("admin_dashboard", "CHANGE"))
        self.admin_tab.setTabText(self.admin_tab.indexOf(
            self.tab_preview), _translate("admin_dashboard", "PREVEIW"))
        self.btn_show_records.setText(
            _translate("admin_dashboard", "SHOW RECORDS"))
        self.lbl_dept_txt_2.setText(_translate(
            "admin_dashboard", "SELECT DEPARTMENT:"))
        self.dept_combo_2.setItemText(
            0, _translate("admin_dashboard", "SELECT"))
        self.dept_combo_2.setItemText(1, _translate(
            "admin_dashboard", "INFORMATION TECHNOLOGY"))
        self.dept_combo_2.setItemText(2, _translate(
            "admin_dashboard", "COMPUTER SCIENCE"))
        self.dept_combo_2.setItemText(3, _translate("admin_dashboard", "EXTC"))
        self.dept_combo_2.setItemText(
            4, _translate("admin_dashboard", "MECHANICAL"))
        self.dept_combo_2.setItemText(
            5, _translate("admin_dashboard", "BIO-MEDICAL"))
        self.lbl_sem_2.setText(_translate(
            "admin_dashboard", "SELECT SEMESTER:"))
        self.sem_combo_2.setItemText(
            0, _translate("admin_dashboard", "SELECT"))
        self.sem_combo_2.setItemText(1, _translate("admin_dashboard", "SEM I"))
        self.sem_combo_2.setItemText(
            2, _translate("admin_dashboard", "SEM II"))
        self.sem_combo_2.setItemText(
            3, _translate("admin_dashboard", "SEM III"))
        self.sem_combo_2.setItemText(
            4, _translate("admin_dashboard", "SEM IV"))
        self.sem_combo_2.setItemText(5, _translate("admin_dashboard", "SEM V"))
        self.sem_combo_2.setItemText(
            6, _translate("admin_dashboard", "SEM VI"))
        self.sem_combo_2.setItemText(
            7, _translate("admin_dashboard", "SEM VII"))
        self.sem_combo_2.setItemText(
            8, _translate("admin_dashboard", "SEM VIII"))
        self.admin_tab.setTabText(self.admin_tab.indexOf(
            self.record_tab), _translate("admin_dashboard", "RECORDS"))
        self.mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )

    def upload_File_it(self,file_path,sem_data):
        print(sem_data)
        print(file_path)
        try:
            print("hi")
            mycursor = self.mydb.cursor()
            query = ("SELECT * FROM it_exel_file where sem ='"+sem_data+"' and file_path ='"+file_path+"'")
            mycursor.execute(query)
            result = mycursor.fetchone()
            print("hello")

            if result:

                self.message("WARNNING!!","FILE IS ALREADY UPLOADED")

            else:
                mycursor.execute("insert into it_exel_file values('"+sem_data+"','"+file_path+"')")
                print("hello")
                self.mydb.commit()
                self.message("CONGRATULATION!!","YOUR FILE IS BEAN UPLOADED!!")

        except mc.Error as e:
            print(e)

    def upload_File_cs(self,file_path,sem_data):
        print(sem_data)
        print(file_path)
        try:
            print("hi")
            mycursor = self.mydb.cursor()
            query = ("SELECT * FROM cs_exel_file where sem ='"+sem_data+"' and file_path ='"+file_path+"'")
            mycursor.execute(query)
            result = mycursor.fetchone()
            print("hello")

            if result:

                self.message("WARNNING!!","FILE IS ALREADY UPLOADED")

            else:
                mycursor.execute("insert into cs_exel_file values('"+sem_data+"','"+file_path+"')")
                print("hello")
                self.mydb.commit()
                self.message("CONGRATULATION!!","YOUR FILE IS BEAN UPLOADED!!")

        except mc.Error as e:
            print(e)

    def upload_File_extc(self,file_path,sem_data):
        print(sem_data)
        print(file_path)
        try:
            print("hi")
            mycursor = self.mydb.cursor()
            query = ("SELECT * FROM extc_exel_file where sem ='"+sem_data+"' and file_path ='"+file_path+"'")
            mycursor.execute(query)
            result = mycursor.fetchone()
            print("hello")

            if result:

                self.message("WARNNING!!","FILE IS ALREADY UPLOADED")

            else:
                mycursor.execute("insert into extc_exel_file values('"+sem_data+"','"+file_path+"')")
                print("hello")
                self.mydb.commit()
                self.message("CONGRATULATION!!","YOUR FILE IS BEAN UPLOADED!!")

        except mc.Error as e:
            print(e)
            
    def upload_File_mech(self,file_path,sem_data):
        print(sem_data)
        print(file_path)
        try:
            print("hi")
            mycursor = self.mydb.cursor()
            query = ("SELECT * FROM mechanical_exel_file where sem ='"+sem_data+"' and file_path ='"+file_path+"'")
            mycursor.execute(query)
            result = mycursor.fetchone()
            print("hello")

            if result:

                self.message("WARNNING!!","FILE IS ALREADY UPLOADED")

            else:
                mycursor.execute("insert mechanical_exel_file values('"+sem_data+"','"+file_path+"')")
                print("hello")
                self.mydb.commit()
                self.message("CONGRATULATION!!","YOUR FILE IS BEAN UPLOADED!!")

        except mc.Error as e:
            print(e)

    def upload_File_biomed(self,file_path,sem_data):
        print(sem_data)
        print(file_path)
        try:
            print("hi")
            mycursor = self.mydb.cursor()
            query = ("SELECT * FROM biomed_exel_file where sem ='"+sem_data+"' and file_path ='"+file_path+"'")
            mycursor.execute(query)
            result = mycursor.fetchone()
            print("hello")

            if result:

                self.message("WARNNING!!","FILE IS ALREADY UPLOADED")

            else:
                mycursor.execute("insert into biomed_exel_file values('"+sem_data+"','"+file_path+"')")
                print("hello")
                self.mydb.commit()
                self.message("CONGRATULATION!!","YOUR FILE IS BEAN UPLOADED!!")

        except mc.Error as e:
            print(e)
        

    def set_file(self):
        department_data = self.dept_combo.currentText()
        sem_data=self.sem_combo.currentText()

        Fname=QFileDialog.getOpenFileName(None,"open File","","All File (*);;Exel File (*.xlsx)")
        file_path=Fname[0]
        if Fname:
            self.linedit_file.setText(Fname[0].split("/")[-1])  


        if department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM III":
            self.upload_File_it(file_path,sem_data) 
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM IV":
            self.upload_File_it(file_path,sem_data) 
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM V":
            self.upload_File_it(file_path,sem_data) 
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM VI":
            self.upload_File_it(file_path,sem_data) 
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM VII":
            self.upload_File_it(file_path,sem_data) 
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM VIII":
            self.upload_File_it(file_path,sem_data) 
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM III":
            self.upload_File_cs(file_path,sem_data)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM IV":
            self.upload_File_cs(file_path,sem_data)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM V":
            self.upload_File_cs(file_path,sem_data)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM VI":
            self.upload_File_cs(file_path,sem_data)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM VII":
            self.upload_File_cs(file_path,sem_data)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM VIII":
            self.upload_File_cs(file_path,sem_data)
        elif department_data=="EXTC" and sem_data=="SEM III":
            self.upload_File_extc(file_path,sem_data)
        elif department_data=="EXTC" and sem_data=="SEM IV":
            self.upload_File_extc(file_path,sem_data)
        elif department_data=="EXTC" and sem_data=="SEM V":
            self.upload_File_extc(file_path,sem_data)
        elif department_data=="EXTC" and sem_data=="SEM VI":
            self.upload_File_extc(file_path,sem_data)
        elif department_data=="EXTC" and sem_data=="SEM VII":
            self.upload_File_extc(file_path,sem_data)
        elif department_data=="EXTC" and sem_data=="SEM VIII":
            self.upload_File_extc(file_path,sem_data)
        elif department_data=="MECHANICAL" and sem_data=="SEM III":
            self.upload_File_mech(file_path,sem_data)
        elif department_data=="MECHANICAL" and sem_data=="SEM IV":
            self.upload_File_mech(file_path,sem_data)
        elif department_data=="MECHANICAL" and sem_data=="SEM V":
            self.upload_File_mech(file_path,sem_data)
        elif department_data=="MECHANICAL" and sem_data=="SEM VI":
            self.upload_File_mech(file_path,sem_data)
        elif department_data=="MECHANICAL" and sem_data=="SEM VII":
            self.upload_File_mech(file_path,sem_data)
        elif department_data=="MECHANICAL" and sem_data=="SEM VIII":
            self.upload_File_mech(file_path,sem_data)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM III":
            self.upload_File_biomed(file_path,sem_data)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM IV":
            self.upload_File_biomed(file_path,sem_data)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM V":
            self.upload_File_biomed(file_path,sem_data)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM VI":
            self.upload_File_biomed(file_path,sem_data)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM VII":
            self.upload_File_biomed(file_path,sem_data)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM VIII":
            self.upload_File_biomed(file_path,sem_data)
        else:
            print("error")

    def get_record(self):
        print("hello")
        department_data = self.dept_combo_2.currentText()
        sem_data=self.sem_combo_2.currentText()
        if department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM III":
            try:
                print("hi")
                mycursor = self.mydb.cursor()
                query = ("SELECT * FROM it_exel_file where sem ='"+sem_data+"'")
                mycursor.execute(query)
                result = mycursor.fetchone()
                self.bg_table_records.setRowCount(0)

                for row_number,row_data in enumerate(result):
                    self.bg_table_records.insertRow(row_number)

                    for collum_number , data in enumerate(row_data):
                        self.bg_table_records.setItem(row_number,collum_number,QtWidgets.QTableWidgetItem(str(data)))
            except mc.Error as e:
                print(e)  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_dashboard = QtWidgets.QMainWindow()
    ui = Ui_admin_dashboard()
    ui.setupUi(admin_dashboard)
    admin_dashboard.show()
    sys.exit(app.exec_())
