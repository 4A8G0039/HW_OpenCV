import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_showhistogram import Ui_Showhistogram
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cImg_o = np.zeros((1,1,3), np.uint8)
        self.ui = Ui_Showhistogram(self.cImg_o)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
 
    sys.exit(app.exec_())
