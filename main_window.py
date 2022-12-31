# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QMainWindow, QMenuBar, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setMaximumSize(QSize(420, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.tableView = QTableView(self.frame_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableView)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame { background-color: rgb(255, 255, 255); }")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.recipeTitle = QLabel(self.frame)
        self.recipeTitle.setObjectName(u"recipeTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.recipeTitle.sizePolicy().hasHeightForWidth())
        self.recipeTitle.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.recipeTitle.setFont(font)
        self.recipeTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.recipeTitle)

        self.recipeAuthor = QLabel(self.frame)
        self.recipeAuthor.setObjectName(u"recipeAuthor")
        font1 = QFont()
        font1.setItalic(True)
        self.recipeAuthor.setFont(font1)
        self.recipeAuthor.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.recipeAuthor)

        self.verticalSpacer = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.recipeDescription = QLabel(self.frame)
        self.recipeDescription.setObjectName(u"recipeDescription")
        sizePolicy1.setHeightForWidth(self.recipeDescription.sizePolicy().hasHeightForWidth())
        self.recipeDescription.setSizePolicy(sizePolicy1)
        self.recipeDescription.setWordWrap(True)

        self.verticalLayout.addWidget(self.recipeDescription)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 8, -1, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 16, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setBold(True)
        self.label.setFont(font2)

        self.verticalLayout_3.addWidget(self.label)

        self.recipeIngredientList = QListView(self.frame)
        self.recipeIngredientList.setObjectName(u"recipeIngredientList")
        self.recipeIngredientList.setSelectionMode(QAbstractItemView.NoSelection)
        self.recipeIngredientList.setSpacing(4)
        self.recipeIngredientList.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.recipeIngredientList)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_2)

        self.recipeInstructionList = QListView(self.frame)
        self.recipeInstructionList.setObjectName(u"recipeInstructionList")
        self.recipeInstructionList.setFocusPolicy(Qt.NoFocus)
        self.recipeInstructionList.setSelectionMode(QAbstractItemView.NoSelection)
        self.recipeInstructionList.setSpacing(8)
        self.recipeInstructionList.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.recipeInstructionList)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.recipeTitle.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.recipeAuthor.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.recipeDescription.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingredients", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Instructions", None))
    # retranslateUi

