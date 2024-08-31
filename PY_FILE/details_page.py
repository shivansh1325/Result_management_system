


import src,uploadN,admin_dahsboard
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
import pandas as pdn 


class Ui_MainWindow(object):
    
    def openwindow(self):
        self.window = admin_dahsboard.QtWidgets.QMainWindow()
        self.ui = admin_dahsboard.Ui_admin_dashboard()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 650))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.detail_label = QtWidgets.QLabel(self.centralwidget)
        self.detail_label.setGeometry(QtCore.QRect(320, 30, 321, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.detail_label.sizePolicy().hasHeightForWidth())
        self.detail_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.detail_label.setFont(font)
        self.detail_label.setStyleSheet("QLabel#detail_label{\n"
                                        "border-style:groove;\n"
                                        "border-width:3px;\n"
                                        "    border-color: rgb(170, 255, 127);\n"
                                        "border-radius:10px;\n"
                                        "    color: rgb(255, 255, 0);\n"
                                        "text-shadow: 0 0 3px #FF0000;\n"
                                        "\n"
                                        "}")
        self.detail_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detail_label.setObjectName("detail_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, -10, 1051, 671))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(1000, 650))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/SOURCE/SOURCE/detail bg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.BG_frame = QtWidgets.QFrame(self.centralwidget)
        self.BG_frame.setGeometry(QtCore.QRect(120, 110, 721, 441))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.BG_frame.sizePolicy().hasHeightForWidth())
        self.BG_frame.setSizePolicy(sizePolicy)
        self.BG_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.BG_frame.setStyleSheet("QFrame#BG_frame{\n"
                                    "background-color: rgb(255, 249, 158);\n"
                                    "border-style:dashed;\n"
                                    "border-width:5px;\n"
                                    "    border-color: rgb(0, 170, 127);\n"
                                    "border-radius:20px;\n"
                                    "}")
        self.BG_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BG_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BG_frame.setObjectName("BG_frame")
        self.label_dept = QtWidgets.QLabel(self.BG_frame)
        self.label_dept.setGeometry(QtCore.QRect(60, 70, 150, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_dept.sizePolicy().hasHeightForWidth())
        self.label_dept.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dept.setFont(font)
        self.label_dept.setObjectName("label_dept")
        self.COMBO_DEPT = QtWidgets.QComboBox(self.BG_frame)
        self.COMBO_DEPT.setGeometry(QtCore.QRect(260, 70, 251, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.COMBO_DEPT.sizePolicy().hasHeightForWidth())
        self.COMBO_DEPT.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.COMBO_DEPT.setFont(font)
        self.COMBO_DEPT.setStyleSheet("QComboBox#COMBO_DEPT{\n"
                                      "border-style:solid;\n"
                                      "border-width:3px;\n"
                                      "border-radius:9px;\n"
                                      "    border-color: rgb(255, 0, 127);\n"
                                      "}\n"
                                      "QComboBox#COMBO_DEPT:hover{\n"
                                      "border-style:solid;\n"
                                      "border-width:4px;\n"
                                      "border-radius:9px;\n"
                                      "    border-color: rgb(255, 0, 127);\n"
                                      "}")
        self.COMBO_DEPT.setObjectName("COMBO_DEPT")
        self.COMBO_DEPT.addItem("")
        self.COMBO_DEPT.addItem("")
        self.COMBO_DEPT.addItem("")
        self.COMBO_DEPT.addItem("")
        self.COMBO_DEPT.addItem("")
        self.COMBO_DEPT.addItem("")
        self.COMBO_DEPT.addItem("")
        self.COMBO_DEPT.addItem("")
        self.label_sem = QtWidgets.QLabel(self.BG_frame)
        self.label_sem.setGeometry(QtCore.QRect(60, 140, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_sem.sizePolicy().hasHeightForWidth())
        self.label_sem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_sem.setFont(font)
        self.label_sem.setObjectName("label_sem")
        self.combo_sem = QtWidgets.QComboBox(self.BG_frame)
        self.combo_sem.setGeometry(QtCore.QRect(260, 140, 251, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.combo_sem.sizePolicy().hasHeightForWidth())
        self.combo_sem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_sem.setFont(font)
        self.combo_sem.setStyleSheet("QComboBox#combo_sem{\n"
                                     "border-style:solid;\n"
                                     "border-width:3px;\n"
                                     "border-radius:9px;\n"
                                     "    border-color: rgb(255, 0, 127);\n"
                                     "}\n"
                                     "QComboBox#combo_sem:hover{\n"
                                     "border-style:solid;\n"
                                     "border-width:4px;\n"
                                     "border-radius:9px;\n"
                                     "    border-color: rgb(255, 0, 127);\n"
                                     "}")
        self.combo_sem.setObjectName("combo_sem")
        self.combo_sem.addItem("")
        self.combo_sem.addItem("")
        self.combo_sem.addItem("")
        self.combo_sem.addItem("")
        self.combo_sem.addItem("")
        self.combo_sem.addItem("")
        self.combo_sem.addItem("")
        self.combo_sem.addItem("")
        self.combo_sem.addItem("")
        self.label_format = QtWidgets.QLabel(self.BG_frame)
        self.label_format.setGeometry(QtCore.QRect(60, 210, 170, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_format.sizePolicy().hasHeightForWidth())
        self.label_format.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_format.setFont(font)
        self.label_format.setObjectName("label_format")
        self.combo_format = QtWidgets.QComboBox(self.BG_frame)
        self.combo_format.setGeometry(QtCore.QRect(260, 210, 251, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.combo_format.sizePolicy().hasHeightForWidth())
        self.combo_format.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_format.setFont(font)
        self.combo_format.setStyleSheet("QComboBox#combo_format{\n"
                                        "border-style:solid;\n"
                                        "border-width:3px;\n"
                                        "border-radius:9px;\n"
                                        "    border-color: rgb(255, 0, 127);\n"
                                        "}\n"
                                        "QComboBox#combo_format:hover{\n"
                                        "border-style:solid;\n"
                                        "border-width:4px;\n"
                                        "border-radius:9px;\n"
                                        "    border-color: rgb(255, 0, 127);\n"
                                        "}")
        self.combo_format.setObjectName("combo_format")
        self.combo_format.addItem("")
        self.combo_format.addItem("")
        self.combo_format.addItem("")
        self.combo_format.addItem("")
        self.label_year = QtWidgets.QLabel(self.BG_frame)
        self.label_year.setGeometry(QtCore.QRect(60, 280, 175, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_year.sizePolicy().hasHeightForWidth())
        self.label_year.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_year.setFont(font)
        self.label_year.setObjectName("label_year")
        self.year_txt = QtWidgets.QLineEdit(self.BG_frame)
        self.year_txt.setGeometry(QtCore.QRect(260, 280, 251, 31))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.year_txt.sizePolicy().hasHeightForWidth())
        self.year_txt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.year_txt.setFont(font)
        self.year_txt.setStyleSheet("QLineEdit#year_txt{\n"
                                    "border-style:solid;\n"
                                    "border-width:3px;\n"
                                    "border-radius:9px;\n"
                                    "    border-color: rgb(255, 0, 127);\n"
                                    "\n"
                                    "}\n"
                                    "QLineEdit#year_txt:hover{\n"
                                    "border-style:solid;\n"
                                    "border-width:4px;\n"
                                    "border-radius:9px;\n"
                                    "    border-color: rgb(255, 0, 127);\n"
                                    "\n"
                                    "}")
        self.year_txt.setObjectName("year_txt")
        self.btn_start = QtWidgets.QPushButton(self.BG_frame)
        self.btn_start.setGeometry(QtCore.QRect(430, 350, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start.setFont(font)
        self.btn_start.clicked.connect(self.enter_detail)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_start.setStyleSheet("QPushButton#btn_start{\n"
                                     "border-style:solid;\n"
                                     "border-width:3px;\n"
                                     "border-radius:15px;\n"
                                     "background-color: rgb(255, 170, 0);\n"
                                     "    border-color: rgb(0, 0, 127);\n"
                                     "}\n"
                                     "QPushButton#btn_start:hover{\n"
                                     "background-color: rgb(0, 170, 0);\n"
                                     "}\n"
                                     "QPushButton#btn_start:pressed{\n"
                                     "background-color: rgb(255, 85, 0);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "")
        self.btn_start.setObjectName("btn_start")
        self.label.raise_()
        self.detail_label.raise_()
        self.BG_frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DETAILS PAGE"))
        self.detail_label.setText(_translate("MainWindow", "ENTER DETAILS!"))
        self.label_dept.setText(_translate("MainWindow", "DEPARTMENT:"))
        
        self.COMBO_DEPT.setCurrentText(_translate("MainWindow", "SELECT"))
        self.COMBO_DEPT.setItemText(0, _translate("MainWindow", "SELECT"))
        self.COMBO_DEPT.setItemText(1, _translate("MainWindow", "INFORMATION TECHNOLOGY"))
        self.COMBO_DEPT.setItemText(2, _translate("MainWindow", "COMPUTER SCIENCE"))
        self.COMBO_DEPT.setItemText(3, _translate("MainWindow", "EXTC"))
        self.COMBO_DEPT.setItemText(4, _translate("MainWindow", "MECHANICAL"))
        self.COMBO_DEPT.setItemText(5, _translate("MainWindow", "CHEMICAL"))
        self.COMBO_DEPT.setItemText(6, _translate("MainWindow", "BIO-MEDICAL"))
        self.COMBO_DEPT.setItemText(7, _translate("MainWindow", "CIVIL"))
        self.label_sem.setText(_translate("MainWindow", "SEMESTER:"))
        self.combo_sem.setCurrentText(_translate("MainWindow", "SELECT"))
        self.combo_sem.setItemText(0, _translate("MainWindow", "SELECT"))
        self.combo_sem.setItemText(1, _translate("MainWindow", "SEM I"))
        self.combo_sem.setItemText(2, _translate("MainWindow", "SEM II"))
        self.combo_sem.setItemText(3, _translate("MainWindow", "SEM III"))
        self.combo_sem.setItemText(4, _translate("MainWindow", "SEM IV"))
        self.combo_sem.setItemText(5, _translate("MainWindow", "SEM V"))
        self.combo_sem.setItemText(6, _translate("MainWindow", "SEM VI"))
        self.combo_sem.setItemText(7, _translate("MainWindow", "SEM VII"))
        self.combo_sem.setItemText(8, _translate("MainWindow", "SEM VIII"))
        self.label_format.setText(_translate("MainWindow", "SELECT FORMAT:"))
        self.combo_format.setCurrentText(_translate("MainWindow", "SELECT"))
        self.combo_format.setItemText(0, _translate("MainWindow", "SELECT"))
        self.combo_format.setItemText(
            1, _translate("MainWindow", "UNIT TEST- I"))
        self.combo_format.setItemText(
            2, _translate("MainWindow", "UNIT TEST- II"))
        self.combo_format.setItemText(
            3, _translate("MainWindow", "SEMESTER END EXAM"))
        self.label_year.setText(_translate("MainWindow", "ACADEMIC YEAR:"))
        self.year_txt.setPlaceholderText(
            _translate("MainWindow", "Academic Year"))
        self.btn_start.setText(_translate(
            "MainWindow", "START ENTERING DETAILS"))

        # self.department_data = self.COMBO_DEPT.currentText()
        # self.sem_data=self.combo_sem.currentText()
        # self.format_data=self.combo_format.currentText()
        # self.year_data=self.year_txt.text()
    def convert_tuple(self,path):  
        str=''.join(path)  
        return str  
    
    def open_uploadN(self,url):
        self.window = uploadN.QtWidgets.QMainWindow()
        self.ui = uploadN.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.show_data(url)
        self.window.show()
   
    def open_upload_It(self,sem):

        try:
            
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )
            print("hi")
            mycursor = mydb.cursor()
            query = ("SELECT file_path FROM it_exel_file where sem='"+sem+"'")
            mycursor.execute(query)
            path = mycursor.fetchone()
            print("hi")
            path_string=self.convert_tuple(path)  
            url=path_string
            print(url)
            self.open_uploadN(url)
            
        except mc.Error as e:
            print(e)
            print("error has occured")    
    
    def open_upload_cs(self,sem):

        try:
            
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )
            print("hi")
            # print(file_db)
            # print(sem)
            mycursor = mydb.cursor()
            query = ("SELECT file_path FROM cs_exel_file where sem='"+sem+"'")
            mycursor.execute(query)
            path = mycursor.fetchone()
            print("hi")
            path_string=self.convert_tuple(path)  
            # url=r"C:\Users\shiva\Desktop\PY_FILE\PY_FILE\Book1.xlsx"
            url=path_string
            print(url)
            
            self.open_uploadN(url)
            
        except mc.Error as e:
            print(e)
            print("error has occured") 

    def open_upload_EXTC(self,sem):

        try:
            
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )
            print("hi")
            mycursor = mydb.cursor()
            query = ("SELECT file_path FROM extc_exel_file where sem='"+sem+"'")
            mycursor.execute(query)
            path = mycursor.fetchone()
            print("hi")
            path_string=self.convert_tuple(path)  
            url=path_string
            print(url)
            self.open_uploadN(url)
            
        except mc.Error as e:
            print(e)
            print("error has occured")

    def open_upload_BIO_MEDICAL(self,sem):

        try:
            
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )
            print("hi")
            mycursor = mydb.cursor()
            query = ("SELECT file_path FROM biomed_exel_file where sem='"+sem+"'")
            mycursor.execute(query)
            path = mycursor.fetchone()
            print("hi")
            path_string=self.convert_tuple(path)  
            url=path_string
            print(url)
            self.open_uploadN(url)
            
        except mc.Error as e:
            print(e)
            print("error has occured")

    def open_upload_MECHANICAL(self,sem):

        try:
            
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )
            print("hi")
            mycursor = mydb.cursor()
            query = ("SELECT file_path FROM mechanical_exel_file where sem='"+sem+"'")
            mycursor.execute(query)
            path = mycursor.fetchone()
            print("hi")
            path_string=self.convert_tuple(path)  
            url=path_string
            print(url)
            self.open_uploadN(url)
            
        except mc.Error as e:
            print(e)
            print("error has occured")

    def enter_detail(self,Fname):
        department_data = self.COMBO_DEPT.currentText()
        sem_data=self.combo_sem.currentText()
        format_data=self.combo_format.currentText()
        year_data=self.year_txt.text()
        
        if department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM III":
            sem=sem_data
            self.open_upload_It(sem)
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM IV":
            sem=sem_data
            self.open_upload_It(sem)
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM V":
            sem=sem_data
            self.open_upload_It(sem)
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM VI":
            sem=sem_data
            self.open_upload_It(sem)
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM VII":
            sem=sem_data
            self.open_upload_It(sem)
        elif department_data=="INFORMATION TECHNOLOGY" and sem_data=="SEM VIII":
            sem=sem_data
            self.open_upload_It(sem)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM III":
            sem=sem_data
            self.open_upload_cs(sem)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM IV":
            sem=sem_data
            self.open_upload_cs(sem)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM V":
            sem=sem_data
            self.open_upload_cs(sem)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM VI":
            sem=sem_data
            self.open_upload_cs(sem)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM VII":
            sem=sem_data
            self.open_upload_cs(sem)
        elif department_data=="COMPUTER SCIENCE" and sem_data=="SEM VIII":
            sem=sem_data
            self.open_upload_cs(sem)
        elif department_data=="EXTC" and sem_data=="SEM III":
            sem=sem_data
            self.open_upload_EXTC(sem)
        elif department_data=="EXTC" and sem_data=="SEM IV":
            sem=sem_data
            self.open_upload_EXTC(sem)
        elif department_data=="EXTC" and sem_data=="SEM V":
            sem=sem_data
            self.open_upload_EXTC(sem)
        elif department_data=="EXTC" and sem_data=="SEM VI":
            sem=sem_data
            self.open_upload_EXTC(sem)
        elif department_data=="EXTC" and sem_data=="SEM VII":
            sem=sem_data
            self.open_upload_EXTC(sem)
        elif department_data=="EXTC" and sem_data=="SEM VIII":
            sem=sem_data
            self.open_upload_EXTC(sem)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM III":
            sem=sem_data
            self.open_upload_BIO_MEDICAL(sem)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM IV":
            sem=sem_data
            self.open_upload_BIO_MEDICAL(sem)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM V":
            sem=sem_data
            self.open_upload_BIO_MEDICAL(sem)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM VI":
            sem=sem_data
            self.open_upload_BIO_MEDICAL(sem)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM VII":
            sem=sem_data
            self.open_upload_BIO_MEDICAL(sem)
        elif department_data=="BIO-MEDICAL" and sem_data=="SEM VIII":
            sem=sem_data
            self.open_upload_BIO_MEDICAL(sem)
        elif department_data=="MECHANICAL" and sem_data=="SEM III":
            sem=sem_data
            self.open_upload_MECHANICAL(sem)
        elif department_data=="MECHANICAL" and sem_data=="SEM IV":
            sem=sem_data
            self.open_upload_MECHANICAL(sem)
        elif department_data=="MECHANICAL" and sem_data=="SEM V":
            sem=sem_data
            self.open_upload_MECHANICAL(sem)
        elif department_data=="MECHANICAL" and sem_data=="SEM VI":
            sem=sem_data
            self.open_upload_MECHANICAL(sem)
        elif department_data=="MECHANICAL" and sem_data=="SEM VII":
            sem=sem_data
            self.open_upload_MECHANICAL(sem)
        elif department_data=="MECHANICAL" and sem_data=="SEM VIII":
            sem=sem_data
            self.open_upload_MECHANICAL(sem)
        else:
            print("please select correct potion")

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
