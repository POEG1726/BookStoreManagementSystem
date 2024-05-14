from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMessageBox,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QListWidgetItem,
    QTableWidgetItem,
)
from qfluentwidgets import (
    ListWidget,
    TableWidget,
    style_sheet,
    PopupTeachingTip,
    TeachingTipTailPosition,
    PushButton,
    SpinBox,
)
from PopupBox import PopupBox_Book, PopupBox_User
from Backend import *


class ManagementInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setObjectName('ManagementInterface')
        self.UserEditor = None
        self.BookEditor = None

        self.vBoxLayout = QVBoxLayout(self)
        self.BannerLayout = QHBoxLayout()

        self.TitleLabel = QLabel(self)

        self.UserManagementWidget = QWidget(self)
        self.UserManagementLabel = QLabel(self.UserManagementWidget)
        self.UserDisplayTable = TableWidget(self.UserManagementWidget)

        self.BookManagementWidget = QWidget(self)
        self.BookManagementLabel = QLabel(self.BookManagementWidget)
        self.BookDisplayList = ListWidget(self.BookManagementWidget)

        self.topLayout = QHBoxLayout()
        self.UserManagementLayout = QVBoxLayout(self.UserManagementWidget)
        self.BookManagementLayout = QVBoxLayout(self.BookManagementWidget)

        self.DebugWidget = QWidget(self)
        self.DebugWidget.setObjectName("DebugWidget")
        self.OperationLayout = QVBoxLayout(self.DebugWidget)
        self.UserLayout = QHBoxLayout()
        self.BookLayout = QHBoxLayout()

        self.AddUserButton = PushButton("Add new user", self.DebugWidget)
        self.AddBookButton = PushButton("Add new book", self.DebugWidget)

        self.GenerateUservLayout = QVBoxLayout()
        self.GenerateUserLabel = QLabel(self.DebugWidget)
        self.GenerateUserhLayout = QHBoxLayout()
        self.GenerateUserSpinBox = SpinBox(self.DebugWidget)
        self.GenerateUserButton = PushButton("Generate", self.DebugWidget)

        self.GenerateBookvLayout = QVBoxLayout()
        self.GenerateBookLabel = QLabel(self.DebugWidget)
        self.GenerateBookhLayout = QHBoxLayout()
        self.GenerateBookSpinBox = SpinBox(self.DebugWidget)
        self.GenerateBookButton = PushButton("Generate", self.DebugWidget)

        self.__initWidgets()
        self.bind()
        self.add_user_to_table_widget()
        self.add_book_to_list_widget()

    def __initLayouts(self):
        self.BannerLayout.addWidget(self.TitleLabel)

        self.GenerateUservLayout.addWidget(self.GenerateUserLabel)
        self.GenerateUserhLayout.addWidget(self.GenerateUserSpinBox)
        self.GenerateUserhLayout.addWidget(self.GenerateUserButton)
        self.GenerateUservLayout.addLayout(self.GenerateUserhLayout)
        self.UserLayout.addWidget(self.AddUserButton)
        self.UserLayout.addLayout(self.GenerateUservLayout)

        self.GenerateBookvLayout.addWidget(self.GenerateBookLabel)
        self.GenerateBookhLayout.addWidget(self.GenerateBookSpinBox)
        self.GenerateBookhLayout.addWidget(self.GenerateBookButton)
        self.GenerateBookvLayout.addLayout(self.GenerateBookhLayout)
        self.BookLayout.addWidget(self.AddBookButton)
        self.BookLayout.addLayout(self.GenerateBookvLayout)

        self.OperationLayout.addLayout(self.UserLayout)
        self.OperationLayout.addLayout(self.BookLayout)

        self.BannerLayout.addWidget(self.DebugWidget)
        # self.BannerLayout.addLayout(self.OperationLayout)
        self.BannerLayout.setContentsMargins(0, 0, 16, 0)

        self.vBoxLayout.addSpacing(4)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.UserManagementLayout.addWidget(self.UserManagementLabel)
        self.UserManagementLayout.addWidget(self.UserDisplayTable)
        self.BookManagementLayout.addWidget(self.BookManagementLabel)
        self.BookManagementLayout.addWidget(self.BookDisplayList)

        self.topLayout.addWidget(self.UserManagementWidget)
        self.topLayout.addWidget(self.BookManagementWidget)

        self.vBoxLayout.addLayout(self.BannerLayout)
        self.vBoxLayout.addLayout(self.topLayout)

    def __initWidgets(self):
        self.__initLayouts()
        self.setObjectName("ManagementInterface")

        self.TitleLabel.setText("Book Store Management Interface")
        self.BookManagementLabel.setText("Book Management")
        self.UserManagementLabel.setText("User Management")

        self.GenerateUserLabel.setText("Generate Virtual Users")
        self.GenerateBookLabel.setText("Generate Virtual Books")

        self.GenerateUserSpinBox.setMaximum(20)
        self.GenerateBookSpinBox.setMaximum(10)
        self.GenerateUserSpinBox.setMinimum(0)
        self.GenerateBookSpinBox.setMinimum(0)
        self.GenerateUserSpinBox.setValue(0)
        self.GenerateBookSpinBox.setValue(0)

        self.AddUserButton.setFixedWidth(127)
        self.AddBookButton.setFixedWidth(127)
        self.GenerateUserButton.setFixedWidth(85)
        self.GenerateBookButton.setFixedWidth(85)
        self.GenerateUserSpinBox.setFixedWidth(110)
        self.GenerateBookSpinBox.setFixedWidth(110)
        self.DebugWidget.setStyleSheet(
            """#DebugWidget {border: 1px solid rgba(255, 0, 0, 0.2);
            border-radius: 10px; background-color: rgba(255, 200, 220, 0.05);}"""
        )

        self.UserDisplayTable.setColumnCount(4)

        self.UserManagementLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.BookManagementLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.UserManagementWidget.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        )
        self.BookManagementWidget.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        )
        self.BookManagementWidget.setMaximumWidth(230)

        self.BookManagementLabel.setStyleSheet("font-size: 18px;")
        self.UserManagementLabel.setStyleSheet("font-size: 18px;")
        self.TitleLabel.setStyleSheet("""font-size: 24px;""")
        # self.UserDisplayTable.setBorderRadius(10)
        # self.UserDisplayTable.setBorderVisible(True)
        self.UserDisplayTable.setStyleSheet(
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
        self.BookDisplayList.setStyleSheet(
            """ListView,
ListWidget {
    background: transparent;
    background-color: rgba(255, 255, 255, 0.667);
    outline: none;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    /* font: 13px 'Segoe UI', 'Microsoft YaHei'; */
    selection-background-color: transparent;
    alternate-background-color: transparent;
}
ListView::item,
ListWidget::item {
    background: transparent;
    border: 0px;
    height: 35px;
}
ListView::indicator,
ListWidget::indicator {
    width: 18px;
    height: 18px;
    border-radius: 5px;
    border: none;
    background-color: transparent;
    margin-right: 4px;
}

"""
        )
        self.setStyleSheet("#ManagementInterface {background-color: transparent;}")

        self.TitleLabel.setContentsMargins(15, 10, 0, 0)
        self.UserManagementWidget.setContentsMargins(0, 0, 0, 0)
        self.BookManagementWidget.setContentsMargins(0, 0, 0, 0)

    def bind(self):
        self.UserDisplayTable.itemDoubleClicked.connect(self.table_doubleclicked_event)
        self.BookDisplayList.itemDoubleClicked.connect(self.list_doubleclicked_event)
        self.AddUserButton.clicked.connect(self.add_user)
        self.AddBookButton.clicked.connect(self.add_book)
        self.GenerateUserButton.clicked.connect(self.GenerateUser)
        self.GenerateBookButton.clicked.connect(self.GenerateBook)

    def add_user_to_table_widget(self):
        Users = loadUsers()
        self.UserDisplayTable.setRowCount(len(Users.keys()))
        self.UserDisplayTable.setHorizontalHeaderLabels(
            ["User Name", "Email", "ID", "Cart"]
        )
        self.UserDisplayTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.UserDisplayTable.verticalHeader().setVisible(False)
        self.UserDisplayTable.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.UserDisplayTable.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        for row, user_info in enumerate(Users.values()):
            del user_info["pwd"]
            del user_info["permission"]
            for col, info in enumerate(user_info.values()):
                if col == 3:
                    _ = ""
                    if len(info) > 1:
                        for key in info:
                            _ += f"{key},"
                        info = _
                    else:
                        info = "None"
                self.UserDisplayTable.setItem(row, col, QTableWidgetItem(str(info)))
                self.UserDisplayTable.item(row, col).setFlags(
                    self.UserDisplayTable.item(row, col).flags() & ~Qt.ItemIsEditable
                )

    def add_book_to_list_widget(self):
        Books = loadBooks()

        for book_id, book in Books.items():
            item = QListWidgetItem(book["name"])
            # item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setData(1, book_id)
            self.BookDisplayList.addItem(item)

    def table_doubleclicked_event(self, item):
        user_id = self.UserDisplayTable.item(item.row(), 2).text()
        self.UserEditor = PopupBox_User(user_id=user_id, parent=self)
        self.UserEditor.show()

    def list_doubleclicked_event(self, item):
        book_id = item.data(1)
        self.BookEditor = PopupBox_Book(book_id=book_id, parent=self)
        self.BookEditor.show()
        # self.BookEditor = PopupTeachingTip.make(
        #     target=self.BookDisplayList,
        #     view=PopupBox_Book(book_id=book_id, parent=self),
        #     tailPosition=TeachingTipTailPosition.LEFT,
        #     duration=-1,
        #     parent=self,
        # )

    def add_user(self):
        self.UserEditor = PopupBox_User(user_id="", mode="Add", parent=self)
        self.UserEditor.show()

    def add_book(self):
        self.BookEditor = PopupBox_Book(book_id="", mode="Add", parent=self)
        self.BookEditor.show()

    def GenerateUser(self):
        num = self.GenerateUserSpinBox.value()
        res = generate_fake_users(num)
        if res:
            QMessageBox.information(self.DebugWidget,'Generate Successfully',f'Generated {num} users successfully All passwords were 1')
            self.reload()
            self.GenerateUserSpinBox.setValue(0)
        else:
            QMessageBox.warning(self.DebugWidget,'Generate Failed','Generate Failed')

    def GenerateBook(self):
        num = self.GenerateBookSpinBox.value()
        res = generate_fake_books(num)
        if res:
            QMessageBox.information(self.DebugWidget,'Generate Successfully',f'Generated {num} books successfully')
            self.reload()
            self.GenerateBookSpinBox.setValue(0)
        else:
            QMessageBox.warning(self.DebugWidget,'Generate Failed','Generate Failed')

    def reload(self):
        self.UserDisplayTable.setRowCount(0)
        self.BookDisplayList.clear()
        self.parent.homeInterface.reload()
        self.parent.cartInterface.reload()

        self.add_user_to_table_widget()
        self.add_book_to_list_widget()