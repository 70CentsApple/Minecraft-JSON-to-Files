# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import QSize, QCoreApplication, QMetaObject
from PySide2.QtGui import QFont,QIcon,QCursor,Qt
from PySide2.QtWidgets import QGridLayout,QLabel,QWidget,QSplitter,QPushButton


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(654, 392)
        font = QFont()
        font.setFamily(u"Microsoft YaHei")
        Main.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(654, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.bt_obj = QPushButton(self.splitter)
        self.bt_obj.setObjectName(u"bt_obj")
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei")
        font1.setPointSize(15)
        self.bt_obj.setFont(font1)
        self.bt_obj.setCursor(QCursor(Qt.PointingHandCursor))
        self.splitter.addWidget(self.bt_obj)
        self.bt_json = QPushButton(self.splitter)
        self.bt_json.setObjectName(u"bt_json")
        self.bt_json.setFont(font1)
        self.bt_json.setCursor(QCursor(Qt.PointingHandCursor))
        self.splitter.addWidget(self.bt_json)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.lb_obj = QLabel(self.splitter_2)
        self.lb_obj.setObjectName(u"lb_obj")
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei")
        font2.setPointSize(12)
        self.lb_obj.setFont(font2)
        self.splitter_2.addWidget(self.lb_obj)
        self.lb_json = QLabel(self.splitter_2)
        self.lb_json.setObjectName(u"lb_json")
        self.lb_json.setFont(font2)
        self.splitter_2.addWidget(self.lb_json)

        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.lb_disk = QLabel(self.centralwidget)
        self.lb_disk.setObjectName(u"lb_disk")
        font3 = QFont()
        font3.setFamily(u"Microsoft YaHei")
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.lb_disk.setFont(font3)
        self.lb_disk.setCursor(QCursor(Qt.ArrowCursor))
        self.lb_disk.setLayoutDirection(Qt.LeftToRight)
        self.lb_disk.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_disk, 2, 0, 1, 1)

        self.lb_path = QLabel(self.centralwidget)
        self.lb_path.setObjectName(u"lb_path")
        font4 = QFont()
        font4.setFamily(u"Microsoft YaHei")
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setWeight(50)
        font4.setKerning(True)
        self.lb_path.setFont(font4)
        self.lb_path.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_path, 3, 0, 1, 1)

        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.bt_out = QPushButton(self.splitter_3)
        self.bt_out.setObjectName(u"bt_out")
        self.bt_out.setFont(font1)
        self.bt_out.setCursor(QCursor(Qt.PointingHandCursor))
        self.splitter_3.addWidget(self.bt_out)
        self.bt_start = QPushButton(self.splitter_3)
        self.bt_start.setObjectName(u"bt_start")
        font5 = QFont()
        font5.setFamily(u"Microsoft YaHei")
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setWeight(75)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.bt_start.setFont(font5)
        self.bt_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.splitter_3.addWidget(self.bt_start)

        self.gridLayout.addWidget(self.splitter_3, 4, 0, 1, 1)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)

    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Minecraft Json Converter by 70CentsApple", None))
        self.bt_obj.setText(QCoreApplication.translate("Main", u"\u9009\u62e9objects\u6587\u4ef6\u5939", None))
        self.bt_json.setText(
            QCoreApplication.translate("Main", u"\u9009\u62e9indexes\u4e0b\u7248\u672cjson\u6587\u4ef6", None))
        self.lb_obj.setText(QCoreApplication.translate("Main", u".minecraft\\assets\\objects", None))
        self.lb_json.setText(QCoreApplication.translate("Main", u".minecraft\\assets\\indexes\\*.json", None))
        self.lb_disk.setText(QCoreApplication.translate("Main",
                                                        u"\u8bf7\u6839\u636e\u4e0a\u8ff0\u63d0\u793a\u5b8c\u6210\u64cd\u4f5c(/\u2267\u25bd\u2266)/",
                                                        None))
        self.lb_path.setText("")
        self.bt_out.setText(
            QCoreApplication.translate("Main", u"\u9009\u62e9\u8f93\u51fa\u6587\u4ef6\u8def\u5f84", None))
        self.bt_start.setText(QCoreApplication.translate("Main", u"\u5f00\u59cb\u64cd\u4f5c", None))
    # retranslateUi
