import os
import sys

from PySide6.QtWidgets import QApplication

from src.ui.mainwindow import OpenVTuber_MainWindow

from utils import global_path

global_path.set_proj_abs_path(os.path.abspath(__file__))

OpenVTuber_QApplication = QApplication()
OpenVTuber_Window = OpenVTuber_MainWindow()
OpenVTuber_Window.show()
sys.exit(OpenVTuber_QApplication.exec())
