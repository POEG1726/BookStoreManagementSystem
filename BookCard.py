from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QWidget,
    QMessageBox,
    QApplication,
)

from qfluentwidgets import (
    IconWidget,
    FluentIcon,
    TextWrap,
    SmoothScrollArea,
    FlowLayout,
)
from Backend import *


class BookCard(QFrame):

    def __init__(self, title, content, book_id, user_id, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(198, 220)
        self.setToolTip("Click to add book to cart")
        self.titleLabel = QLabel(title, self)
        self.titleLabel.setWordWrap(True)
        self.PriceLabel = QLabel(self)
        self.book_id = book_id
        self.user_id = user_id
        self.contentLabel = QLabel(TextWrap.wrap(content, 28, False)[0], self)
        self.CartWidget = IconWidget(FluentIcon.SHOPPING_CART, self)

        self.__initWidget()

    def __initWidget(self):
        self.setCursor(Qt.PointingHandCursor)
        self.contentLabel.setFixedHeight(60)
        self.CartWidget.setFixedSize(16, 16)
        self.PriceLabel.setText(f"Price: ${look_up_book(self.book_id)['price']}")

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(20, 0, 10, 13)
        self.vBoxLayout.addSpacing(16)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(8)
        self.vBoxLayout.addWidget(self.contentLabel)
        self.vBoxLayout.addStretch()
        self.vBoxLayout.addWidget(self.PriceLabel)
        self.vBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.CartWidget.move(170, 192)

        self.titleLabel.setObjectName("titleLabel")
        self.contentLabel.setObjectName("contentLabel")

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        quantity = loadCart(user_id=self.user_id)
        if self.book_id in quantity.keys():
            quantity[self.book_id] += 1
        else:
            quantity[self.book_id] = 1
        res = update_cart(
            user_id=self.user_id, book_id=self.book_id, quantity=quantity[self.book_id]
        )

        QMessageBox.information(
            self,
            "Add Success",
            f"Added 'book: {look_up_book(book_id=res[1])['name']}' to your cart.\n\n   Quantity: {quantity[self.book_id]}",
        )


class BookCardView(SmoothScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.view = QWidget(self)
        if parent:
            self.parent = parent
        self.flowLayout = FlowLayout(self.view)
        self.flowLayout.setContentsMargins(36, 36, 36, 0)
        self.flowLayout.setSpacing(12)
        self.flowLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setWidget(self.view)
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setObjectName("view")
        self.view.setStyleSheet(
            """BookCard {
    border: 1px solid rgb(200, 200, 200);
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.667);
}

BookCard:hover {
    background-color: rgba(249, 249, 249, 0.93);
    border: 1px solid rgb(170, 170, 170);
}

#titleLabel {
    font: 18px 'PingFang SC';
    color: black;
}

#contentLabel {
    font: 12px 'PingFang SC';
    color: rgb(93, 93, 93);
}

BookCardView {
    background-color: transparent;
    border: none;
}

#view {
    background-color: transparent;
}"""
        )

    def addCard(self, title, content, book_id):
        """add link card"""
        card = BookCard(
            title, content, book_id, self.parent.parent.user["uniqID"], self.view
        )
        self.flowLayout.addWidget(card)