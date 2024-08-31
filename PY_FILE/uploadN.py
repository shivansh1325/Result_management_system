

import source_2,pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import mysql.connector as mc
import openpyxl



class Ui_MainWindow(object):
    def message(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def show_data(self,url):
        self.uurl=url
        data=pd.read_excel(url,sheet_name=0)
        if data.size==0:
            print("nothing")
        data.fillna("", inplace=True)
        self.tableWidget.setRowCount(data.shape[0])
        self.tableWidget.setColumnCount(data.shape[1])
        # self.tableWidget.setHorizontalHeaderLabels(data.columns)
        self.tableWidget.setVerticalHeaderLabels(data.index.astype(str))

        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                cell_value = str(data.iloc[i,j])
                table_item = QtWidgets.QTableWidgetItem(cell_value)
                if pd.api.types.is_list_like(data.iloc[i, j]):
                    merge_info = data.iloc[i, j]
                    merge_rows, merge_cols = merge_info
                    for p in range(i, i + merge_rows):
                        for q in range(j, j + merge_cols):
                            if p == i and q == j:
                                continue
                            self.tableWidget.setItem(p, q, QtWidgets.QTableWidgetItem(""))
                    self.tableWidget.setSpan(i, j, merge_rows, merge_cols)
                self.tableWidget.setItem(i, j, table_item)
        




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/source/pencil_logo.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_frame = QtWidgets.QFrame(self.centralwidget)
        self.bg_frame.setGeometry(QtCore.QRect(0, 0, 1080, 721))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bg_frame.sizePolicy().hasHeightForWidth())
        self.bg_frame.setSizePolicy(sizePolicy)
        self.bg_frame.setMaximumSize(QtCore.QSize(1080, 721))
        self.bg_frame.setStyleSheet("QFrame#bg_frame{\n"
                                    "    background-color: rgb(170, 170, 255);\n"
                                    "}")
        self.bg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg_frame.setObjectName("bg_frame")
        self.download_btn = QtWidgets.QCommandLinkButton(self.bg_frame)
        self.download_btn.setGeometry(QtCore.QRect(440, 660, 190, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.download_btn.sizePolicy().hasHeightForWidth())
        self.download_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.download_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/source/dowload_logo.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_btn.setIcon(icon1)
        self.download_btn.setIconSize(QtCore.QSize(35, 35))
        self.download_btn.setObjectName("download_btn")
        self.download_btn.clicked.connect(self.download_file)
        self.upload_btn = QtWidgets.QCommandLinkButton(self.bg_frame)
        self.upload_btn.setGeometry(QtCore.QRect(20, 650, 250, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.upload_btn.sizePolicy().hasHeightForWidth())
        self.upload_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.upload_btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/src/source/import_logo.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_btn.setIcon(icon2)
        self.upload_btn.setIconSize(QtCore.QSize(50, 50))
        self.upload_btn.setObjectName("upload_btn")
        self.upload_btn.clicked.connect(self.upload_file)
        self.save_btn = QtWidgets.QCommandLinkButton(self.bg_frame)
        self.save_btn.setGeometry(QtCore.QRect(840, 660, 185, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/src/source/save_btn.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon3)
        # self.save_btn.clicked.connect(self.save_file)
        self.save_btn.setIconSize(QtCore.QSize(30, 30))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.save_file)
        self.tableWidget = QtWidgets.QTableWidget(self.bg_frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1061, 621))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeIncrement(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
                                       "border-style: outset;\n"
                                       "border-width:5px;\n"
                                       "border-radius: 10px;\n"
                                       "    border-color: rgb(230, 107, 255);\n"
                                       "}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enter Details"))
        self.download_btn.setText(_translate("MainWindow", "DOWNLOAD"))
        self.upload_btn.setText(_translate("MainWindow", "UPLOAD"))
        self.save_btn.setText(_translate("MainWindow", "SAVE"))
        self.mydb = mc.connect(
                host="localhost",
                user="root",
                password="root",
                database="result_management_system"
            )

    def download_file(self):
        file_name, _ = QFileDialog.getSaveFileName(None, 'Save Excel File', '', 'Excel Files (*.xlsx *.xls)')
        if file_name:
            try:
                df = pd.DataFrame()
                for row in range(self.tableWidget.rowCount()):
                    df_row = []
                    for col in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, col)
                        if item:
                            df_row.append(item.text())
                        else:
                            df_row.append('')
                    df = df.append(pd.Series(df_row), ignore_index=True)

                df.to_excel(file_name, index=False)
                self.message("CONGRATULATION!!","YOUR FILE IS BEAN SAVED!!")

            except Exception as e:
                print(e)
    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Upload Excel File", "", "Excel Files (*.xlsx)")
        if not file_path:
            return

        df = pd.read_excel(file_path)

        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        self.tableWidget.setVerticalHeaderLabels(df.index.astype(str))
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(df.iloc[i, j]))
                self.tableWidget.setItem(i, j, item)

    def save_file(self):
        try:
            print("hi")
        

            data = []
            for row in range(self.tableWidget.rowCount()):
                data.append([])
                for column in range(self.tableWidget.columnCount()):
                    data[row].append(self.tableWidget.item(row, column).text())

            df = pd.DataFrame(data)
            sheet_name, ok = QtWidgets.QInputDialog.getText(None, "Sheet Name", "Enter the sheet name:", QtWidgets.QLineEdit.Normal)
            if not ok:
                # pass
                sheet_name="2"

            excel_df = pd.read_excel(self.uurl, index_col=None)
            with pd.ExcelWriter(self.uurl, engine='openpyxl', mode='a') as writer:
                try:
                    writer.book = openpyxl.load_workbook(self.uurl)
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                except FileNotFoundError:
                    df.to_excel(writer, sheet_name=sheet_name, index=False)

                # df.to_excel(writer, sheet_name="hello", index=False)
            # # Append the new DataFrame to the existing one
            # merged_df = excel_df.append(df, ignore_index=True)
            # merged_df.to_excel(self.uurl, index=False)
            print("done")
            self.message("CONGRATULATION!!","YOUR CHANGES IS BEAN SAVED!!")

        except mc.Error as e:
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
