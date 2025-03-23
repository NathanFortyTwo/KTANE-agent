from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
import sys


class QTOverlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dragging = False
        self.offset = QPoint()

    def initUI(self):
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint,
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 800, 600)

        self.close_button = QPushButton("X", self)
        self.close_button.setGeometry(750, 10, 40, 30)
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet(
            """
            QPushButton {
                color: white;
                background-color: red;
                border: none;
                font-size: 16px;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
            """
        )

        # Add another clickable button
        self.action_button = QPushButton("Click Me!", self)
        self.action_button.setGeometry(300, 250, 200, 100)
        self.action_button.clicked.connect(self.on_button_click)
        self.action_button.setStyleSheet(
            """
            QPushButton {
                color: black;
                background-color: white;
                border: 2px solid gray;
                font-size: 18px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
            """
        )

    def on_button_click(self):
        print("ee")


class Overlay:
    def __init__(self):
        app = QApplication(sys.argv)
        overlay = QTOverlay()
        overlay.show()
        app.exec_()
