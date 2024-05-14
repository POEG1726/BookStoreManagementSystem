from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QLabel, QSizePolicy

from qfluentwidgets import ScrollArea
from BookCard import BookCardView

from Backend import *


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
        self.vBoxLayout.setContentsMargins(36, 36, 36, 0)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addWidget(self.subtitleLabel)
        # self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.setAlignment(Qt.AlignTop)


class HomeInterface(ScrollArea):
    """Home interface"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        if parent:
            self.parent = parent
        self.BookCardView = None
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)
        # TitleLabel = QLabel(self)
        # TitleLabel.setText("Home Interface")
        # TitleLabel.setStyleSheet("""font-size: 24px;""")
        # TitleLabel.setContentsMargins(36, 10, 0, 0)
        # self.vBoxLayout.addWidget(TitleLabel)
        self.toolBar = ToolBar("Home Interface", "Click to add book to your cart", self)
        self.setViewportMargins(0, self.toolBar.height(), 0, 0)
        # SubTitleLabel = QLabel(self)
        # SubTitleLabel.setText("Double Click to add book to your cart")
        # SubTitleLabel.setStyleSheet("""font-size: 16px;""")
        # SubTitleLabel.setContentsMargins(36, 10, 0, 0)
        # self.vBoxLayout.addWidget(SubTitleLabel)
        self.__initWidget()

    def __initWidget(self):
        self.view.setObjectName("view")
        self.setObjectName("homeInterface")
        self.setStyleSheet(
            """SettingInterface,
#view {
    background-color: transparent;
}

QScrollArea {
    border: none;
    background-color: transparent;
}

BannerWidget > #galleryLabel {
    font: 42px;
    background-color: transparent;
    color: black;
    padding-left: 28px;
}

CartCardView {
    background-color: transparent;
}

ToolBar > #TitleLabel {
    color: black;
    font: 28px;
}

ToolBar > #SubtitleLabel {
    font: 14px;
    color: rgb(96, 96, 96);
}

TitleLabel {
    color: black;
}
"""
        )

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 30, 0, 36)
        # self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.Books = loadBooks()
        self.BookCardView = BookCardView(self)
        self.vBoxLayout.addWidget(
            self.BookCardView,
            1,
        )
        self.Add_ALL_Book_To_Screen()

    def Add_ALL_Book_To_Screen(self):
        for id, book in self.Books.items():
            self.BookCardView.addCard(
                title=book["name"],
                content=book["desc"],
                book_id=id,
            )

    def reload(self):
        self.BookCardView.flowLayout.takeAllWidgets()
        self.Books = loadBooks()
        self.Add_ALL_Book_To_Screen()