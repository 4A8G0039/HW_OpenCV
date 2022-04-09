import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np


class Ui_Image_Thresholding_Window(QWidget):
    def __init__(self):
        super(Ui_Image_Thresholding_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle(u"Image Thresholding (影像二值化)")
        self.setFixedSize(700, 100)
        self.seaved = False
        self.Imagethresholding_img = np.zeros((1,1,3), np.uint8)
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#####################################################################################
#Threshold value
        self.threshold_horizontalLayout = QHBoxLayout()

        self.threshold = QLabel()
        self.threshold.setText("Threshold value")
        self.threshold_horizontalLayout.addWidget(self.threshold)

        self.threshold_Slider = QSlider()
        self.threshold_Slider.setMinimum(-1)
        self.threshold_Slider.setMaximum(255)
        self.threshold_Slider.setValue(127)
        self.threshold_Slider.setOrientation(Qt.Horizontal)
        self.threshold_horizontalLayout.addWidget(self.threshold_Slider)

        self.threshold_value = QLabel()
        sizePolicy.setHeightForWidth(self.threshold_value.sizePolicy().hasHeightForWidth())
        self.threshold_value.setSizePolicy(sizePolicy)
        self.threshold_value.setMinimumSize(QSize(30, 0))
        self.threshold_value.setText("127")
        self.threshold_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.threshold_horizontalLayout.addWidget(self.threshold_value)


        self.main_verticalLayout.addLayout(self.threshold_horizontalLayout)

#####################################################################################
#Maximum value
        self.maximum_horizontalLayout = QHBoxLayout()

        self.maximum = QLabel()
        self.maximum.setText("Maximum value")
        self.maximum_horizontalLayout.addWidget(self.maximum)

        self.maximum_Slider = QSlider()
        self.maximum_Slider.setMaximum(255)
        self.maximum_Slider.setValue(255)
        self.maximum_Slider.setOrientation(Qt.Horizontal)
        self.maximum_horizontalLayout.addWidget(self.maximum_Slider)

        self.maximum_value = QLabel()
        sizePolicy.setHeightForWidth(self.maximum_value.sizePolicy().hasHeightForWidth())
        self.maximum_value.setSizePolicy(sizePolicy)
        self.maximum_value.setMinimumSize(QSize(30, 0))
        self.maximum_value.setText("255")
        self.maximum_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.maximum_horizontalLayout.addWidget(self.maximum_value)

        self.main_verticalLayout.addLayout(self.maximum_horizontalLayout)

        self.setLayout(self.main_verticalLayout)

#####################################################################################

        self.threshold_Slider.valueChanged.connect(self.threshold_valueChanged)
        self.maximum_Slider.valueChanged.connect(self.maximum_valueChanged)
        self.keyPressEvent = self.key_Press_Event


    def threshold_valueChanged(self):
        self.threshold_value.setText(f"{self.threshold_Slider.value()}")

    def maximum_valueChanged(self):
        self.maximum_value.setText(f"{self.maximum_Slider.value()}")

    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()