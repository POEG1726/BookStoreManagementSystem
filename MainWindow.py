# coding:utf-8
"""
Online Bookstore Management System
----------------------------------
Developed by: Yiwei Lyu
GitHub: https://github.com/POEG1726
GitHub Repository: https://github.com/POEG1726/BookStoreManagementSystem

This Online Bookstore Management System is designed to facilitate the management and purchase of books online. 
It features a responsive and accessible user interface developed with PySide6 and Python 3.9, alongside a backend 
leveraging JSON for efficient data storage and retrieval. This system allows users to browse, search, and purchase 
books and provides administrators with tools to manage inventory, orders, and customer information efficiently.

Technical Stack:
- Frontend: PySide6 with QFluentWidgets, ensuring a smooth graphical user interface.
- Backend:  Python 3.9, handling logic for user management, data inquiry, and order processing.
- Database: JSON files used for storing data related to books, users, and transactions.

Usage:
Run `MainWindow.py` to launch the application. Ensure all dependencies are installed as per the README instructions.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QMessageBox,
)
from qfluentwidgets import FluentBackgroundTheme
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import FluentWindow, SplitTitleBar, setThemeColor
from qframelesswindow import FramelessWindow as Window

from Backend import *
from Cart import CartInterface
from Home import HomeInterface
from Management import ManagementInterface
from WindowUI import Login_Ui_Form, Register_Ui_Form


class LoginWindow(Window, Login_Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
        setThemeColor("#28afe9")
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.label.setScaledContents(False)
        self.setWindowTitle("Book Store -Login")
        self.resize(1000, 650)
        color = QColor(240, 244, 249)
        self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def bind(self):
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.registration)
        self.lineEdit_4.returnPressed.connect(self.login)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap(":/images/resource/images/BookStoreBackground.jpg").scaled(
            self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
        )
        self.label.setPixmap(pixmap)

    def login(self):
        email = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        res = authorization(email, password)
        if res[0]:
            QMessageBox.information(self, "Login Success", "You are logged in!")
            Main = Window(user_id=res[1])
            Main.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect email or password.")

    def registration(self):
        tmp = register()
        tmp.show()
        self.close()


class register(Window, Register_Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        setThemeColor("#28afe9")
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()
        self.label.setScaledContents(False)
        self.setWindowTitle("Book Store -Registration")
        self.resize(1000, 650)
        color = QColor(240, 244, 249)
        self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")
        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.pushButton_2.clicked.connect(self.reg)
        self.lineEdit_4.returnPressed.connect(self.reg)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap(":/images/resource/images/BookStoreBackground.jpg").scaled(
            self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
        )
        self.label.setPixmap(pixmap)

    def reg(self):
        name = self.lineEdit.text()
        email = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        res = add_user(name=name, email=email, password=password)
        if res:
            QMessageBox.information(
                self, "Registration", "Registration successful! Logging you in..."
            )
            Main = Window(user_id=res[1])
            Main.show()
            self.close()
            return
        else:
            QMessageBox.warning(self, "User is already existed!")
        self.close()  # Close the registration window


class Widget(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setStyleSheet(
            """font-size: 30px;
color: green;"""
        )
        self.hBoxLayout = QHBoxLayout(self)
        # setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(" ", "-"))


class Window(FluentWindow):

    def __init__(self, user_id: str):
        super().__init__()

        # create sub interface
        self.user = look_up_user(user_id=user_id)
        self.homeInterface = HomeInterface(self)
        self.cartInterface = CartInterface(self)
        self.managementInterface = ManagementInterface(self)
        self.initNavigation()
        self.initWindow()
        self.stackedWidget.currentChanged.connect(self.reload_page)

    def reload_page(self, index):
        if index == 1:
            self.cartInterface.reload()
            self.homeInterface.reload()
        # if index == 2:
        #     if self.user['permission'] == 'user':
        #     self.managementInterface.reload()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, "Home")
        self.addSubInterface(self.cartInterface, FIF.SHOPPING_CART, "Cart")
        if self.user["permission"] == "admin":
            self.addSubInterface(self.managementInterface, FIF.SETTING, "Management")
        else:
            self.addSubInterface(
                Widget("You Are Not Admin!!!", self), FIF.SETTING, "Management"
            )

    def initWindow(self):
        # self.resize(940, 700)
        self.setFixedSize(940,700)
        self.setWindowTitle(f"Book Store     User: {self.user['email']}")
        # self.setWindowIcon(QI)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.setCustomBackgroundColor(*FluentBackgroundTheme.DEFAULT_BLUE)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    debug = False
    if debug == True:
        Main = Window(user_id="0008bc60")
        Main.show()
    else:
        login = LoginWindow()
        login.show()
    app.exec()
