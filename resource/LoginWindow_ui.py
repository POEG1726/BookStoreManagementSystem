# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PrimaryPushButton)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1250, 809)
        Form.setMinimumSize(QSize(700, 500))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/images/BookStoreBackground.jpg"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(360, 0))
        self.widget.setMaximumSize(QSize(360, 16777215))
        self.widget.setStyleSheet(u"QLabel{\n"
"	font: 13px 'Microsoft YaHei'\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(100, 100))
        self.label_2.setMaximumSize(QSize(100, 100))
        self.label_2.setPixmap(QPixmap(u":/images/bookstore.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_5 = BodyLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.lineEdit_3 = LineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.label_6 = BodyLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.lineEdit_4 = LineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.lineEdit_4.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.pushButton = PrimaryPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalSpacer_6 = QSpacerItem(20, 6, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.pushButton_2 = PrimaryPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Email", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"example@example.com", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Password", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Log in", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Register", None))
    # retranslateUi

