import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np


class Ui_Translate_Rotate_Window(QWidget):
    def __init__(self, imgwidth, imgheight):
        super(Ui_Translate_Rotate_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle(u"Translate Rotate (平移/旋轉)")
        self.setFixedSize(800, 150)
        self.imgwidth = imgwidth
        self.imgheight = imgheight
        self.smove = False
        self.seaved = False
        self.Translaterotate_img_o = np.zeros((1,1,3), np.uint8)
        self.Translaterotate_img_o_pad = 0
        self.Translaterotate_img_r = np.zeros((1,1,3), np.uint8)
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#####################################################################################
#xTranslate value
        self.xTranslate_HorizontalLayout = QHBoxLayout()

        self.xTranslate = QLabel()
        self.xTranslate.setText("X_Translate value")
        self.xTranslate.setMinimumSize(QSize(135, 0))
        self.xTranslate_HorizontalLayout.addWidget(self.xTranslate)

        self.xTranslate_Slider = QSlider()
        self.xTranslate_Slider.setMinimum(0 - (self.imgwidth))
        self.xTranslate_Slider.setMaximum(self.imgwidth)
        self.xTranslate_Slider.setValue(0)
        self.xTranslate_Slider.setOrientation(Qt.Horizontal)
        self.xTranslate_HorizontalLayout.addWidget(self.xTranslate_Slider)

        self.xTranslate_value = QLabel()
        sizePolicy.setHeightForWidth(self.xTranslate_value.sizePolicy().hasHeightForWidth())
        self.xTranslate_value.setSizePolicy(sizePolicy)
        self.xTranslate_value.setMinimumSize(QSize(45, 0))
        self.xTranslate_value.setText("0")
        self.xTranslate_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.xTranslate_HorizontalLayout.addWidget(self.xTranslate_value)


        self.main_verticalLayout.addLayout(self.xTranslate_HorizontalLayout)

#####################################################################################
#Translate value
        self.yTranslate_HorizontalLayout = QHBoxLayout()

        self.yTranslate = QLabel()
        self.yTranslate.setText("Y_Translate value")
        self.yTranslate.setMinimumSize(QSize(135, 0))
        self.yTranslate_HorizontalLayout.addWidget(self.yTranslate)

        self.yTranslate_Slider = QSlider()
        self.yTranslate_Slider.setMinimum(0 - (self.imgheight))
        self.yTranslate_Slider.setMaximum(self.imgheight)
        self.yTranslate_Slider.setValue(0)
        self.yTranslate_Slider.setOrientation(Qt.Horizontal)
        self.yTranslate_HorizontalLayout.addWidget(self.yTranslate_Slider)

        self.yTranslate_value = QLabel()
        sizePolicy.setHeightForWidth(self.yTranslate_value.sizePolicy().hasHeightForWidth())
        self.yTranslate_value.setSizePolicy(sizePolicy)
        self.yTranslate_value.setMinimumSize(QSize(45, 0))
        self.yTranslate_value.setText("0")
        self.yTranslate_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.yTranslate_HorizontalLayout.addWidget(self.yTranslate_value)


        self.main_verticalLayout.addLayout(self.yTranslate_HorizontalLayout)

#####################################################################################
#Rotate value
        self.Rotate_HorizontalLayout = QHBoxLayout()

        self.Rotate = QLabel()
        self.Rotate.setText("Rotate value")
        self.Rotate.setMinimumSize(QSize(135, 0))
        self.Rotate_HorizontalLayout.addWidget(self.Rotate)

        self.Rotate_Slider = QSlider()
        self.Rotate_Slider.setMaximum(360)
        self.Rotate_Slider.setValue(0)
        self.Rotate_Slider.setOrientation(Qt.Horizontal)
        self.Rotate_HorizontalLayout.addWidget(self.Rotate_Slider)

        self.Rotate_value = QLabel()
        sizePolicy.setHeightForWidth(self.Rotate_value.sizePolicy().hasHeightForWidth())
        self.Rotate_value.setSizePolicy(sizePolicy)
        self.Rotate_value.setMinimumSize(QSize(45, 0))
        self.Rotate_value.setText("0")
        self.Rotate_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Rotate_HorizontalLayout.addWidget(self.Rotate_value)

        self.main_verticalLayout.addLayout(self.Rotate_HorizontalLayout)

        self.setLayout(self.main_verticalLayout)

#####################################################################################

        self.xTranslate_Slider.valueChanged.connect(self.xTranslate_valueChanged)
        self.yTranslate_Slider.valueChanged.connect(self.yTranslate_valueChanged)
        self.Rotate_Slider.valueChanged.connect(self.Rotate_valueChanged)
        self.keyPressEvent = self.key_Press_Event


    def xTranslate_valueChanged(self):
        self.xTranslate_value.setText(f"{self.xTranslate_Slider.value()}")

    def yTranslate_valueChanged(self):
        self.yTranslate_value.setText(f"{self.yTranslate_Slider.value()}")

    def Rotate_valueChanged(self):
        self.Rotate_value.setText(f"{self.Rotate_Slider.value()}")

    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()

        if event.key() == Qt.Key_Delete or event.key() == Qt.Key_Backspace:
            self.xTranslate_Slider.setValue(0)
            self.yTranslate_Slider.setValue(0)
            self.Rotate_Slider.setValue(0)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ui_Translate_Rotate_Window(10000,10000)
#     window.show()
#     sys.exit(app.exec_())