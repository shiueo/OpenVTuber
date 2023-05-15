from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
    QMenuBar,
    QMenu,
)

from utils import global_path


class OpenVTuber_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenVTuber")
        self.resize(1280, 720)
        self.setWindowIcon(QIcon(global_path.get_proj_abs_path("assets/icon.png")))

        widget = QWidget()
        self.setCentralWidget(widget)

        self.initUI()

    def initUI(self):
        with open(
            file=global_path.get_proj_abs_path("assets/stylesheet.txt"), mode="r"
        ) as f:
            self.setStyleSheet(f.read())
