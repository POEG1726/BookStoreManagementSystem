from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
)
from qfluentwidgets import (
    ComboBox,
    DoubleSpinBox,
    FluentIcon,
    LineEdit,
    PushButton,
    TableWidget,
    ToolButton,
)
from qframelesswindow import FramelessWindow as Window

from Backend import *


class PopupBox_User(Window):
    refreshSignal = Signal()

    def __init__(self, user_id, parent=None, mode="Update"):
        super().__init__()

        self.parent = parent
        # print(type(parent),type(self.parent))
        self.setStyleSheet(
            """PopupBox_User {
    background-color: rgba(255, 255, 255, 0.667);
}"""
        )
        self.user_id = user_id
        self.mode = mode
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.setSpacing(7)
        self.setFixedSize(QSize(400, 500))

        self.UserNameLabel = QLabel(self)
        self.UserNameLineEdit = LineEdit(self)
        self.UserEmailLabel = QLabel(self)
        self.UserEmailLineEdit = LineEdit(self)
        self.UserPermissionLabel = QLabel(self)
        self.UserPermissionComboBox = ComboBox(self)
        self.UserCartLabel = QLabel(self)
        self.UserCartTable = TableWidget(self)
        self.SaveChangeButton = PushButton(FluentIcon.SAVE, "SAVE")
        self.DeleteUserButton = PushButton(FluentIcon.DELETE, "DELETE")
        self.CancelButton = PushButton(FluentIcon.CANCEL, "CANCEL")

        self.__initWidgets()
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.bind()
        if self.mode == "Update":
            self.loaddata()
        # else:
        #     self.user_id = generate_id()

    def __initWidgets(self, parent=None):
        self.UserCartTable.setStyleSheet(
            """QTableView {
    background: transparent;
    outline: none;
    selection-background-color: transparent;
    alternate-background-color: transparent;
    background-color: rgba(255, 255, 255, 0.667);
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}
QTableView::item {
    background: transparent;
    border: 0px;
    padding-left: 16px;
    padding-right: 16px;
    height: 35px;
}
QTableView::indicator {
    width: 18px;
    height: 18px;
    border-radius: 5px;
    border: none;
    background-color: transparent;
}
QHeaderView {
    background-color: transparent;
}
QHeaderView::section {
    background-color: transparent;
    color: rgb(96, 96, 96);
    padding-left: 5px;
    padding-right: 5px;
    border: 1px solid rgba(0, 0, 0, 15);
    font: 13px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
}
QHeaderView::section:horizontal {
    border-left: none;
    height: 33px;
}
QTableView, QHeaderView::section:horizontal {
    border-top: none;
}
QHeaderView::section:horizontal:last {
    border-right: none;
}

QHeaderView::section:vertical {
    border-top: none;
}

QHeaderView::section:checked {
    background-color: transparent;
}

QHeaderView::down-arrow {
    subcontrol-origin: padding;
    subcontrol-position: center right;
    margin-right: 6px;
    image: url(:/qfluentwidgets/images/table_view/Down_black.svg);
}

QHeaderView::up-arrow {
    subcontrol-origin: padding;
    subcontrol-position: center right;
    margin-right: 6px;
    image: url(:/qfluentwidgets/images/table_view/Up_black.svg);
}

QTableCornerButton::section {
    background-color: transparent;
    border: 1px solid rgba(0, 0, 0, 15);
}

QTableCornerButton::section:pressed {
    background-color: rgba(0, 0, 0, 12);
}"""
        )
        self.UserNameLineEdit.setClearButtonEnabled(True)
        self.UserEmailLineEdit.setClearButtonEnabled(True)

        self.UserNameLabel.setText("User Name:")
        self.UserEmailLabel.setText("User Email:")
        self.UserPermissionLabel.setText("User Permission:")
        self.UserCartLabel.setText("User Cart:")

        # self.UserNameLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        # self.UserEmailLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        # self.UserPermissionLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        # self.UserCartLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.UserNameLabel.setFixedWidth(100)
        self.UserEmailLabel.setFixedWidth(100)
        self.UserPermissionLabel.setFixedWidth(100)
        self.UserCartLabel.setFixedWidth(100)

        self.UserPermissionComboBox.addItems(["user", "admin"])

        self.UserCartTable.setColumnCount(3)
        self.UserCartTable.setHorizontalHeaderLabels(["Book Name", "Quantity", "Del"])
        self.UserCartTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.UserCartTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.UserCartTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.UserCartTable.setColumnWidth(1, 65)
        self.UserCartTable.setColumnWidth(2, 32)

        self.UserCartTable.verticalHeader().setVisible(False)
        self.UserCartTable.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.UserCartTable.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.vBoxLayout.addWidget(self.UserNameLabel)
        self.vBoxLayout.addWidget(self.UserNameLineEdit)
        self.vBoxLayout.addWidget(self.UserEmailLabel)
        self.vBoxLayout.addWidget(self.UserEmailLineEdit)
        self.vBoxLayout.addWidget(self.UserPermissionLabel)
        self.vBoxLayout.addWidget(self.UserPermissionComboBox)
        self.vBoxLayout.addWidget(self.UserCartLabel)
        self.vBoxLayout.addWidget(self.UserCartTable)
        self.hBoxLayout.addWidget(self.SaveChangeButton)
        self.hBoxLayout.addWidget(self.DeleteUserButton)
        self.hBoxLayout.addWidget(self.CancelButton)

    def bind(self):
        self.SaveChangeButton.clicked.connect(self.save)
        self.DeleteUserButton.clicked.connect(self.delete)
        self.CancelButton.clicked.connect(self.close)
        self.refreshSignal.connect(self.parent.reload)

    def loaddata(self):
        user = look_up_user(self.user_id)
        self.UserNameLineEdit.setText(user["name"])
        self.UserEmailLineEdit.setText(user["email"])
        self.UserPermissionComboBox.setCurrentText(
            look_up_user(self.user_id)["permission"]
        )

        for book_id, quantity in look_up_user(self.user_id)["cart"].items():
            row_position = self.UserCartTable.rowCount()
            self.UserCartTable.insertRow(row_position)

            item = QTableWidgetItem(look_up_book(book_id)["name"])
            item.setData(1, book_id)
            self.UserCartTable.setItem(row_position, 0, item)
            self.UserCartTable.item(row_position, 0).setFlags(
                self.UserCartTable.item(row_position, 0).flags() & ~Qt.ItemIsEditable
            )
            self.UserCartTable.setItem(row_position, 1, QTableWidgetItem(str(quantity)))

            ButtonWidget = QWidget()
            ButtonhBoxLayout = QHBoxLayout()
            ButtonhBoxLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            ButtonWidget.setContentsMargins(0, 0, 0, 0)
            ButtonhBoxLayout.setContentsMargins(0, 0, 0, 0)
            DeleteCartItemButton = ToolButton(FluentIcon.DELETE)
            DeleteCartItemButton.setFixedSize(QSize(32, 32))
            DeleteCartItemButton.clicked.connect(
                lambda: self.DeleteCartItem(row_position)
            )
            ButtonhBoxLayout.addWidget(DeleteCartItemButton)
            ButtonWidget.setLayout(ButtonhBoxLayout)

            self.UserCartTable.setCellWidget(row_position, 2, ButtonWidget)

    def DeleteCartItem(self, row):
        self.UserCartTable.removeRow(row)
        # self.refreshSignal.emit()

    def save(self):
        user_name = self.UserNameLineEdit.text()
        user_email = self.UserEmailLineEdit.text()
        user_cart = {}
        for row in range(self.UserCartTable.rowCount()):
            book_id = self.UserCartTable.item(row, 0).data(1)
            quantity = self.UserCartTable.item(row, 1).text()
            user_cart[book_id] = int(quantity)

        if self.mode == "Update":
            res = update_user(
                user_id=self.user_id,
                name=user_name,
                email=user_email,
                permission=self.UserPermissionComboBox.currentText(),
                cart=user_cart,
            )
        else:
            res = add_user(
                name=user_name,
                email=user_email,
                password="1",
                permission=self.UserPermissionComboBox.currentText(),
            )
        if res:
            QMessageBox.information(self, "User updated", "User updated Successfully")
            self.close()
            self.refreshSignal.emit()

        else:
            QMessageBox.warning(self, "Failed", "Failed to update")

    def delete(self):
        if self.mode == "Update":
            res = delete_user(self.user_id)
            if res:
                QMessageBox.information(
                    self, "User deleted", "User deleted Successfully"
                )
                self.close()
                self.refreshSignal.emit()

            else:
                QMessageBox.warning(self, "Failed", "Failed to delete")
        else:
            QMessageBox.warning(
                self, "Error deleting", "Cannot delete user that not exist"
            )
            self.DeleteUserButton.deleteLater()


