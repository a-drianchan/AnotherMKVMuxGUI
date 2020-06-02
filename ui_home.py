# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeILqRUk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(972, 814)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.log = QTextEdit(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setReadOnly(True)

        self.gridLayout_4.addWidget(self.log, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_single = QWidget()
        self.tab_single.setObjectName(u"tab_single")
        self.verticalLayout = QVBoxLayout(self.tab_single)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_single_input = QGroupBox(self.tab_single)
        self.group_single_input.setObjectName(u"group_single_input")
        self.gridLayout_5 = QGridLayout(self.group_single_input)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_single_trackinfo = QLabel(self.group_single_input)
        self.label_single_trackinfo.setObjectName(u"label_single_trackinfo")

        self.gridLayout_5.addWidget(self.label_single_trackinfo, 2, 1, 1, 1)

        self.label_single_avaltrack = QLabel(self.group_single_input)
        self.label_single_avaltrack.setObjectName(u"label_single_avaltrack")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_single_avaltrack.sizePolicy().hasHeightForWidth())
        self.label_single_avaltrack.setSizePolicy(sizePolicy)
        self.label_single_avaltrack.setMinimumSize(QSize(0, 10))

        self.gridLayout_5.addWidget(self.label_single_avaltrack, 0, 1, 1, 1)

        self.list_single_avaltrack = QListWidget(self.group_single_input)
        self.list_single_avaltrack.setObjectName(u"list_single_avaltrack")
        self.list_single_avaltrack.setViewMode(QListView.ListMode)

        self.gridLayout_5.addWidget(self.list_single_avaltrack, 1, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_single_add_file = QPushButton(self.group_single_input)
        self.button_single_add_file.setObjectName(u"button_single_add_file")

        self.verticalLayout_2.addWidget(self.button_single_add_file)

        self.button_single_clear = QPushButton(self.group_single_input)
        self.button_single_clear.setObjectName(u"button_single_clear")

        self.verticalLayout_2.addWidget(self.button_single_clear)


        self.gridLayout_5.addLayout(self.verticalLayout_2, 1, 2, 1, 1)

        self.list_single_trackinfo = QListWidget(self.group_single_input)
        self.list_single_trackinfo.setObjectName(u"list_single_trackinfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.list_single_trackinfo.sizePolicy().hasHeightForWidth())
        self.list_single_trackinfo.setSizePolicy(sizePolicy1)
        self.list_single_trackinfo.setMinimumSize(QSize(0, 0))
        self.list_single_trackinfo.setMaximumSize(QSize(16777215, 140))
        self.list_single_trackinfo.setBaseSize(QSize(0, 140))

        self.gridLayout_5.addWidget(self.list_single_trackinfo, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.group_single_input)

        self.group_single_output = QGroupBox(self.tab_single)
        self.group_single_output.setObjectName(u"group_single_output")
        self.gridLayout_6 = QGridLayout(self.group_single_output)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineedit_single_ouputdir = QLineEdit(self.group_single_output)
        self.lineedit_single_ouputdir.setObjectName(u"lineedit_single_ouputdir")

        self.gridLayout_6.addWidget(self.lineedit_single_ouputdir, 2, 1, 1, 1)

        self.button_single_browse_dir = QPushButton(self.group_single_output)
        self.button_single_browse_dir.setObjectName(u"button_single_browse_dir")

        self.gridLayout_6.addWidget(self.button_single_browse_dir, 2, 2, 1, 1)

        self.label_single_outputname = QLabel(self.group_single_output)
        self.label_single_outputname.setObjectName(u"label_single_outputname")

        self.gridLayout_6.addWidget(self.label_single_outputname, 0, 0, 1, 1)

        self.label_single_outputdir = QLabel(self.group_single_output)
        self.label_single_outputdir.setObjectName(u"label_single_outputdir")

        self.gridLayout_6.addWidget(self.label_single_outputdir, 2, 0, 1, 1)

        self.lineedit_single_outputname = QLineEdit(self.group_single_output)
        self.lineedit_single_outputname.setObjectName(u"lineedit_single_outputname")

        self.gridLayout_6.addWidget(self.lineedit_single_outputname, 0, 1, 1, 2)


        self.verticalLayout.addWidget(self.group_single_output)

        self.button_sinlge_mux = QPushButton(self.tab_single)
        self.button_sinlge_mux.setObjectName(u"button_sinlge_mux")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_sinlge_mux.sizePolicy().hasHeightForWidth())
        self.button_sinlge_mux.setSizePolicy(sizePolicy2)
        self.button_sinlge_mux.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.button_sinlge_mux)

        self.tabWidget.addTab(self.tab_single, "")
        self.tab_batch = QWidget()
        self.tab_batch.setObjectName(u"tab_batch")
        self.gridLayout_3 = QGridLayout(self.tab_batch)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_4 = QGroupBox(self.tab_batch)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.button_batch_clear = QPushButton(self.groupBox_4)
        self.button_batch_clear.setObjectName(u"button_batch_clear")

        self.gridLayout_8.addWidget(self.button_batch_clear, 2, 1, 1, 1)

        self.list_batch_source1 = QListWidget(self.groupBox_4)
        self.list_batch_source1.setObjectName(u"list_batch_source1")

        self.gridLayout_8.addWidget(self.list_batch_source1, 2, 0, 1, 1)

        self.list_batch_source2 = QListWidget(self.groupBox_4)
        self.list_batch_source2.setObjectName(u"list_batch_source2")

        self.gridLayout_8.addWidget(self.list_batch_source2, 2, 2, 1, 1)

        self.lable_batch_file_count_1 = QLabel(self.groupBox_4)
        self.lable_batch_file_count_1.setObjectName(u"lable_batch_file_count_1")

        self.gridLayout_8.addWidget(self.lable_batch_file_count_1, 3, 0, 1, 1)

        self.lable_batch_file_count_2 = QLabel(self.groupBox_4)
        self.lable_batch_file_count_2.setObjectName(u"lable_batch_file_count_2")

        self.gridLayout_8.addWidget(self.lable_batch_file_count_2, 3, 2, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_batch)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_batch_source1dir = QLabel(self.groupBox_2)
        self.label_batch_source1dir.setObjectName(u"label_batch_source1dir")

        self.gridLayout.addWidget(self.label_batch_source1dir, 0, 0, 1, 1)

        self.button_batch_select_input1 = QPushButton(self.groupBox_2)
        self.button_batch_select_input1.setObjectName(u"button_batch_select_input1")
        self.button_batch_select_input1.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.button_batch_select_input1, 0, 1, 1, 1)

        self.label_batch_source2dir = QLabel(self.groupBox_2)
        self.label_batch_source2dir.setObjectName(u"label_batch_source2dir")

        self.gridLayout.addWidget(self.label_batch_source2dir, 1, 0, 1, 1)

        self.button_batch_select_input2 = QPushButton(self.groupBox_2)
        self.button_batch_select_input2.setObjectName(u"button_batch_select_input2")

        self.gridLayout.addWidget(self.button_batch_select_input2, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(731, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label_batch_outputdir = QLabel(self.groupBox_2)
        self.label_batch_outputdir.setObjectName(u"label_batch_outputdir")

        self.gridLayout.addWidget(self.label_batch_outputdir, 2, 0, 1, 1)

        self.button_batch_select_output = QPushButton(self.groupBox_2)
        self.button_batch_select_output.setObjectName(u"button_batch_select_output")

        self.gridLayout.addWidget(self.button_batch_select_output, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 2)

        self.button_batch_mux = QPushButton(self.tab_batch)
        self.button_batch_mux.setObjectName(u"button_batch_mux")
        self.button_batch_mux.setBaseSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.button_batch_mux, 5, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.tab_batch)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.list_batch_reference_1 = QListWidget(self.groupBox_3)
        self.list_batch_reference_1.setObjectName(u"list_batch_reference_1")

        self.gridLayout_7.addWidget(self.list_batch_reference_1, 1, 0, 1, 1)

        self.list_batch_reference_2 = QListWidget(self.groupBox_3)
        self.list_batch_reference_2.setObjectName(u"list_batch_reference_2")

        self.gridLayout_7.addWidget(self.list_batch_reference_2, 1, 1, 1, 1)

        self.label_batch_ref_1 = QLabel(self.groupBox_3)
        self.label_batch_ref_1.setObjectName(u"label_batch_ref_1")
        self.label_batch_ref_1.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_batch_ref_1, 0, 0, 1, 1)

        self.label_batch_ref_2 = QLabel(self.groupBox_3)
        self.label_batch_ref_2.setObjectName(u"label_batch_ref_2")
        self.label_batch_ref_2.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_batch_ref_2, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_batch, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 972, 21))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionAbout)
        self.menuSettings.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"A(nother)MKVMuxGUI", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.group_single_input.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_single_trackinfo.setText(QCoreApplication.translate("MainWindow", u"Track Info", None))
        self.label_single_avaltrack.setText(QCoreApplication.translate("MainWindow", u"Avaliable Track", None))
        self.button_single_add_file.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
        self.button_single_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.group_single_output.setTitle(QCoreApplication.translate("MainWindow", u"Output Files", None))
        self.button_single_browse_dir.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_single_outputname.setText(QCoreApplication.translate("MainWindow", u"Output Name:", None))
        self.label_single_outputdir.setText(QCoreApplication.translate("MainWindow", u"Output Directory:", None))
        self.button_sinlge_mux.setText(QCoreApplication.translate("MainWindow", u"Mux", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_single), QCoreApplication.translate("MainWindow", u"MKV Mux", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"File Matching", None))
        self.button_batch_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lable_batch_file_count_1.setText(QCoreApplication.translate("MainWindow", u"File Count:", None))
        self.lable_batch_file_count_2.setText(QCoreApplication.translate("MainWindow", u"File Count:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Input Settings", None))
        self.label_batch_source1dir.setText(QCoreApplication.translate("MainWindow", u"Source 1 Directory", None))
        self.button_batch_select_input1.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_batch_source2dir.setText(QCoreApplication.translate("MainWindow", u"Source 2 Directory", None))
        self.button_batch_select_input2.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_batch_outputdir.setText(QCoreApplication.translate("MainWindow", u"Output Directory", None))
        self.button_batch_select_output.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.button_batch_mux.setText(QCoreApplication.translate("MainWindow", u"Mux", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Reference Settings", None))
        self.label_batch_ref_1.setText(QCoreApplication.translate("MainWindow", u"No file loaded", None))
        self.label_batch_ref_2.setText(QCoreApplication.translate("MainWindow", u"No file loaded", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_batch), QCoreApplication.translate("MainWindow", u"Directory Mux", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

