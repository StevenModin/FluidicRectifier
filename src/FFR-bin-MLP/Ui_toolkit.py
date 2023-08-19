# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toolkit.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(782, 432)
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.TitleLable = QLabel(Form)
        self.TitleLable.setObjectName(u"TitleLable")
        self.TitleLable.setGeometry(QRect(50, 90, 201, 31))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        self.TitleLable.setFont(font)
        self.TitleLable.setTextFormat(Qt.AutoText)
        self.TitleLable.setAlignment(Qt.AlignCenter)
        self.TitleLable.setIndent(0)
        self.pathEdit_1 = QLineEdit(Form)
        self.pathEdit_1.setObjectName(u"pathEdit_1")
        self.pathEdit_1.setGeometry(QRect(30, 60, 221, 20))
        self.pathButton_1 = QPushButton(Form)
        self.pathButton_1.setObjectName(u"pathButton_1")
        self.pathButton_1.setGeometry(QRect(250, 60, 21, 21))
        self.noticeLabel_1 = QLabel(Form)
        self.noticeLabel_1.setObjectName(u"noticeLabel_1")
        self.noticeLabel_1.setGeometry(QRect(30, 30, 241, 21))
        self.resultLabel = QLabel(Form)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setGeometry(QRect(40, 380, 221, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.resultLabel.setFont(font1)
        self.resultLabel.setLayoutDirection(Qt.LeftToRight)
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 130, 241, 201))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textLabel_1 = QLabel(self.layoutWidget)
        self.textLabel_1.setObjectName(u"textLabel_1")
        font2 = QFont()
        font2.setPointSize(10)
        self.textLabel_1.setFont(font2)
        self.textLabel_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.textLabel_1)

        self.textLabel_2 = QLabel(self.layoutWidget)
        self.textLabel_2.setObjectName(u"textLabel_2")
        self.textLabel_2.setFont(font2)
        self.textLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.textLabel_2)

        self.textLabel_3 = QLabel(self.layoutWidget)
        self.textLabel_3.setObjectName(u"textLabel_3")
        self.textLabel_3.setFont(font2)
        self.textLabel_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.textLabel_3)

        self.textLabel_4 = QLabel(self.layoutWidget)
        self.textLabel_4.setObjectName(u"textLabel_4")
        self.textLabel_4.setFont(font2)
        self.textLabel_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.textLabel_4)

        self.textLabel_5 = QLabel(self.layoutWidget)
        self.textLabel_5.setObjectName(u"textLabel_5")
        self.textLabel_5.setFont(font2)
        self.textLabel_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.textLabel_5)

        self.textLabel_6 = QLabel(self.layoutWidget)
        self.textLabel_6.setObjectName(u"textLabel_6")
        self.textLabel_6.setFont(font2)
        self.textLabel_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.textLabel_6)

        self.textLabel_7 = QLabel(self.layoutWidget)
        self.textLabel_7.setObjectName(u"textLabel_7")
        self.textLabel_7.setFont(font2)
        self.textLabel_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.textLabel_7)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_1 = QLineEdit(self.layoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.verticalLayout.addWidget(self.lineEdit_1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout.addWidget(self.lineEdit_7)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(300, 60, 451, 261))
        self.TitleLable_2 = QLabel(Form)
        self.TitleLable_2.setObjectName(u"TitleLable_2")
        self.TitleLable_2.setGeometry(QRect(450, 30, 151, 21))
        self.TitleLable_2.setFont(font)
        self.TitleLable_2.setTextFormat(Qt.AutoText)
        self.TitleLable_2.setAlignment(Qt.AlignCenter)
        self.TitleLable_2.setIndent(0)
        self.pathEdit_2 = QLineEdit(Form)
        self.pathEdit_2.setObjectName(u"pathEdit_2")
        self.pathEdit_2.setGeometry(QRect(300, 320, 431, 20))
        self.pathButton_2 = QPushButton(Form)
        self.pathButton_2.setObjectName(u"pathButton_2")
        self.pathButton_2.setGeometry(QRect(730, 320, 21, 21))
        self.noticeLabel_2 = QLabel(Form)
        self.noticeLabel_2.setObjectName(u"noticeLabel_2")
        self.noticeLabel_2.setGeometry(QRect(300, 340, 361, 21))
        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 350, 201, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.classButton = QPushButton(self.layoutWidget1)
        self.classButton.setObjectName(u"classButton")

        self.horizontalLayout_3.addWidget(self.classButton)

        self.clearButton_1 = QPushButton(self.layoutWidget1)
        self.clearButton_1.setObjectName(u"clearButton_1")

        self.horizontalLayout_3.addWidget(self.clearButton_1)

        self.layoutWidget2 = QWidget(Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(300, 370, 451, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.batchButton = QPushButton(self.layoutWidget2)
        self.batchButton.setObjectName(u"batchButton")

        self.horizontalLayout_2.addWidget(self.batchButton)

        self.clearButton_2 = QPushButton(self.layoutWidget2)
        self.clearButton_2.setObjectName(u"clearButton_2")

        self.horizontalLayout_2.addWidget(self.clearButton_2)

        self.saveButton = QPushButton(self.layoutWidget2)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.saveToButton = QPushButton(self.layoutWidget2)
        self.saveToButton.setObjectName(u"saveToButton")

        self.horizontalLayout_2.addWidget(self.saveToButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"RFR Tool", None))
        self.TitleLable.setText(QCoreApplication.translate("Form", u"Single Group Data Process", None))
        self.pathEdit_1.setText(QCoreApplication.translate("Form", u"add a file or load from default path", None))
        self.pathButton_1.setText(QCoreApplication.translate("Form", u"...", None))
        self.noticeLabel_1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.resultLabel.setText(QCoreApplication.translate("Form", u"TBD.", None))
        self.textLabel_1.setText(QCoreApplication.translate("Form", u"Pressure", None))
        self.textLabel_2.setText(QCoreApplication.translate("Form", u"Width", None))
        self.textLabel_3.setText(QCoreApplication.translate("Form", u"Gap", None))
        self.textLabel_4.setText(QCoreApplication.translate("Form", u"Lap length", None))
        self.textLabel_5.setText(QCoreApplication.translate("Form", u"Valve length", None))
        self.textLabel_6.setText(QCoreApplication.translate("Form", u"Bending angle", None))
        self.textLabel_7.setText(QCoreApplication.translate("Form", u"Twisting angle", None))
        self.TitleLable_2.setText(QCoreApplication.translate("Form", u"Batch Processing", None))
        self.pathEdit_2.setText(QCoreApplication.translate("Form", u"Click button to load a dateset ...", None))
        self.pathButton_2.setText(QCoreApplication.translate("Form", u"...", None))
        self.noticeLabel_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.classButton.setText(QCoreApplication.translate("Form", u"Classify", None))
        self.clearButton_1.setText(QCoreApplication.translate("Form", u"clear", None))
        self.batchButton.setText(QCoreApplication.translate("Form", u"Process", None))
        self.clearButton_2.setText(QCoreApplication.translate("Form", u"Clear data", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.saveToButton.setText(QCoreApplication.translate("Form", u"Save to ...", None))
    # retranslateUi

