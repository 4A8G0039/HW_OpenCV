import sys
import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from image_filtering import *

import numpy as np


class Ui_Image_Filtering_Window(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Image_Filtering_Window, self).__init__()
        self.setWindowTitle("Blur (均值濾波)")
        self.setFixedSize(820, 100)
        self.seaved = False
        self.index = 0
        self.mainWindow = mainWindow
        self.form = [Ui_Blur(self.mainWindow), 
        Box_Filter(self.mainWindow), 
        Gaussian_Blur(self.mainWindow), 
        Bilateral_Filter(self.mainWindow), 
        Median_Blur(self.mainWindow)]

        widget = QWidget()
        self.stacked_layout = QStackedLayout()
        widget.setLayout(self.stacked_layout)
        for f in self.form:
            self.stacked_layout.addWidget(f)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 5, 0, 0)
        layout.addWidget(widget)
        self.setLayout(layout)

        self.Top_menubar = QMenuBar(self) #新增一個QMenuBar命名為Top_menubar
        self.Top_menubar.setGeometry(QRect(0, 0, 800, 25)) #設定Top_menubar的尺寸
        
        self.Blur_action = QAction(self)
        self.Blur_action.setText("Blur (均值濾波)")
        self.Top_menubar.addAction(self.Blur_action)
        self.Box_Filter_action = QAction(self)
        self.Box_Filter_action.setText("Box Filter (方框濾波)")
        self.Top_menubar.addAction(self.Box_Filter_action)
        self.Gaussian_Blur_action = QAction(self)
        self.Gaussian_Blur_action.setText("Gaussian Blur (高斯濾波)")
        self.Top_menubar.addAction(self.Gaussian_Blur_action)
        self.Bilateral_Filter_action = QAction(self)
        self.Bilateral_Filter_action.setText("Bilateral Filter (雙邊濾波)")
        self.Top_menubar.addAction(self.Bilateral_Filter_action)
        self.Median_Blur_action = QAction(self)
        self.Median_Blur_action.setText("Median Blur (中值濾波)")
        self.Top_menubar.addAction(self.Median_Blur_action)

        self.Blur_action.triggered.connect(self.Blur_Clicked)
        self.Box_Filter_action.triggered.connect(self.Box_Filter_Clicked)
        self.Gaussian_Blur_action.triggered.connect(self.Gaussian_Blur_Clicked)
        self.Bilateral_Filter_action.triggered.connect(self.Bilateral_Filter_Clicked)
        self.Median_Blur_action.triggered.connect(self.Median_Blur_Clicked)
        self.keyPressEvent = self.key_Press_Event
        self.closeEvent = self.close_Event
        self.form[0].img_update()

    def Blur_Clicked(self):
        self.index = 0
        self.setWindowTitle("Blur (均值濾波)")
        self.setFixedSize(820, 100)
        self.stacked_layout.setCurrentIndex(0)
        self.form[0].img_update()

    def Box_Filter_Clicked(self):
        self.index = 1
        self.setWindowTitle("Box Filter (均值濾波)")
        self.setFixedSize(820, 100)
        self.stacked_layout.setCurrentIndex(1)
        self.form[1].img_update()

    def Gaussian_Blur_Clicked(self):
        self.index = 2
        self.setWindowTitle("Gaussian Blur (高斯濾波)")
        self.setFixedSize(820, 140)
        self.stacked_layout.setCurrentIndex(2)
        self.form[2].img_update()

    def Bilateral_Filter_Clicked(self):
        self.index = 3
        self.setWindowTitle("Bilateral Filter (雙邊濾波)")
        self.setFixedSize(820, 140)
        self.stacked_layout.setCurrentIndex(3)
        self.form[3].img_update()

    def Median_Blur_Clicked(self):
        self.index = 4
        self.setWindowTitle("Median Blur (中值濾波)")
        self.setFixedSize(820, 60)
        self.stacked_layout.setCurrentIndex(4)
        self.form[4].img_update()
    
    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()

    def close_Event(self, event):
        if self.seaved:
            self.mainWindow.cImg_o = self.form[self.index].Imag
            self.mainWindow.qImg, self.mainWindow.cImg_r, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
            self.mainWindow.show_img()
        else:
            self.mainWindow.show_img()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     image = cv2.imread("./Img/wallpaper_g.png")
#     win = Ui_Image_Filtering_Window(image)
#     win.show()
#     sys.exit(app.exec_())