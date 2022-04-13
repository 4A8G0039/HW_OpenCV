import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import cv2
import numpy as np


class Ui_Blur(QWidget):
    def __init__(self, Imag):
        super(Ui_Blur, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(700, 100)
        self.seaved = False
        self.Imag = Imag
        self.main_verticalLayout = QVBoxLayout()
        slide(self)
        self.setLayout(self.main_verticalLayout)

        self.s1_Slider.valueChanged.connect(self.img_update)
        self.s2_Slider.valueChanged.connect(self.img_update)

    def img_update(self):
        self.s1_v = (self.s1_Slider.value()) * 2 - 1
        self.s2_v = (self.s2_Slider.value()) * 2 - 1
        self.s1_value.setText(f"{self.s1_v}")
        self.s2_value.setText(f"{self.s2_v}")
        blur = cv2.blur(self.Imag, (self.s1_v, self.s2_v))
        cv2.imshow("blur", blur)



class Box_Filter(QWidget):
    def __init__(self, Imag):
        super(Box_Filter, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(700, 100)
        self.seaved = False
        self.Imag = Imag
        self.main_verticalLayout = QVBoxLayout()
        slide(self)
        self.setLayout(self.main_verticalLayout)

        self.s1_Slider.valueChanged.connect(self.img_update)
        self.s2_Slider.valueChanged.connect(self.img_update)

    def img_update(self):
        self.s1_v = (self.s1_Slider.value()) * 2 - 1
        self.s2_v = (self.s2_Slider.value()) * 2 - 1
        self.s1_value.setText(f"{self.s1_v}")
        self.s2_value.setText(f"{self.s2_v}")
        box = cv2.boxFilter(self.Imag, -1, (self.s1_v, self.s2_v), normalize=True)
        cv2.imshow("box", box)


def slide(Window):
    sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
#####################################################################################
#s1 value
    Window.s1_horizontalLayout = QHBoxLayout()

    Window.s1 = QLabel()
    Window.s1.setText("s1 value")
    Window.s1_horizontalLayout.addWidget(Window.s1)

    Window.s1_Slider = QSlider()
    Window.s1_Slider.setRange(1, 21)
    Window.s1_Slider.setPageStep(1)
    Window.s1_Slider.setValue(1)
    Window.s1_Slider.setOrientation(Qt.Horizontal)
    Window.s1_horizontalLayout.addWidget(Window.s1_Slider)

    Window.s1_value = QLabel()
    sizePolicy.setHeightForWidth(Window.s1_value.sizePolicy().hasHeightForWidth())
    Window.s1_value.setSizePolicy(sizePolicy)
    Window.s1_value.setMinimumSize(QSize(30, 0))
    Window.s1_value.setText("1")
    Window.s1_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
    Window.s1_horizontalLayout.addWidget(Window.s1_value)


    Window.main_verticalLayout.addLayout(Window.s1_horizontalLayout)

#####################################################################################
#s2 value
    Window.s2_horizontalLayout = QHBoxLayout()

    Window.s2 = QLabel()
    Window.s2.setText("s2 value")
    Window.s2_horizontalLayout.addWidget(Window.s2)

    Window.s2_Slider = QSlider()
    Window.s2_Slider.setRange(1, 21)
    Window.s2_Slider.setPageStep(1)
    Window.s2_Slider.setValue(1)
    Window.s2_Slider.setOrientation(Qt.Horizontal)
    Window.s2_horizontalLayout.addWidget(Window.s2_Slider)
    
    Window.s2_value = QLabel()
    sizePolicy.setHeightForWidth(Window.s2_value.sizePolicy().hasHeightForWidth())
    Window.s2_value.setSizePolicy(sizePolicy)
    Window.s2_value.setMinimumSize(QSize(30, 0))
    Window.s2_value.setText("1")
    Window.s2_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
    Window.s2_horizontalLayout.addWidget(Window.s2_value)

    Window.main_verticalLayout.addLayout(Window.s2_horizontalLayout)


#####################################################################################

    

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ui_Blur()
#     window.show()
#     sys.exit(app.exec_())