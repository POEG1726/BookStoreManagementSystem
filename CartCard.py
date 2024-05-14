from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from qfluentwidgets import (
    FlyoutViewBase,
    PopupTeachingTip,
    PrimaryPushButton,
    SpinBox,
    TeachingTipTailPosition,
    SmoothScrollArea,
)

import resource_rc
from Backend import *


class CustomFlyoutView(FlyoutViewBase):
    SignalChoice = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        self.label = QLabel("Are you sure you want to delete it from your cart?")
        self.button_yes = PrimaryPushButton("Yes")
        self.button_cancel = PrimaryPushButton("Calcel")
        self.button_yes.setSizePolicy(
            QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        )
        self.button_yes.clicked.connect(lambda: self.SignalChoice.emit(True))
        self.button_cancel.clicked.connect(lambda: self.SignalChoice.emit(False))

        self.button_cancel.setSizePolicy(
            QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        )
        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(20, 16, 20, 16)
        self.vBoxLayout.addWidget(self.label)
        self.hBoxLayout.addWidget(self.button_yes)
        self.hBoxLayout.addWidget(self.button_cancel)
        self.vBoxLayout.addLayout(self.hBoxLayout)


class CartCard(QFrame):
    def __init__(
        self,
        name: str,
        author: str,
        desc: str,
        book_id: str,
        quantity: int,
        price: int,
        parent=None,
    ) -> None:
        super().__init__(parent)
        self.parent = parent
        self.user = self.parent.parent.user
        self.popuptip = None
        self.name = name
        self.author = author if author else "Unknown"
        self.desc = desc
        self.quantity = quantity
        self.price = price
        self.book_id = book_id
        # self.setFixedSize(700, 110)

        self.spinBox = SpinBox(self)
        self.PriceLabel = QLabel(self)
        self.QuantityLabel = QLabel(self)
        self.DescLabel = QLabel(self)
        self.AuthorLabel = QLabel(self)
        self.NameLabel = QLabel(self)
        self.ImageLabel = QLabel(self)

        self.NameLabel.setText(self.name)
        self.AuthorLabel.setText(self.author)
        self.DescLabel.setText(
            self.DescLabel.fontMetrics().elidedText(
                self.desc, Qt.ElideRight, self.DescLabel.width()
            )
        )
        # self.DescLabel.setText(desc)
        self.PriceLabel.setText(f"Total: $ {round(self.price*self.quantity,2)}")
        self.spinBox.setValue(self.quantity)
        self.previous_value = self.quantity
        self.spinBox.valueChanged.connect(self.QuantityChangedEvent)
        self.flyoutview = CustomFlyoutView()
        self.__initWidget()

    def __initWidget(self):
        self.setStyleSheet(
            """
QLabel {font-size: 14pt;}
SpinBox {
    min-height: 30px;
    font-size: 15pt;
}
QLabel#PriceLabel {
    font-size: 14pt;
}"""
        )
        self.hBoxLayout = QHBoxLayout(self)
        # self.setMinimumWidth(736)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setFixedSize(80, 80)
        self.ImageLabel.setPixmap(QPixmap(":/images/resource/images/Book.png"))
        self.ImageLabel.setScaledContents(True)

        self.hBoxLayout.addWidget(self.ImageLabel)

        self.vBoxLayout = QVBoxLayout()

        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.NameLabel.sizePolicy().hasHeightForWidth())
        self.NameLabel.setSizePolicy(sizePolicy1)
        self.NameLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.vBoxLayout.addWidget(self.NameLabel)
        sizePolicy1.setHeightForWidth(self.AuthorLabel.sizePolicy().hasHeightForWidth())
        self.AuthorLabel.setSizePolicy(sizePolicy1)
        self.AuthorLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.vBoxLayout.addWidget(self.AuthorLabel)
        self.vBoxLayout
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.DescLabel.setWordWrap(True)
        self.DescLabel.setFixedHeight(70)
        self.DescLabel.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        )
        self.hBoxLayout.addWidget(self.DescLabel)
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.QuantityLabel.sizePolicy().hasHeightForWidth()
        )
        self.QuantityLabel.setSizePolicy(sizePolicy2)
        # font = QFont()
        # font.setPointSize(14)
        # self.QuantityLabel.setFont(font)

        self.hBoxLayout.addWidget(self.QuantityLabel)

        # self.spinBox.setMinimumHeight(30)
        # font1 = QFont()
        # font1.setPointSize(15)
        # self.spinBox.setFont(font1)
        self.spinBox.setFrame(True)
        self.spinBox.setMaximum(32773)
        self.spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hBoxLayout.addWidget(self.spinBox)

        # self.PriceLabel.setFont(font)
        self.PriceLabel.setFixedWidth(100)
        self.PriceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hBoxLayout.addWidget(self.PriceLabel)

    def QuantityChangedEvent(self, value):
        if value == 0:
            self.showTeachingTip()
        else:
            self.PriceLabel.setText(f"Total: $ {round(self.price*value,2)}")
            update_cart(self.user["uniqID"], self.book_id, value)

    def showTeachingTip(self):
        self.popuptip = PopupTeachingTip.make(
            target=self.spinBox,
            view=self.flyoutview,
            tailPosition=TeachingTipTailPosition.RIGHT,
            duration=-1,
            parent=self,
            isDeleteOnClose=False,
        )
        self.popuptip.view.SignalChoice.connect(lambda x: self.updatevariable(x))

    def updatevariable(self, choice):
        print(choice)
        self.popuptip.close()
        if choice == True:
            delete_from_cart(self.user["uniqID"], self.book_id)
            QMessageBox.information(
                self, "Removed", f"Removed {self.name} from your cart"
            )
            self.deleteLater()
        elif choice == False:
            QMessageBox.information(
                self, "Cancelled", f"Cancelled removing {self.name} from your cart"
            )
            print("Cancelled")
            self.spinBox.setValue(self.previous_value)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.DescLabel.setText(
            self.DescLabel.fontMetrics().elidedText(
                self.desc, Qt.ElideRight, self.DescLabel.width()
            )
        )
        self.DescLabel.setWordWrap(True)


