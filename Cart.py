from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QLabel, QSizePolicy

from qfluentwidgets import ScrollArea
from CartCard import CartCardView

from Backend import *


class CartInterface(ScrollArea):
    """Home interface"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        if parent:
            self.parent = parent
        self.user = look_up_user(self.parent.user["uniqID"])
        # self.user = look_up_user("0008bc60")

        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)
        self.__initWidget()

    def __initWidget(self):
        self.view.setObjectName("view")
        self.setObjectName("CartInterface")
        self.setStyleSheet(
            """#view {
    background-color: transparent;
}

QScrollArea {
    border: none;
    background-color: transparent;
}

CartCard {
    background-color: rgba(255, 255, 255, 0.667);
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    border-radius: 10px;
}
"""
        )

        self.setMinimumWidth(736)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 30, 0, 0)
        # self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

        self.CartCardView = CartCardView(
            parent=self,
            title=f"{self.user['name']}'s Cart",
            # subtitle=f"Items were loaded from user: poeg1726@qq.com",
            subtitle=f'Items were loaded from user: {self.user["email"] }',
        )
        self.vBoxLayout.addWidget(
            self.CartCardView,
            1,
        )

        self.CartItem_Statistics = loadCart(self.user["uniqID"])
        self.Add_All_Cart_Items()

    def Add_All_Cart_Items(self):
        if self.CartItem_Statistics == {}:
            NothingLabel = QLabel(self)
            NothingLabel.setText("Nothing in your cart! Why not add something?")
            NothingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            NothingLabel.setStyleSheet(
                """font-size: 30px;
color: green;"""
            )
            NothingLabel.setSizePolicy(
                QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            )
            self.CartCardView.vBoxLayout.addWidget(NothingLabel)
        self.CartItems = []
        for book_id in self.CartItem_Statistics.keys():
            self.CartItems.append(look_up_book(book_id=book_id))
        for item_1, item_2 in zip(self.CartItem_Statistics.items(), self.CartItems):
            book_id, quantity = item_1
            self.CartCardView.add_item(
                name=item_2["name"],
                author=item_2["author"],
                description=item_2["desc"],
                book_id=book_id,
                quantity=quantity,
                price=item_2["price"],
            )

    def reload(self):
        if self.CartCardView.vBoxLayout.count() > 0:
            while self.CartCardView.vBoxLayout.count():
                item = self.CartCardView.vBoxLayout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

        self.CartItem_Statistics = loadCart(self.user["uniqID"])
        self.Add_All_Cart_Items()