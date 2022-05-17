import sys
import cv2
import math

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_main_window import Ui_Main_Window
from ui_roi_window import Ui_ROI_Window
from ui_show_histogram_window import Ui_Show_Histogram_Window
from ui_change_hsv_window import Ui_Change_Hsv_Window
from ui_image_thresholding_window import Ui_Image_Thresholding_Window
from ui_perspective_transform_window import Ui_Perspective_Transform_Window
from ui_translate_rotate_window import Ui_Translate_Rotate_Window
from ui_affine_transform_window import Ui_Affine_Transform_Window
from ui_image_filtering_window import Ui_Image_Filtering_Window
from ui_canny_edge_detection_window import Ui_Canny_Edge_Detection_Window
from ui_hough_line_transform_window import Ui_Hough_Line_Transform_Window
from ui_harris_corner_detection_window import Ui_Harris_Corner_Detection_Window
from ui_feature_detection_window import Ui_Feature_Detection_Window

import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._window = Ui_Main_Window()
        self._window.setupUi(self)
        self.setup_control()

    def OpenFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "OpenFile", "./Img", "Image Files(*.png *.jpg *.jpeg *.bmp *.tif)")
        if filename != "":
            self.filename = filename
            print("Open Path :", self.filename)
            self.cImg_o=cv2.imdecode(np.fromfile(self.filename,dtype=np.uint8),1)
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o)
            self.show_img()
            self.Statusbar_Message(self.filename.split("/")[-1])
            # print(QApplication.desktop().primaryScreen(), QApplication.desktop().screenGeometry(0))
            # self.move(((QApplication.desktop().width() - self.width())/2), ((QApplication.desktop().height() - self.height())/2) - 20)
            
    def SaveFile(self):
        if self.filename != "":
            filename, _ = QFileDialog.getSaveFileName(self, "SaveFile", "./", "Image Files(*.png *.jpg *.jpeg *.bmp *.tif)")
            if filename != "":
                cv2.imencode('.jpg', self.cImg_o)[1].tofile(filename)
                print("Save Path :", filename)
        else:
            self.Statusbar_Message("No Image")

    def ROI(self):
        if self.filename != "":
            print('ROI')
            self.ROIWindow = Ui_ROI_Window(self.cImg_o, self.cImg_r, self.qImg)
            self.ROIWindow.closeEvent = self.ROI_closeEvent
            self.ROIWindow.show()
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
            print('Show Histogram')
            self.Showhistogram = Ui_Show_Histogram_Window(self.cImg_o)
            self.Showhistogram.show()
        else:
            self.Statusbar_Message("No Image")
            
    def Change_HSV(self):
        if self.filename != "":
            print("Change HSV")
            self.ChangeHSV = Ui_Change_Hsv_Window()
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
        img = self.cImg_o.copy()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        self.ChangeHSV.HCV_img = cv2.bitwise_and(img, img, mask = mask)
        show_img, _, _ = self.cvimgTOqtimg(self.ChangeHSV.HCV_img, p = False)
        self._window.Img_Lable.setPixmap(show_img)

    def Change_HSV_closeEvent(self, event):
        if self.ChangeHSV.seaved:
            self.cImg_o = self.ChangeHSV.HCV_img
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o, p = False)
            self.show_img()
        else:
            self.show_img()

    def Change_GRAY(self):
        if self.filename != "":
            print("Change GRAY")
            self.qImg, self.cImg_r, self.cImg_o = self.cvimgTOqtimg(self.cImg_o, color = "GRAY")
            self.show_img()
        else:
            self.Statusbar_Message("No Image")

    def Show_Imgsize(self):
        if self.filename != "":
            print("Show Imgsize")
            information = f'Original :\n\tHeight : {self.cImg_o.shape[0]}\n\tWidth  : {self.cImg_o.shape[1]}\n'
            information += f'Show :\n\tHeight : {self.cImg_r.shape[0]}\n\tWidth  : {self.cImg_r.shape[1]}'
            QMessageBox.information(self, 'Image Size', information)
        else:
            self.Statusbar_Message("No Image")

    def Image_Thresholding(self):
        if self.filename != "":
            print("Image Thresholding")
            self.Imagethresholding = Ui_Image_Thresholding_Window()
            self.Imagethresholding.closeEvent = self.Image_Thresholding_closeEvent
            self.Imagethresholding.threshold_Slider.valueChanged.connect(self.Img_Image_Thresholding)
            self.Imagethresholding.maximum_Slider.valueChanged.connect(self.Img_Image_Thresholding)
            self.Imagethresholding.show()
            _, self.Imagethresholding.Imagethresholding_img = cv2.threshold(self.cImg_o, 127, 255, cv2.THRESH_BINARY)
            show_img, _, _ = self.cvimgTOqtimg(self.Imagethresholding.Imagethresholding_img, p = False)
            self._window.Img_Lable.setPixmap(show_img)
        else:
            self.Statusbar_Message("No Image")

    def Img_Image_Thresholding(self):
        Threshold_value = self.Imagethresholding.threshold_Slider.value()
        Maximum_value = self.Imagethresholding.maximum_Slider.value()
        _, self.Imagethresholding.Imagethresholding_img = cv2.threshold(self.cImg_o, Threshold_value, Maximum_value, cv2.THRESH_BINARY)
        show_img, _, _ = self.cvimgTOqtimg(self.Imagethresholding.Imagethresholding_img, p = False)
        self._window.Img_Lable.setPixmap(show_img)

    def Image_Thresholding_closeEvent(self, event):
        if self.Imagethresholding.seaved:
            self.cImg_o = self.Imagethresholding.Imagethresholding_img
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o)
            self.show_img()
        else:
            self.show_img()

    def Histogram_Equalization(self):
        if self.filename != "":
            print("Histogram Equalization")
            ycrcb = cv2.cvtColor(self.cImg_o, cv2.COLOR_BGR2YCR_CB)
            channels = cv2.split(ycrcb)
            cv2.equalizeHist(channels[0], channels[0])
            cv2.merge(channels, ycrcb)
            self.cImg_o = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, self.cImg_o)
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o)
            self.show_img()
        else:
            self.Statusbar_Message("No Image")

    def Perspective_Transform(self):
        if self.filename != "":
            print("Perspective Transform")
            self.Perspectivetransform = Ui_Perspective_Transform_Window(self.cImg_o, self.cImg_r, self.qImg)
            self.Perspectivetransform.closeEvent = self.Perspective_Transform_closeEvent
            self.Perspectivetransform.show()
        else:
            self.Statusbar_Message("No Image")

    def Perspective_Transform_closeEvent(self, event):
        if self.Perspectivetransform.seaved:
            self.cImg_o = self.Perspectivetransform.cPT_o
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o)
            self.show_img()

    def Translate_Rotate(self):
        if self.filename != "":
            print("Translate Rotate")
            self.Translaterotate = Ui_Translate_Rotate_Window(self.cImg_o.shape[1],self.cImg_o.shape[0])
            self.Translaterotate.xTranslate_Slider.valueChanged.connect(self.Img_Translate_Rotate)
            self.Translaterotate.yTranslate_Slider.valueChanged.connect(self.Img_Translate_Rotate)
            self.Translaterotate.Rotate_Slider.valueChanged.connect(self.Img_Translate_Rotate)
            self.Translaterotate.Resize_Slider.valueChanged.connect(self.Img_Translate_Rotate)
            self.Translaterotate.closeEvent = self.Translate_Rotate_closeEvent
            self.Translaterotate.show()
            self.Translaterotate.Translaterotate_img_o_pad = self.cImg_r.shape[0] if self.cImg_r.shape[0] > self.cImg_r.shape[1] else self.cImg_r.shape[1]
            pad = self.Translaterotate.Translaterotate_img_o_pad
            self.Translaterotate.Translaterotate_img_o = cv2.copyMakeBorder(self.cImg_r, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=(0, 0, 0))
            self.Translaterotate.Translaterotate_img_r = self.Translaterotate.Translaterotate_img_o.copy()
        else:
            self.Statusbar_Message("No Image")

    def Img_Translate_Rotate(self, val):
        Translate = self.Translaterotate
        if isinstance(val,int):
            y, x, _ = self.cImg_r.shape
            Ty, Tx, _ = Translate.Translaterotate_img_o.shape
            pad = Translate.Translaterotate_img_o_pad
            z = self.cImg_o.shape[0] / self.cImg_r.shape[0]
            xTranslate = Translate.xTranslate_Slider.value() / z
            yTranslate = Translate.yTranslate_Slider.value() / z
        else:
            Translate.Translaterotate_img_o_pad = self.cImg_o.shape[0] if self.cImg_o.shape[0] > self.cImg_o.shape[1] else self.cImg_o.shape[1]
            pad = Translate.Translaterotate_img_o_pad
            Translate.Translaterotate_img_o = cv2.copyMakeBorder(self.cImg_o, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=(0, 0, 0))
            Translate.Translaterotate_img_r = Translate.Translaterotate_img_o.copy()
            y, x, _ = self.cImg_o.shape
            Ty, Tx, _ = Translate.Translaterotate_img_o.shape
            xTranslate = Translate.xTranslate_Slider.value()
            yTranslate = Translate.yTranslate_Slider.value()

        Rotate = Translate.Rotate_Slider.value()
        Resize = (Translate.Resize_Slider.value() + 51) / 51

        M = np.float32([[1, 0, xTranslate], [0, 1, yTranslate]])
        Translate.Translaterotate_img_r = cv2.warpAffine(Translate.Translaterotate_img_o, M, (Tx, Ty))

        M = cv2.getRotationMatrix2D((Tx / 2 + xTranslate, Ty / 2 + yTranslate), Rotate, Resize)
        Translate.Translaterotate_img_r = cv2.warpAffine(Translate.Translaterotate_img_r, M, (Tx, Ty))

        show_img, _, _ = self.cvimgTOqtimg(Translate.Translaterotate_img_r[pad:pad + y, pad:pad + x], p = False)
        self._window.Img_Lable.setPixmap(show_img)

    def Translate_Rotate_closeEvent(self, event):
        if self.Translaterotate.seaved:
            self.Img_Translate_Rotate("")
            y, x, _ = self.cImg_o.shape
            pad = self.Translaterotate.Translaterotate_img_o_pad
            self.cImg_o = self.Translaterotate.Translaterotate_img_r[pad:pad + y, pad:pad + x]
            self.qImg, self.cImg_r, _ = self.cvimgTOqtimg(self.cImg_o)
            self.show_img()
        else:
            self.show_img()

    def Affine_Transform(self):
        if self.filename != "":
            print("Affine Transform")
            self.Affinetransform = Ui_Affine_Transform_Window(self)
            self.Affinetransform.show()
        else:
            self.Statusbar_Message("No Image")

    def Image_Filtering(self):
        if self.filename != "":
            print("Image Filtering")
            self.imagefiltering = Ui_Image_Filtering_Window(self)
            self.imagefiltering.show()
        else:
            self.Statusbar_Message("No Image")

    def Canny_Edge_Detection(self):
        if self.filename != "":
            print("Canny Edge Detection")
            self.cannyedgedetection = Ui_Canny_Edge_Detection_Window(self)
            self.cannyedgedetection.show()
        else:
            self.Statusbar_Message("No Image")

    def Hough_Line_Transform(self):
        if self.filename != "":
            print("Hough Line Transform")
            self.houghlinetransform = Ui_Hough_Line_Transform_Window(self)
            self.houghlinetransform.show()
        else:
            self.Statusbar_Message("No Image")

    def Harris_Corner_Detection(self):
        if self.filename != "":
            print("Harris Corner Detection")
            self.harriscornerdetection = Ui_Harris_Corner_Detection_Window(self)
            self.harriscornerdetection.show()
        else:
            self.Statusbar_Message("No Image")

    def Feature_Detection(self):
        if self.filename != "":
            print("Feature Detection")
            self.featuredetection = Ui_Feature_Detection_Window(self)
            self.featuredetection.show()
        else:
            self.Statusbar_Message("No Image")


    def show_img(self):
        self._window.Img_Lable.setPixmap(self.qImg)
        if self.qImg.size().width() >= 400:
            if self.qImg.size().height() >= 400:
                self._window.Img_Lable.setFixedSize(self.qImg.size().width(), self.qImg.size().height())
                self.setFixedSize(self.qImg.size().width(), self.qImg.size().height() + 45)
            else:
                self._window.Img_Lable.setFixedSize(self.qImg.size().width(), 400)
                self.setFixedSize(self.qImg.size().width(), 445)
        else:
            if self.qImg.size().height() >= 400:
                self._window.Img_Lable.setFixedSize(400, self.qImg.size().height())
                self.setFixedSize(400, self.qImg.size().height() + 45)
            else:
                self._window.Img_Lable.setFixedSize(400, 400)
                self.setFixedSize(400, 445)

    def cvimgTOqtimg(self, cvImg, color = "RGB", p = True):
        if p:print(f'Height : {cvImg.shape[0]}, Width : {cvImg.shape[1]}')
        ocvImg = cvImg.copy()
        if cvImg.shape[0] >960 or cvImg.shape[1] > 1440:
            cvImg = self.img_resize(cvImg, p)
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

    def img_resize(self, image, p = True):
        height, width = image.shape[0], image.shape[1]
        # 设置新的图片分辨率框架
        height_new = 960
        width_new = 1440
        # 判断图片的长宽比率
        if width / height >= width_new / height_new:
            img_new = cv2.resize(image, (width_new, int(height * width_new / width + 0.5)))
        else:
            img_new = cv2.resize(image, (int(width * height_new / height + 0.5), height_new))
        if p:print(f'Show_Height : {img_new.shape[0]}, Show_Width : {img_new.shape[1]}')
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
        self._window.Histogram_Equalization_action.triggered.connect(self.Histogram_Equalization)
        self._window.Perspective_Transform_action.triggered.connect(self.Perspective_Transform)
        self._window.Translate_Rotate_action.triggered.connect(self.Translate_Rotate)
        self._window.Affine_Transform_action.triggered.connect(self.Affine_Transform)
        self._window.Image_Filtering_action.triggered.connect(self.Image_Filtering)
        self._window.Canny_Edge_Detection_action.triggered.connect(self.Canny_Edge_Detection)
        self._window.Hough_Line_Transform_action.triggered.connect(self.Hough_Line_Transform)
        self._window.Harris_Corner_Detection_action.triggered.connect(self.Harris_Corner_Detection)
        self._window.Feature_Detection_action.triggered.connect(self.Feature_Detection)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())