class PopupBox_Book(Window):
    refreshSignal = Signal()

    def __init__(self, book_id, parent=None, mode="Update"):
        super().__init__()
        self.parent = parent
        self.titleBar.raise_()
        self.setStyleSheet(
            """PopupBox_Book {
    background-color: rgba(255, 255, 255, 0.667);
}"""
        )
        self.book_id = book_id
        self.mode = mode
        self.setFixedSize(QSize(350, 350))
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.setSpacing(7)

        self.BookNameLabel = QLabel(self)
        self.BookNameLineEdit = LineEdit(self)
        self.BookDescLabel = QLabel(self)
        self.BookDescLineEdit = LineEdit(self)
        self.BookPriceLabel = QLabel(self)
        self.BookPriceSpinBox = DoubleSpinBox(self)
        self.BookAuthorLabel = QLabel(self)
        self.BookAuthorLineEdit = LineEdit(self)
        self.SaveChangeButton = PushButton(FluentIcon.SAVE, "SAVE")
        self.DeleteBookButton = PushButton(FluentIcon.DELETE, "DELETE")
        self.CancelButton = PushButton(FluentIcon.CANCEL, "CANCEL")

        self.__initWidgets()
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.bind()
        if self.mode == "Update":
            self.loaddata()
        # else:
        #     self.book_id = generate_id()

    def __initWidgets(self):
        self.BookNameLineEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.BookNameLineEdit.setClearButtonEnabled(True)
        self.BookAuthorLineEdit.setClearButtonEnabled(True)
        self.BookDescLineEdit.setClearButtonEnabled(True)

        self.BookNameLabel.setText("Book Name:")
        self.BookDescLabel.setText("Book Description:")
        self.BookPriceLabel.setText("Book Price:")
        self.BookAuthorLabel.setText("Book Author:")

        # self.BookNameLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        # self.BookDescLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        # self.BookPriceLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        # self.BookAuthorLabel.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.BookNameLabel.setFixedWidth(100)
        self.BookDescLabel.setFixedWidth(100)
        self.BookPriceLabel.setFixedWidth(100)
        self.BookAuthorLabel.setFixedWidth(100)

        self.vBoxLayout.addWidget(self.BookNameLabel)
        self.vBoxLayout.addWidget(self.BookNameLineEdit)
        self.vBoxLayout.addWidget(self.BookAuthorLabel)
        self.vBoxLayout.addWidget(self.BookAuthorLineEdit)
        self.vBoxLayout.addWidget(self.BookDescLabel)
        self.vBoxLayout.addWidget(self.BookDescLineEdit)
        self.vBoxLayout.addWidget(self.BookPriceLabel)
        self.vBoxLayout.addWidget(self.BookPriceSpinBox)
        self.hBoxLayout.addWidget(self.SaveChangeButton)
        self.hBoxLayout.addWidget(self.DeleteBookButton)
        self.hBoxLayout.addWidget(self.CancelButton)

    def bind(self):
        self.SaveChangeButton.clicked.connect(self.save)
        self.DeleteBookButton.clicked.connect(self.delete)
        self.CancelButton.clicked.connect(self.close)
        self.refreshSignal.connect(self.parent.reload)

    def loaddata(self):
        Book = look_up_book(self.book_id)
        self.BookNameLineEdit.setText(Book["name"])
        self.BookAuthorLineEdit.setText(Book["author"])
        self.BookDescLineEdit.setText(Book["desc"])
        self.BookPriceSpinBox.setValue(Book["price"])

    def save(self):
        book_name = self.BookNameLineEdit.text()
        book_author = self.BookAuthorLineEdit.text()
        book_desc = self.BookDescLineEdit.text()
        book_price = self.BookPriceSpinBox.value()
        if self.mode == "Update":
            res = update_book(
                self.book_id, book_name, book_author, book_price, book_desc
            )
        else:
            res = add_book(book_name, book_author, book_price, book_desc)

        if res:
            QMessageBox.information(self, "Book saved", "Book saved Successfully")
            self.close()
            self.refreshSignal.emit()
        else:
            QMessageBox.warning(self, "Failed", "Failed to save")

    def delete(self):
        if self.mode == "Update":
            res = delete_book(self.book_id)
            if res:
                QMessageBox.information(
                    self, "Book deleted", "Book deleted Successfully"
                )
                self.close()
                self.refreshSignal.emit()

            else:
                QMessageBox.warning(self, "Failed", "Failed to delete")
        else:
            QMessageBox.warning(
                self, "Error deleting", "Cannot delete book that not exist"
            )
            self.DeleteBookButton.deleteLater()
