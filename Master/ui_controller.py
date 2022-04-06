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
from ui_showhistogramwindow import Ui_ShowhistogramWinddow

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
            self.qImg, self.cImg_r = self.cvimgTOqtimg(self.cImg_o)
            self._window.Img_Lable.setPixmap(self.qImg)
            if self.qImg.size().width() >= 300:
                if self.qImg.size().height() >= 300:
                    self._window.Img_Lable.setFixedSize(self.qImg.size().width(), self.qImg.size().height())
                    self.setFixedSize(self.qImg.size().width(), self.qImg.size().height() + 45)
                else:
                    self._window.Img_Lable.setFixedSize(self.qImg.size().width(), 300)
                    self.setFixedSize(self.qImg.size().width(), 345)
            else:
                if self.qImg.size().height() >= 300:
                    self._window.Img_Lable.setFixedSize(300, self.qImg.size().height())
                    self.setFixedSize(300, self.qImg.size().height() + 45)
                else:
                    self._window.Img_Lable.setFixedSize(300, 300)
                    self.setFixedSize(300, 345)
            # print(QApplication.desktop().primaryScreen(), QApplication.desktop().screenGeometry(0))
            # self.move(((QApplication.desktop().width() - self.width())/2), ((QApplication.desktop().height() - self.height())/2) - 20)
            self._window.statusbar.showMessage(self.filename.split("/")[-1])
            
    def ROI(self):
        if self.filename != "":
            self.ROIWindow = Ui_ROIWindow(self.cImg_o, self.cImg_r, self.qImg)
            self.ROIWindow.show()
            print('ROI')
            # ROIWindow.move(((QApplication.desktop().width() - self.width())/2), ((QApplication.desktop().height() - self.height())/2) + 5)
 
    def Show_histogram(self):
        if self.filename != "":
            self.Showhistogram = Ui_ShowhistogramWinddow(self.cImg_o)
            self.Showhistogram.show()
            print('Showhistogram')
            # # 畫出 RGB 三種顏色的分佈圖
            # color=('b','g','r')
            # plt.style.use('dark_background')
            # for i,col in enumerate(color):
            #     hist=cv2.calcHist([self.cImg_o],[i],None,[256],[0,256])
            #     plt.plot(hist,color=col)#(一維陣列,線顏色)
            #     plt.xlim([0,256])#x範圍的值
            # plt.show()

    def Show_change_color_space(self):
        # self.ShowChange_ColorSpaceWindow = Show_Change_Color_Space_Window()
        # self.ShowChange_ColorSpaceWindow.show()
        None

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
        return QPixmap(qtImg), cvImg

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


    def closeEvent(self, event):
        QApplication.closeAllWindows()

    def setup_control(self):
        self.filename = ""
        self.cImg_o = np.zeros((1,1,3), np.uint8)
        self.cImg_r = np.zeros((1,1,3), np.uint8)
        self.qImg = QPixmap("")
        self._window.OpenFile_action.triggered.connect(self.OpenFile)
        self._window.ROI_action.triggered.connect(self.ROI)
        self._window.Show_histogram_action.triggered.connect(self.Show_histogram)
        self._window.Show_change_colorspace_action.triggered.connect(self.Show_change_color_space)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())