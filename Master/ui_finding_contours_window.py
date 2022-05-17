import cv2
import random
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np

class Ui_Finding_Contours_Window(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Finding_Contours_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Finding contours (尋找輪廓)")
        self.setFixedSize(700, 50)
        self.mainWindow = mainWindow
        self.seaved = False
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#####################################################################################
#Threshold value
        self.threshold_horizontalLayout = QHBoxLayout()

        self.threshold = QLabel()
        self.threshold.setMinimumSize(QSize(100, 0))
        self.threshold.setText("Threshold value")
        self.threshold_horizontalLayout.addWidget(self.threshold)

        self.threshold_Slider = QSlider()
        self.threshold_Slider.setMaximum(226)
        self.threshold_Slider.setValue(0)
        self.threshold_Slider.setOrientation(Qt.Horizontal)
        self.threshold_horizontalLayout.addWidget(self.threshold_Slider)

        self.threshold_value = QLabel()
        sizePolicy.setHeightForWidth(self.threshold_value.sizePolicy().hasHeightForWidth())
        self.threshold_value.setSizePolicy(sizePolicy)
        self.threshold_value.setMinimumSize(QSize(30, 0))
        self.threshold_value.setText("0")
        self.threshold_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.threshold_horizontalLayout.addWidget(self.threshold_value)


        self.main_verticalLayout.addLayout(self.threshold_horizontalLayout)

        self.setLayout(self.main_verticalLayout)


#####################################################################################

        self.threshold_Slider.valueChanged.connect(self.valueChanged)
        self.keyPressEvent = self.key_Press_Event
        self.closeEvent = self.close_Event


    def valueChanged(self):
        self.threshold_v = self.threshold_Slider.value()
        self.threshold_v += 29 if self.threshold_Slider.value() > 0 else 0
        self.threshold_value.setText(f"{self.threshold_v}")
        if self.threshold_v == 0: show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
        else: show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Finding_Contours(), p = False)
        self.mainWindow.show_img(show_img)

    def Finding_Contours(self):
        threshold = self.threshold_v
        src = self.mainWindow.cImg_o.copy()
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        src_gray = cv2.blur(src_gray, (3,3))
        # Detect edges using Canny
        canny_output = cv2.Canny(src_gray, threshold, threshold * 2)
        # Find contours
        contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # Draw contours
        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        for i in range(len(contours)):
            color = (random.randint(0,256), random.randint(0,256), random.randint(0,256))
            cv2.drawContours(drawing, contours, i, color, 2, cv2.LINE_8, hierarchy, 0)
        return drawing

    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()

    def close_Event(self, event):
        if self.seaved and self.threshold_v != 0:
            self.mainWindow.cImg_o = self.Finding_Contours()
            self.mainWindow.qImg, self.mainWindow.cImg_r, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
            self.mainWindow.show_img()
        else:
            self.mainWindow.show_img()
