#designer
import sys
import cv2


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_mainwindow import Ui_MainWindow
from ui_roiwindow import Ui_ROIWindow
from ui_showhistogramwindow import Ui_ShowhistogramWindow
from ui_changehsvwindow import Ui_ChangehsvWindow
from ui_imagethresholdingwindow import Ui_ImagethresholdingWindow

import numpy as np
import matplotlib.pyplot as plt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._window = Ui_MainWindow()
        self._window.setupUi(self)
        self.setup_control()

    def OpenFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "OpenFile", "./", "Image Files(*.png *.jpg *.jpeg *.bmp *.tif)")
        if filename != "":
            self.filename = filename
            print("Open Path :", self.filename)
            self.cImg_o=cv2.imdecode(np.fromfile(self.filename,dtype=np.uint8),-1)
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o)
            self.show_img()
            self.Statusbar_Message(self.filename.split("/")[-1])
            # print(QApplication.desktop().primaryScreen(), QApplication.desktop().screenGeometry(0))
            # self.move(((QApplication.desktop().width() - self.width())/2), ((QApplication.desktop().height() - self.height())/2) - 20)
            
    def SaveFile(self):
        if self.filename != "":
            filename, _ = QFileDialog.getSaveFileName(self, "SaveFile", "./", "Image Files(*.png *.jpg *.jpeg *.bmp *.tif)")
            if filename != "":
                cv2.imencode('.png', self.cImg_o)[1].tofile(filename)
                print("Save Path :", filename)
        else:
            self.Statusbar_Message("No Image")


    def ROI(self):
        if self.filename != "":
            self.ROIWindow = Ui_ROIWindow(self.cImg_o, self.cImg_r, self.qImg)
            self.ROIWindow.closeEvent = self.ROI_closeEvent
            self.ROIWindow.show()
            print('ROI')
            # ROIWindow.move(((QApplication.desktop().width() - self.width())/2), ((QApplication.desktop().height() - self.height())/2) + 5)
        else:
            self.Statusbar_Message("No Image")

    def ROI_closeEvent(self, event):
        if self.ROIWindow.seaved:
            self.cImg_o = self.ROIWindow.cRoi_o
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o)
            self.show_img()
        

    def Show_Histogram(self):
        if self.filename != "":
            self.Showhistogram = Ui_ShowhistogramWindow(self.cImg_o)
            self.Showhistogram.show()
            print('Showhistogram')
        else:
            self.Statusbar_Message("No Image")
            
    def Change_HSV(self):
        if self.filename != "":
            self.ChangeHSV = Ui_ChangehsvWindow()
            self.ChangeHSV.u_h_Slider.valueChanged.connect(self.Img_Change_HSV)
            self.ChangeHSV.u_s_Slider.valueChanged.connect(self.Img_Change_HSV)
            self.ChangeHSV.u_v_Slider.valueChanged.connect(self.Img_Change_HSV)
            self.ChangeHSV.l_h_Slider.valueChanged.connect(self.Img_Change_HSV)
            self.ChangeHSV.l_s_Slider.valueChanged.connect(self.Img_Change_HSV)
            self.ChangeHSV.l_v_Slider.valueChanged.connect(self.Img_Change_HSV)
            self.ChangeHSV.closeEvent = self.Change_HSV_closeEvent
            self.ChangeHSV.show()
        else:
            self.Statusbar_Message("No Image")

    def Img_Change_HSV(self):
        CHSV = self.ChangeHSV
        upper = np.array([CHSV.u_h_Slider.value(), CHSV.u_s_Slider.value(), CHSV.u_v_Slider.value()])
        lower = np.array([CHSV.l_h_Slider.value(), CHSV.l_s_Slider.value(), CHSV.l_v_Slider.value()])
        print(upper)
        print(lower)
        img = self.cImg_o.copy()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        self.ChangeHSV.HCV_img = cv2.bitwise_and(img, img, mask = mask)
        show_img, _, _ = self.cvimgTOqtimg(self.ChangeHSV.HCV_img)
        self._window.Img_Lable.setPixmap(show_img)

    def Change_HSV_closeEvent(self, event):
        if self.ChangeHSV.seaved:
            self.cImg_o = self.ChangeHSV.HCV_img
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o)
            self.show_img()
        else:
            self.show_img()

    def Change_GRAY(self):
        if self.filename != "":
            self.qImg, self.cImg_r, self.cImg_o = self.cvimgTOqtimg(self.cImg_o, color = "GRAY")
            self.show_img()
        else:
            self.Statusbar_Message("No Image")

    def Show_Imgsize(self):
        if self.filename != "":
            information = f'Original :\n\tHeight : {self.cImg_o.shape[0]}\n\tWidth  : {self.cImg_o.shape[1]}\n'
            information += f'Show :\n\tHeight : {self.cImg_r.shape[0]}\n\tWidth  : {self.cImg_r.shape[1]}'
            QMessageBox.information(self, 'Image Size', information)
        else:
            self.Statusbar_Message("No Image")

    def Image_Thresholding(self):
        if self.filename != "":
            self.Imagethresholding = Ui_ImagethresholdingWindow()
            self.Imagethresholding.closeEvent = self.Image_Thresholding_closeEvent
            self.Imagethresholding.threshold_Slider.valueChanged.connect(self.Img_Image_Thresholding)
            self.Imagethresholding.maximum_Slider.valueChanged.connect(self.Img_Image_Thresholding)
            self.Imagethresholding.show()
            _, self.Imagethresholding.Imagethresholding_img = cv2.threshold(self.cImg_o, 127, 255, cv2.THRESH_BINARY)
            show_img, _, _ = self.cvimgTOqtimg(self.Imagethresholding.Imagethresholding_img)
            self._window.Img_Lable.setPixmap(show_img)
        else:
            self.Statusbar_Message("No Image")

    def Img_Image_Thresholding(self):
        Threshold_value = self.Imagethresholding.threshold_Slider.value()
        Maximum_value = self.Imagethresholding.maximum_Slider.value()
        _, self.Imagethresholding.Imagethresholding_img = cv2.threshold(self.cImg_o, Threshold_value, Maximum_value, cv2.THRESH_BINARY)
        show_img, _, _ = self.cvimgTOqtimg(self.Imagethresholding.Imagethresholding_img)
        self._window.Img_Lable.setPixmap(show_img)

    def Image_Thresholding_closeEvent(self, event):
        if self.Imagethresholding.seaved:
            self.cImg_o = self.Imagethresholding.Imagethresholding_img
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o)
            self.show_img()
        else:
            self.show_img()

    def show_img(self):
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

    def cvimgTOqtimg(self, cvImg, color = "RGB"):
        print(f'Height : {cvImg.shape[0]}, Width : {cvImg.shape[1]}')
        ocvImg = cvImg.copy()
        if cvImg.shape[0] >960 or cvImg.shape[1] > 1440:
            cvImg = self.img_resize(cvImg)
        if color == "RGB":
            ccvImg = cvImg.copy()
            height, width, depth = ccvImg.shape
            ccvImg = cv2.cvtColor(ccvImg, cv2.COLOR_BGR2RGB)
            qtImg = QImage(ccvImg.data, width, height, width * depth, QImage.Format_RGB888)
        elif color == "GRAY":
            ocvImg = cv2.cvtColor(ocvImg, cv2.COLOR_BGR2GRAY)
            ocvImg = cv2.cvtColor(ocvImg, cv2.COLOR_GRAY2BGR)
            cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
            cvImg = cv2.cvtColor(cvImg, cv2.COLOR_GRAY2BGR)
            height, width, depth = cvImg.shape
            qtImg = QImage(cvImg.data, width, height, width * depth, QImage.Format_RGB888)
        return QPixmap(qtImg), cvImg, ocvImg

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
        print(f'Show_Height : {img_new.shape[0]}, Show_Width : {img_new.shape[1]}')
        return img_new

    def Statusbar_Message(self, message):
        self._window.statusbar.showMessage(message)

    def closeEvent(self, event):
        QApplication.closeAllWindows()

    def setup_control(self):
        self.filename = ""
        self.cImg_o = np.zeros((1,1,3), np.uint8)
        self.cImg_r = np.zeros((1,1,3), np.uint8)
        self.qImg = QPixmap("")
        self.closeEvent = self.closeEvent
        self._window.OpenFile_action.triggered.connect(self.OpenFile)
        self._window.SaveFile_action.triggered.connect(self.SaveFile)
        self._window.ROI_action.triggered.connect(self.ROI)
        self._window.Show_Histogram_action.triggered.connect(self.Show_Histogram)
        self._window.Show_Imgsize_action.triggered.connect(self.Show_Imgsize)
        self._window.Change_HSV_action.triggered.connect(self.Change_HSV)
        self._window.Change_GRAY_action.triggered.connect(self.Change_GRAY)
        self._window.Image_Thresholding_action.triggered.connect(self.Image_Thresholding)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())