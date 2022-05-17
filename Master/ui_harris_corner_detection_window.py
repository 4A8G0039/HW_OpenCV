import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np

class Ui_Harris_Corner_Detection_Window(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Harris_Corner_Detection_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Harris Corner Detection (Harris角點檢測)")
        self.setFixedSize(700, 100)
        self.seaved = False
        self.mainWindow = mainWindow
        self.threshold_v = 150
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#####################################################################################
#Threshold value
        self.threshold_horizontalLayout = QHBoxLayout()

        self.threshold = QLabel()
        self.threshold.setMinimumSize(QSize(120, 0))
        self.threshold.setText("Threshold value")
        self.threshold_horizontalLayout.addWidget(self.threshold)

        self.threshold_Slider = QSlider()
        self.threshold_Slider.setRange(110, 255)
        self.threshold_Slider.setValue(150)
        self.threshold_Slider.setOrientation(Qt.Horizontal)
        self.threshold_horizontalLayout.addWidget(self.threshold_Slider)

        self.threshold_value = QLabel()
        sizePolicy.setHeightForWidth(self.threshold_value.sizePolicy().hasHeightForWidth())
        self.threshold_value.setSizePolicy(sizePolicy)
        self.threshold_value.setMinimumSize(QSize(30, 0))
        self.threshold_value.setText("150")
        self.threshold_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.threshold_horizontalLayout.addWidget(self.threshold_value)


        self.main_verticalLayout.addLayout(self.threshold_horizontalLayout)

        self.setLayout(self.main_verticalLayout)


#####################################################################################

        self.threshold_Slider.valueChanged.connect(self.valueChanged)
        self.keyPressEvent = self.key_Press_Event
        self.closeEvent = self.close_Event

        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Harris_Corner_Detector(), p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)

    def valueChanged(self):
        self.threshold_v = self.threshold_Slider.value()
        self.threshold_value.setText(f"{self.threshold_v}")
        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Harris_Corner_Detector(), p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)

    def Harris_Corner_Detector(self):
        # Detector parameters
        blockSize = 2
        apertureSize = 3
        k = 0.04
        # Detecting corners
        img = self.mainWindow.cImg_o.copy()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dst = cv2.cornerHarris(img_gray, blockSize, apertureSize, k)
        # Normalizing
        dst_norm = np.empty(dst.shape, dtype = np.float32)
        cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        dst_norm_scaled = cv2.convertScaleAbs(dst_norm)
        # Drawing a circle around corners
        for i in range(dst_norm.shape[0]):
            for j in range(dst_norm.shape[1]):
                if int(dst_norm[i,j]) > self.threshold_v:
                    cv2.circle(img, (j,i), 5, (0, 0, 255), 1)
        return img

    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()

    def close_Event(self, event):
        if self.seaved:
            self.mainWindow.cImg_o = self.Harris_Corner_Detector()
            self.mainWindow.qImg, self.mainWindow.cImg_r, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
            self.mainWindow.show_img()
        else:
            self.mainWindow.show_img()