class ToolBar(QWidget):
    """Tool bar"""

    def __init__(self, title, subtitle, parent=None):
        super().__init__(parent=parent)
        self.titleLabel = QLabel(title, self)
        self.titleLabel.setObjectName("TitleLabel")
        self.subtitleLabel = QLabel(subtitle, self)
        self.subtitleLabel.setObjectName("SubtitleLabel")

        self.vBoxLayout = QVBoxLayout(self)

        self.__initWidget()

    def __initWidget(self):
        self.setFixedHeight(80)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(36, 0, 36, 0)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addWidget(self.subtitleLabel)
        # self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

        # self.subtitleLabel.setTextColor(QColor(96, 96, 96), QColor(216, 216, 216))


class CartCardView(SmoothScrollArea):
    def __init__(self, title: str, subtitle: str, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        # self.setSmoothMode(SmoothMode.NO_SMOOTH)
        self.view = QWidget(self)
        self.toolBar = ToolBar(title, subtitle, self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, self.toolBar.height(), 0, 0)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setSpacing(30)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.vBoxLayout.setContentsMargins(36, 0, 36, 36)

        self.view.setObjectName("view")
        self.setStyleSheet(
            """
CartCardView, ToolBar, #view {
    background-color: transparent;
}

SmoothScrollArea {
    border: none;
}

ToolBar > #TitleLabel {
    color: black;
    font: 28px;
}

ToolBar > #SubtitleLabel {
    font: 14px
    color: rgb(96, 96, 96);
}

TitleLabel {
    color: black;
}

CartCard > QLabel {
    font: 14px;
    color: black;
}
"""
        )
        # self.add_item('BookName','JLin','This is the description of the book',10,5)

    def add_item(self, name, author, description, book_id, quantity, price):
        item = CartCard(name, author, description, book_id, quantity, price, self)
        # item = CartCard(name, author, description, book_id, quantity, price, self.view)
        self.vBoxLayout.addWidget(item)

    # def remove_item(self):
    #     self.vBoxLayout.removeWidget


if __name__ == "__main__":
    app = QApplication()
    window = CartCardView("CartInterface", "Subtitle")
    window.add_item(
        "BookName", "JLin", "This is the description of the book", "000ef68b", 2, 5
    )
    window.setMinimumHeight(250)
    window.show()
    app.exec()
