# -*- coding: utf-8 -*-
'''
    该文件为可视化界面定义文件,设置基本布局样式及功能响应
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
import numpy as np

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 888)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1071, 891))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 0, 130, 71))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 981, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 130, 71))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 690, 130, 71))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(200, 690, 130, 71))
        self.label_4.setObjectName("label_4")

        font = QtGui.QFont()
        font.setPointSize(18)
        # font.setBold(True)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.lineEdit.setFont(font)

        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(250, 760, 571, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(40, 180, 981, 511))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 171, 61))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 60, 741, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 120, 1001, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(790, 60, 241, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 170, 291, 61))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 350, 1001, 51))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 290, 741, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(790, 290, 241, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(30, 220, 251, 61))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 230, 871, 51))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 420, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")

        # 为按钮绑定功能函数
        self.pushButton_2.clicked.connect(self.uploadfile)  # 选择新闻excel文件
        self.pushButton_3.clicked.connect(self.preview)       # 预览excel文件
        self.pushButton_4.clicked.connect(self.choosefile)  # 设置输出文件路径
        self.pushButton_5.clicked.connect(self.clear)       # 清空选择

        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(30, 490, 1001, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")

        # 设置背景图片
        self.tabWidget.setStyleSheet("background-image: url(./resources/background.png);")  # 设置背景图片

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "新闻智分系统"))
        Form.setWindowIcon(QIcon('resources//logo.ico'))
        self.label.setText(_translate("Form", "新闻标题："))
        self.label_2.setText(_translate("Form", "新闻正文："))
        self.label_3.setText(_translate("Form", "新闻类别："))
        self.label_4.setText(_translate("Form", "无"))
        self.pushButton.setText(_translate("Form", "进行新闻文本分类"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "          单条新闻文本分类          "))
        self.label_5.setText(_translate("Form", "批量导入新闻："))
        self.pushButton_2.setText(_translate("Form", "选择要进行分类的新闻Excel文件"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "选择的Excel文件路径"))
        self.pushButton_3.setText(_translate("Form", "预览文件"))
        self.label_6.setText(_translate("Form", "设置结果文件输出路径："))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "结果文件输出路径"))
        self.pushButton_4.setText(_translate("Form", "选择输出文件夹"))
        self.pushButton_5.setText(_translate("Form", "清空选择"))
        self.label_7.setText(_translate("Form", "文件名称："))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "输出文件名称"))
        self.pushButton_6.setText(_translate("Form", "进行新闻文本分类"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "           批量新闻文本分类          "))
        self.label.setStyleSheet("background: transparent;")
        self.label_2.setStyleSheet("background: transparent;")
        self.label_3.setStyleSheet("background: transparent;")
        self.label_4.setStyleSheet("background: transparent;")
        self.label_5.setStyleSheet("background: transparent;")
        self.label_6.setStyleSheet("background: transparent;")
        self.label_7.setStyleSheet("background: transparent;")
        self.lineEdit.setStyleSheet("background: transparent;")
        self.textEdit.setStyleSheet("background: transparent;")
        self.lineEdit_2.setStyleSheet("background: transparent;")
        self.lineEdit_3.setStyleSheet("background: transparent;")
        self.lineEdit_4.setStyleSheet("background: transparent;")
        self.tableWidget.setStyleSheet("background: transparent;")

        self.pushButton.setStyleSheet(
            '''QPushButton{background:#AFEEEE;border-radius:5px;}QPushButton:hover{background:#00FFFF;}''')
        self.pushButton_2.setStyleSheet(
            '''QPushButton{background:#AFEEEE;border-radius:5px;}QPushButton:hover{background:#00FFFF;}''')
        self.pushButton_3.setStyleSheet(
            '''QPushButton{background:#AFEEEE;border-radius:5px;}QPushButton:hover{background:#00FFFF;}''')
        self.pushButton_4.setStyleSheet(
            '''QPushButton{background:#AFEEEE;border-radius:15px;}QPushButton:hover{background:#00FFFF;}''')
        self.pushButton_5.setStyleSheet(
            '''QPushButton{background:#AFEEEE;border-radius:15px;}QPushButton:hover{background:#00FFFF;}''')
        self.pushButton_6.setStyleSheet(
            '''QPushButton{background:#AFEEEE;border-radius:15px;}QPushButton:hover{background:#00FFFF;}''')
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)

    # 添加功能函数:
    # 选择excel文件
    def uploadfile(self, Filepath):
        x, _ = QtWidgets.QFileDialog.getOpenFileName(None, "选取excel文件", "./", "*.xlsx")
        self.lineEdit_2.setText(x)

    # 预览excel文件
    def preview(self):
        excelFilepath = self.lineEdit_2.text()
        if excelFilepath == '':
            QMessageBox().warning(None, "警告", "请先选择要进行分类的Excel文件！", QMessageBox.Close)
        else:
            input_table = pd.read_excel(excelFilepath)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
            input_table_header = input_table.columns.values.tolist()

            ###===========读取表格，转换表格，============================================
            ###======================给tablewidget设置行列表头============================
            self.tableWidget.setColumnCount(input_table_colunms)
            self.tableWidget.setRowCount(input_table_rows)
            self.tableWidget.setHorizontalHeaderLabels(input_table_header)
            # 自定义分配列宽
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
            ###======================给tablewidget设置行列表头============================

            ###================遍历表格每个元素，同时添加到tablewidget中========================
            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                #print(input_table_rows_values)
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
        ###==============将遍历的元素添加到tablewidget中并显示=======================
                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items) 
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.tableWidget.setItem(i, j, newItem)  
        ###================遍历表格每个元素，同时添加到tablewidget中========================

    # 设置输出路径
    def choosefile(self, Filepath):
        # 选择输出路径
        f = QtWidgets.QFileDialog.getExistingDirectory(None, "选择输出文件夹", "./")  # 起始路径
        # 输出文件名称
        filename = self.lineEdit_4.text()
        if filename.endswith('.xlsx'):
            filename = filename[:-5]
        else:
            filename = filename
        if filename == '':
            QMessageBox().warning(None, "警告", "请先补全输出文件名称！", QMessageBox.Close)
        else:
            f += '/'
            f += filename
            f += '.xlsx'   # 后续此处需要添加支持其他的格式
            self.lineEdit_3.setText(f)

    # 清空输出文件路径
    def clear(self):
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')

    # 警告与提示
    def warn1(self):
        QMessageBox().warning(None, "警告", "新闻内容不能为空！", QMessageBox.Close)

    def warn2(self):
        QMessageBox().warning(None, "警告", "未选择要进行分类的新闻Excel文件！", QMessageBox.Close)

    def warn3(self):
        QMessageBox().warning(None, "警告", "未设置结果文件输出路径！", QMessageBox.Close)

    def success1(self):
        QMessageBox().information(None, "提示", "单条新闻文本分类完成！", QMessageBox.Close)

    def success2(self):
        QMessageBox().information(None, "提示", "批量新闻文本分类完成！", QMessageBox.Close)

    # 展示输出预测结果
    def showresult(self):
        excelFilepath = self.lineEdit_3.text()
        if excelFilepath == '':
            QMessageBox().warning(None, "警告", "请先设置结果文件输出路径！", QMessageBox.Close)
        else:
            input_table = pd.read_excel(excelFilepath)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
            input_table_header = input_table.columns.values.tolist()

            ###===========读取表格，转换表格，============================================
            ###======================给tablewidget设置行列表头============================
            self.tableWidget.setColumnCount(input_table_colunms)
            self.tableWidget.setRowCount(input_table_rows)
            self.tableWidget.setHorizontalHeaderLabels(input_table_header)
            # 自定义分配列宽
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
            ###======================给tablewidget设置行列表头============================

            ###================遍历表格每个元素，同时添加到tablewidget中========================
            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                #print(input_table_rows_values)
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
        ###==============将遍历的元素添加到tablewidget中并显示=======================
                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items) 
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.tableWidget.setItem(i, j, newItem)  
        ###================遍历表格每个元素，同时添加到tablewidget中========================


