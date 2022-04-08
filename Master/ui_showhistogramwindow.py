import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent = None, width = 10, height = 4, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor="black")
        self.axes = fig.add_subplot(111)
        self.axes.set_facecolor('k')
        self.axes.tick_params(labelcolor='w')
        self.axes.spines['top'].set_color('w')
        self.axes.spines['bottom'].set_color('w')
        self.axes.spines['left'].set_color('w')
        self.axes.spines['right'].set_color('w')
        self.axes.tick_params(axis='x', colors='w')
        self.axes.tick_params(axis='y', colors='w')
        super(MplCanvas, self).__init__(fig)


class Ui_ShowhistogramWindow(QWidget):
    def __init__(self, cImg_o):
        super(Ui_ShowhistogramWindow, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Show_histogram")
        sc = MplCanvas(self)
        self.cImg_o = cImg_o
        color=('b','g','r')
        for i,col in enumerate(color):
                hist = cv2.calcHist([self.cImg_o],[i],None,[256],[0,256])
                sc.axes.plot(hist,color=col)#(一維陣列,線顏色)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ui_Showhistogram()
#     window.show()
#     sys.exit(app.exec_())