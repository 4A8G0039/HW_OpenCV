import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import cv2
import numpy as np


class Ui_Blur(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Blur, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(820, 100)
        self.mainWindow = mainWindow
        self.seaved = False
        self.main_verticalLayout = QVBoxLayout()
        slide(self, name = ["x_ksize", "y_ksize"])
        self.setLayout(self.main_verticalLayout)

        self.s1_Slider.valueChanged.connect(self.img_update)
        self.s2_Slider.valueChanged.connect(self.img_update)

    def img_update(self):
        self.s1_v = (self.s1_Slider.value()) * 2 - 1
        self.s2_v = (self.s2_Slider.value()) * 2 - 1
        self.s1_value.setText(f"{self.s1_v}")
        self.s2_value.setText(f"{self.s2_v}")
        self.Imag = self.mainWindow.cImg_o.copy()
        self.Imag = cv2.blur(self.Imag, (self.s1_v, self.s2_v))
        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Imag, p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)



class Box_Filter(QWidget):
    def __init__(self, mainWindow):
        super(Box_Filter, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(820, 100)
        self.mainWindow = mainWindow
        self.seaved = False
        self.main_verticalLayout = QVBoxLayout()
        slide(self, name = ["x_ksize", "y_ksize"])
        self.setLayout(self.main_verticalLayout)

        self.s1_Slider.valueChanged.connect(self.img_update)
        self.s2_Slider.valueChanged.connect(self.img_update)

    def img_update(self):
        self.s1_v = (self.s1_Slider.value()) * 2 - 1
        self.s2_v = (self.s2_Slider.value()) * 2 - 1
        self.s1_value.setText(f"{self.s1_v}")
        self.s2_value.setText(f"{self.s2_v}")
        self.Imag = self.mainWindow.cImg_o.copy()
        self.Imag = cv2.boxFilter(self.Imag, -1, (self.s1_v, self.s2_v), normalize=True)
        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Imag, p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)



class Gaussian_Blur(QWidget):
    def __init__(self, mainWindow):
        super(Gaussian_Blur, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(820, 140)
        self.mainWindow = mainWindow
        self.seaved = False
        self.main_verticalLayout = QVBoxLayout()
        slide(self, type = 3, name = ["x_ksize", "y_ksize", "sigma"], Range = [0, 11, 0, 11, 0,11])
        self.setLayout(self.main_verticalLayout)

        self.s1_Slider.valueChanged.connect(self.img_update)
        self.s2_Slider.valueChanged.connect(self.img_update)
        self.s3_Slider.valueChanged.connect(self.img_update)

    def img_update(self):
        self.s1_v = (self.s1_Slider.value()) * 2 - 1 if self.s1_Slider.value() > 0 else 0
        self.s2_v = (self.s2_Slider.value()) * 2 - 1 if self.s2_Slider.value() > 0 else 0
        self.s3_v = (self.s3_Slider.value())
        self.s1_value.setText(f"{self.s1_v}")
        self.s2_value.setText(f"{self.s2_v}")
        self.s3_value.setText(f"{self.s3_v}")
        self.Imag = self.mainWindow.cImg_o.copy()
        self.Imag = cv2.GaussianBlur(self.Imag, (self.s1_v, self.s2_v), self.s3_v)
        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Imag, p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)



class Bilateral_Filter(QWidget):
    def __init__(self, mainWindow):
        super(Bilateral_Filter, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(820, 140)
        self.mainWindow = mainWindow
        self.seaved = False
        self.main_verticalLayout = QVBoxLayout()
        slide(self, type = 3, name = ["sigmaColor", "sigmaSpace", "d"], Range = [0, 150, 0, 10, 0,20])
        self.setLayout(self.main_verticalLayout)

        self.s1_Slider.valueChanged.connect(self.img_update)
        self.s2_Slider.valueChanged.connect(self.img_update)
        self.s3_Slider.valueChanged.connect(self.img_update)

    def img_update(self):
        self.s1_v = (self.s1_Slider.value())
        self.s2_v = (self.s2_Slider.value())
        self.s3_v = (self.s3_Slider.value())
        self.s1_value.setText(f"{self.s1_v}")
        self.s2_value.setText(f"{self.s2_v}")
        self.s3_value.setText(f"{self.s3_v}")
        self.Imag = self.mainWindow.cImg_o.copy()
        self.Imag = cv2.bilateralFilter(self.Imag, self.s3_v, self.s1_v, self.s2_v)
        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Imag, p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)



