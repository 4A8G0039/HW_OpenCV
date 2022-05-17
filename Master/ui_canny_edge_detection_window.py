import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Canny_Edge_Detection_Window(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Canny_Edge_Detection_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Canny Edge Detection (Canny邊緣檢測)")
        self.setFixedSize(700, 100)
        self.seaved = False
        self.mainWindow = mainWindow
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#####################################################################################
#Threshold_low value
        self.threshold_low_horizontalLayout = QHBoxLayout()

        self.threshold_low = QLabel()
        self.threshold_low.setMinimumSize(QSize(120, 0))
        self.threshold_low.setText("Threshold low value")
        self.threshold_low_horizontalLayout.addWidget(self.threshold_low)

        self.threshold_low_Slider = QSlider()
        self.threshold_low_Slider.setMaximum(255)
        self.threshold_low_Slider.setValue(0)
        self.threshold_low_Slider.setOrientation(Qt.Horizontal)
        self.threshold_low_horizontalLayout.addWidget(self.threshold_low_Slider)

        self.threshold_low_value = QLabel()
        sizePolicy.setHeightForWidth(self.threshold_low_value.sizePolicy().hasHeightForWidth())
        self.threshold_low_value.setSizePolicy(sizePolicy)
        self.threshold_low_value.setMinimumSize(QSize(30, 0))
        self.threshold_low_value.setText("0")
        self.threshold_low_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.threshold_low_horizontalLayout.addWidget(self.threshold_low_value)


        self.main_verticalLayout.addLayout(self.threshold_low_horizontalLayout)

#####################################################################################
#Ratio value
        self.ratio_horizontalLayout = QHBoxLayout()

        self.ratio = QLabel()
        self.ratio.setMinimumSize(QSize(120, 0))
        self.ratio.setText("Ratio value")
        self.ratio_horizontalLayout.addWidget(self.ratio)

        self.ratio_Slider = QSlider()
        self.ratio_Slider.setMaximum(40)
        self.ratio_Slider.setValue(0)
        self.ratio_Slider.setPageStep(1)
        self.ratio_Slider.setOrientation(Qt.Horizontal)
        self.ratio_horizontalLayout.addWidget(self.ratio_Slider)

        self.ratio_value = QLabel()
        sizePolicy.setHeightForWidth(self.ratio_value.sizePolicy().hasHeightForWidth())
        self.ratio_value.setSizePolicy(sizePolicy)
        self.ratio_value.setMinimumSize(QSize(30, 0))
        self.ratio_value.setText("1.0")
        self.ratio_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ratio_horizontalLayout.addWidget(self.ratio_value)

        self.main_verticalLayout.addLayout(self.ratio_horizontalLayout)

        self.setLayout(self.main_verticalLayout)

#####################################################################################
#Ksize value
        self.ksize_horizontalLayout = QHBoxLayout()

        self.ksize = QLabel()
        self.ksize.setMinimumSize(QSize(120, 0))
        self.ksize.setText("Ksize value")
        self.ksize_horizontalLayout.addWidget(self.ksize)

        self.ksize_Slider = QSlider()
        self.ksize_Slider.setRange(1, 6)
        self.ksize_Slider.setValue(1)
        self.ksize_Slider.setPageStep(1)
        self.ksize_Slider.setOrientation(Qt.Horizontal)
        self.ksize_horizontalLayout.addWidget(self.ksize_Slider)

        self.ksize_value = QLabel()
        sizePolicy.setHeightForWidth(self.ksize_value.sizePolicy().hasHeightForWidth())
        self.ksize_value.setSizePolicy(sizePolicy)
        self.ksize_value.setMinimumSize(QSize(30, 0))
        self.ksize_value.setText("1")
        self.ksize_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ksize_horizontalLayout.addWidget(self.ksize_value)

        self.main_verticalLayout.addLayout(self.ksize_horizontalLayout)

        self.setLayout(self.main_verticalLayout)

#####################################################################################

        self.threshold_low_Slider.valueChanged.connect(self.valueChanged)
        self.ratio_Slider.valueChanged.connect(self.valueChanged)
        self.ksize_Slider.valueChanged.connect(self.valueChanged)
        self.keyPressEvent = self.key_Press_Event
        self.closeEvent = self.close_Event

    def valueChanged(self):
        self.threshold_l_v = self.threshold_low_Slider.value()
        self.ratio_v = 1 + round(self.ratio_Slider.value() * 0.1, 1)
        self.ksize_v = (self.ksize_Slider.value()) * 2 - 1
        self.threshold_low_value.setText(f"{self.threshold_l_v}")
        self.ratio_value.setText(f"{self.ratio_v}")
        self.ksize_value.setText(f"{self.ksize_v}")
        if self.threshold_l_v == 0: show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
        else: show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Canny_Edge_Detector(), p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)

    def Canny_Edge_Detector(self):
        img = self.mainWindow.cImg_o.copy()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.blur(img_gray, (self.ksize_v, self.ksize_v))
        detected_edges = cv2.Canny(img_blur, self.threshold_l_v, int(self.threshold_l_v * self.ratio_v), self.ksize_v)
        mask = detected_edges != 0
        dst = img * (mask[:, :, None].astype(img.dtype))
        return dst

    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()

    def close_Event(self, event):
        if self.seaved:
            self.mainWindow.cImg_o = self.Canny_Edge_Detector()
            self.mainWindow.qImg, self.mainWindow.cImg_r, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
            self.mainWindow.show_img()
        else:
            self.mainWindow.show_img()
