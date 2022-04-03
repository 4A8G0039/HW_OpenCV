#designer
import os
import sys
import time
import cv2


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_mainwindow import Ui_MainWindow
from ui_roiwindow import Ui_ROIWindow

import numpy as np
import matplotlib.pyplot as plt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._window = Ui_MainWindow()
        self._window.setupUi(self)
        self.setup_control()

    def OpenFile(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "OpenFile", "./", "Image Files(*.png *.jpg *.jpeg *.bmp *.tif)")
        if self.filename != "":
            print("Open Path :", self.filename)
            self.cImg_o=cv2.imdecode(np.fromfile(self.filename,dtype=np.uint8),-1)
            self.qImg, self.img_height_r, self.img_width_r, self.cImg_r = self.cvimgTOqtimg(self.cImg_o)
            self._window.Img_Lable.setPixmap(self.qImg)
            if self.img_width_r >= 300 or self.img_height_r >= 300:
                self._window.Img_Lable.setFixedSize(self.img_width_r, self.img_height_r)
                self.setFixedSize(self.img_width_r, self.img_height_r + 45)
            else:
                self._window.Img_Lable.setFixedSize(300, 300)
                self.setFixedSize(300, 345)
            self._window.statusbar.showMessage(self.filename.split("/")[-1])
            
    def ROI(self):
        if self.filename != "":
            self.ROIWindow = Ui_ROIWindow(self.cImg_o, self.cImg_r, self.qImg)
            #self.ROIWindow.show_img(self.qImg)
            # self.ROIWindow.label.setPixmap(self.qImg)
            # self.ROIWindow.label.setFixedSize(self.img_width_r, self.img_height_r)
            # if self.img_width_r >= 200 or self.img_height_r >= 200:
            #     self.ROIWindow.setFixedSize(self.img_width_r, self.img_height_r) 
            #     self.ROIWindow.label.setFixedSize(self.img_width_r, self.img_height_r)
            # else:
            #     self.ROIWindow.setFixedSize(200, 200)
            #     self.ROIWindow.label.setFixedSize(self.img_width_r, self.img_height_r)
            self.ROIWindow.show()
 
    def Show_histogram(self):
        if self.filename != "":
            # 畫出 RGB 三種顏色的分佈圖
            color=('b','g','r')
            plt.style.use('dark_background')
            for i,col in enumerate(color):
                hist=cv2.calcHist([self.cImg_o],[i],None,[256],[0,256])
                plt.plot(hist,color=col)#(一維陣列,線顏色)
                plt.xlim([0,256])#x範圍的值
            plt.show()

    def Show_change_color_space(self):
        self.ShowChange_ColorSpaceWindow = Show_Change_Color_Space_Window()
        self.ShowChange_ColorSpaceWindow.show()

    # def cvImread(self, imgPath):
    #     cvImg=cv2.imdecode(np.fromfile(imgPath,dtype=np.uint8),-1)
    #     cvImg=cv2.cvtColor(cvImg,cv2.COLOR_RGB2BGR)
    #     return cvImg


    def cvimgTOqtimg(self, cvImg):
        print("Height : %d, Width : %d" % (cvImg.shape[0], cvImg.shape[1]))
        if cvImg.shape[0] >960 or cvImg.shape[1] > 1440:
            cvImg = self.img_resize(cvImg)
        ccvImg = cvImg.copy()
        height, width, depth = ccvImg.shape
        
        ccvImg = cv2.cvtColor(ccvImg, cv2.COLOR_BGR2RGB)
        qtImg = QImage(ccvImg.data, width, height, width * depth, QImage.Format_RGB888)
        return QPixmap(qtImg), height, width, cvImg

    def img_resize(self, image):
        height, width = image.shape[0], image.shape[1]
        # 设置新的图片分辨率框架
        height_new = 960
        width_new = 1440
        # 判断图片的长宽比率
        if width / height >= width_new / height_new:
            img_new = cv2.resize(image, (width_new, int(height * width_new / width + 0.5)))
        else:
            img_new = cv2.resize(image, (int(width * height_new / height + 0.5), height_new))
        print("New_Height : %d, New_Width : %d" % (img_new.shape[0], img_new.shape[1]))
        return img_new

    def setup_control(self):
        self.filename = ""
        self.cImg_o = np.zeros((1,1,3), np.uint8)
        self.cImg_r = np.zeros((1,1,3), np.uint8)
        self.qImg = QPixmap("")
        self.img_height_r = 0
        self.img_width_r = 0
        self._window.OpenFile_action.triggered.connect(self.OpenFile)
        self._window.ROI_action.triggered.connect(self.ROI)
        self._window.Show_histogram_action.triggered.connect(self.Show_histogram)
        self._window.Show_change_colorspace_action.triggered.connect(self.Show_change_color_space)



class Show_Change_Color_Space_Window(QWidget):
    def __init__(self):
        super(Show_Change_Color_Space_Window, self).__init__()
        self.setWindowTitle("Show_change_colorspace")
        self.setFixedSize(700, 300)
        self.qlayout = QGridLayout()
        
        self.qslider1 =  QSlider(Qt.Horizontal)
        self.qslider1.setMinimum(0)  # 設定最小值
        self.qslider1.setMaximum(255)  # 設定最大值
        self.qslider1.setSingleStep(1)  # 步長
        self.qslider1.setTickPosition(QSlider.NoTicks)
        self.qlayout.addWidget(self.qslider1)

        self.qslider2 =  QSlider(Qt.Horizontal)
        self.qslider2.setMinimum(0)  # 設定最小值
        self.qslider2.setMaximum(255)  # 設定最大值
        self.qslider2.setSingleStep(1)  # 步長
        self.qslider2.setTickPosition(QSlider.NoTicks)
        self.qlayout.addWidget(self.qslider2)

        self.qslider3 =  QSlider(Qt.Horizontal)
        self.qslider3.setMinimum(0)  # 設定最小值
        self.qslider3.setMaximum(255)  # 設定最大值
        self.qslider3.setSingleStep(1)  # 步長
        self.qslider3.setTickPosition(QSlider.NoTicks)
        self.qlayout.addWidget(self.qslider3)

        self.qslider4 =  QSlider(Qt.Horizontal)
        self.qslider4.setMinimum(0)  # 設定最小值
        self.qslider4.setMaximum(255)  # 設定最大值
        self.qslider4.setSingleStep(1)  # 步長
        self.qslider4.setTickPosition(QSlider.NoTicks)
        self.qlayout.addWidget(self.qslider4)

        self.qslider5 =  QSlider(Qt.Horizontal)
        self.qslider5.setMinimum(0)  # 設定最小值
        self.qslider5.setMaximum(255)  # 設定最大值
        self.qslider5.setSingleStep(1)  # 步長
        self.qslider5.setTickPosition(QSlider.NoTicks)
        self.qlayout.addWidget(self.qslider5)

        self.qslider6 =  QSlider(Qt.Horizontal)
        self.qslider6.setMinimum(0)  # 設定最小值
        self.qslider6.setMaximum(255)  # 設定最大值
        self.qslider6.setSingleStep(1)  # 步長
        self.qslider6.setTickPosition(QSlider.NoTicks)
        self.qlayout.addWidget(self.qslider6)

        self.setLayout(self.qlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
 
    sys.exit(app.exec_())