class Median_Blur(QWidget):
    def __init__(self, mainWindow):
        super(Median_Blur, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(820, 60)
        self.mainWindow = mainWindow
        self.seaved = False
        self.main_verticalLayout = QVBoxLayout()
        slide(self, type = 1, name = ["", "", "ksize"], Range = [0, 0, 0, 0, 1,6])
        self.setLayout(self.main_verticalLayout)

        self.s3_Slider.valueChanged.connect(self.img_update)

    def img_update(self):
        self.s3_v = (self.s3_Slider.value()) * 2 - 1
        self.s3_value.setText(f"{self.s3_v}")
        self.Imag = self.mainWindow.cImg_o.copy()
        self.Imag = cv2.medianBlur(self.Imag, self.s3_v)
        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Imag, p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)




def slide(Window, type = 2, name = ["s1", "s2", "s3"], Range = [1, 11, 1, 11, 0,10]):
    sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)

    if type == 2 or type == 3:
        Window.s1_horizontalLayout = QHBoxLayout()
        Window.s1 = QLabel()
        sizePolicy.setHeightForWidth(Window.s1.sizePolicy().hasHeightForWidth())
        Window.s1.setSizePolicy(sizePolicy)
        Window.s1.setMinimumSize(QSize(100, 0))
        Window.s1.setText(f"{name[0]} value")
        Window.s1_horizontalLayout.addWidget(Window.s1)

        Window.s1_Slider = QSlider()
        Window.s1_Slider.setRange(Range[0], Range[1])
        Window.s1_Slider.setPageStep(1)
        Window.s1_Slider.setValue(1)
        Window.s1_Slider.setOrientation(Qt.Horizontal)
        Window.s1_horizontalLayout.addWidget(Window.s1_Slider)

        Window.s1_value = QLabel()
        sizePolicy.setHeightForWidth(Window.s1_value.sizePolicy().hasHeightForWidth())
        Window.s1_value.setSizePolicy(sizePolicy)
        Window.s1_value.setMinimumSize(QSize(30, 0))
        Window.s1_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        Window.s1_horizontalLayout.addWidget(Window.s1_value)

        Window.main_verticalLayout.addLayout(Window.s1_horizontalLayout)


        Window.s2_horizontalLayout = QHBoxLayout()
        Window.s2 = QLabel()
        sizePolicy.setHeightForWidth(Window.s2.sizePolicy().hasHeightForWidth())
        Window.s2.setSizePolicy(sizePolicy)
        Window.s2.setMinimumSize(QSize(100, 0))
        Window.s2.setText(f"{name[1]} value")
        Window.s2_horizontalLayout.addWidget(Window.s2)

        Window.s2_Slider = QSlider()
        Window.s2_Slider.setRange(Range[2], Range[3])
        Window.s2_Slider.setPageStep(1)
        Window.s2_Slider.setValue(1)
        Window.s2_Slider.setOrientation(Qt.Horizontal)
        Window.s2_horizontalLayout.addWidget(Window.s2_Slider)
        
        Window.s2_value = QLabel()
        sizePolicy.setHeightForWidth(Window.s2_value.sizePolicy().hasHeightForWidth())
        Window.s2_value.setSizePolicy(sizePolicy)
        Window.s2_value.setMinimumSize(QSize(30, 0))
        Window.s2_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        Window.s2_horizontalLayout.addWidget(Window.s2_value)

        Window.main_verticalLayout.addLayout(Window.s2_horizontalLayout)

    if type == 3 or type == 1:
        Window.s3_horizontalLayout = QHBoxLayout()
        Window.s3 = QLabel()
        sizePolicy.setHeightForWidth(Window.s3.sizePolicy().hasHeightForWidth())
        Window.s3.setSizePolicy(sizePolicy)
        Window.s3.setMinimumSize(QSize(100, 0))
        Window.s3.setText(f"{name[2]} value")
        Window.s3_horizontalLayout.addWidget(Window.s3)

        Window.s3_Slider = QSlider()
        Window.s3_Slider.setRange(Range[4], Range[5])
        Window.s3_Slider.setPageStep(1)
        Window.s3_Slider.setValue(0)
        Window.s3_Slider.setOrientation(Qt.Horizontal)
        Window.s3_horizontalLayout.addWidget(Window.s3_Slider)
        
        Window.s3_value = QLabel()
        sizePolicy.setHeightForWidth(Window.s3_value.sizePolicy().hasHeightForWidth())
        Window.s3_value.setSizePolicy(sizePolicy)
        Window.s3_value.setMinimumSize(QSize(30, 0))
        Window.s3_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        Window.s3_horizontalLayout.addWidget(Window.s3_value)

        Window.main_verticalLayout.addLayout(Window.s3_horizontalLayout)

    

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ui_Blur()
#     window.show()
#     sys.exit(app.exec_())