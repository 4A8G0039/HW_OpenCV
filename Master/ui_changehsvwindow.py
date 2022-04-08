import sys
import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np


class Ui_ChangehsvWindow(QWidget):
    def __init__(self):
        super(Ui_ChangehsvWindow, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle(u"HSV")
        self.setFixedSize(700, 300)
        self.seaved = False
        self.HCV_img = np.zeros((1,1,3), np.uint8)
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#####################################################################################

        self.u_h_horizontalLayout = QHBoxLayout()
        self.Upper_label = QLabel()
        sizePolicy.setHeightForWidth(self.Upper_label.sizePolicy().hasHeightForWidth())
        self.Upper_label.setSizePolicy(sizePolicy)
        self.Upper_label.setMinimumSize(QSize(40, 0))
        self.Upper_label.setText("Upper :")
        self.u_h_horizontalLayout.addWidget(self.Upper_label)

        self.u_h = QLabel()
        self.u_h.setText('H')
        self.u_h_horizontalLayout.addWidget(self.u_h)

        self.u_h_Slider = QSlider()
        self.u_h_Slider.setMaximum(255)
        self.u_h_Slider.setValue(255)
        self.u_h_Slider.setOrientation(Qt.Horizontal)
        self.u_h_horizontalLayout.addWidget(self.u_h_Slider)

        self.u_h_v = QLabel()
        sizePolicy.setHeightForWidth(self.u_h_v.sizePolicy().hasHeightForWidth())
        self.u_h_v.setSizePolicy(sizePolicy)
        self.u_h_v.setMinimumSize(QSize(20, 0))
        self.u_h_v.setText("255")
        self.u_h_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.u_h_horizontalLayout.addWidget(self.u_h_v)


        self.main_verticalLayout.addLayout(self.u_h_horizontalLayout)

#####################################################################################

        self.u_s_horizontalLayout = QHBoxLayout()
        self.u_s_horizontalSpacer = QSpacerItem(52, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.u_s_horizontalLayout.addItem(self.u_s_horizontalSpacer)

        self.u_s = QLabel()
        self.u_s.setText("S")
        self.u_s_horizontalLayout.addWidget(self.u_s)

        self.u_s_Slider = QSlider()
        self.u_s_Slider.setMaximum(255)
        self.u_s_Slider.setValue(255)
        self.u_s_Slider.setOrientation(Qt.Horizontal)
        self.u_s_horizontalLayout.addWidget(self.u_s_Slider)

        self.u_s_v = QLabel()
        sizePolicy.setHeightForWidth(self.u_s_v.sizePolicy().hasHeightForWidth())
        self.u_s_v.setSizePolicy(sizePolicy)
        self.u_s_v.setMinimumSize(QSize(20, 0))
        self.u_s_v.setText("255")
        self.u_s_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.u_s_horizontalLayout.addWidget(self.u_s_v)

        self.main_verticalLayout.addLayout(self.u_s_horizontalLayout)

#####################################################################################

        self.u_v_horizontalLayout = QHBoxLayout()
        self.u_v_horizontalSpacer = QSpacerItem(52, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.u_v_horizontalLayout.addItem(self.u_v_horizontalSpacer)

        self.u_v = QLabel()
        self.u_v.setText("V")
        self.u_v_horizontalLayout.addWidget(self.u_v)

        self.u_v_Slider = QSlider()
        self.u_v_Slider.setMaximum(255)
        self.u_v_Slider.setValue(255)
        self.u_v_Slider.setOrientation(Qt.Horizontal)
        self.u_v_horizontalLayout.addWidget(self.u_v_Slider)

        self.u_v_v = QLabel()
        sizePolicy.setHeightForWidth(self.u_v_v.sizePolicy().hasHeightForWidth())
        self.u_v_v.setSizePolicy(sizePolicy)
        self.u_v_v.setMinimumSize(QSize(20, 0))
        self.u_v_v.setText("255")
        self.u_v_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.u_v_horizontalLayout.addWidget(self.u_v_v)

        self.main_verticalLayout.addLayout(self.u_v_horizontalLayout)

#####################################################################################  LINE


        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.main_verticalLayout.addWidget(self.line)


#####################################################################################  LINE

        self.l_h_horizontalLayout = QHBoxLayout()
        self.Lower_label = QLabel()
        sizePolicy.setHeightForWidth(self.Lower_label.sizePolicy().hasHeightForWidth())
        self.Lower_label.setSizePolicy(sizePolicy)
        self.Lower_label.setMinimumSize(QSize(40, 0))
        self.Lower_label.setText("Lower :")
        self.l_h_horizontalLayout.addWidget(self.Lower_label)

        self.l_h = QLabel()
        self.l_h.setText("H")
        self.l_h_horizontalLayout.addWidget(self.l_h)

        self.l_h_Slider = QSlider()
        self.l_h_Slider.setMaximum(250)
        self.l_h_Slider.setValue(0)
        self.l_h_Slider.setOrientation(Qt.Horizontal)
        self.l_h_horizontalLayout.addWidget(self.l_h_Slider)

        self.l_h_v = QLabel()
        sizePolicy.setHeightForWidth(self.l_h_v.sizePolicy().hasHeightForWidth())
        self.l_h_v.setSizePolicy(sizePolicy)
        self.l_h_v.setMinimumSize(QSize(20, 0))
        self.l_h_v.setText("0")
        self.l_h_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.l_h_horizontalLayout.addWidget(self.l_h_v)

        self.main_verticalLayout.addLayout(self.l_h_horizontalLayout)

#####################################################################################

        self.l_s_horizontalLayout = QHBoxLayout()
        self.l_s_horizontalSpacer = QSpacerItem(52, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.l_s_horizontalLayout.addItem(self.l_s_horizontalSpacer)

        self.l_s = QLabel()
        self.l_s.setText("S")
        self.l_s_horizontalLayout.addWidget(self.l_s)

        self.l_s_Slider = QSlider()
        self.l_s_Slider.setMaximum(250)
        self.l_s_Slider.setValue(0)
        self.l_s_Slider.setOrientation(Qt.Horizontal)
        self.l_s_horizontalLayout.addWidget(self.l_s_Slider)

        self.l_s_v = QLabel()
        sizePolicy.setHeightForWidth(self.l_s_v.sizePolicy().hasHeightForWidth())
        self.l_s_v.setSizePolicy(sizePolicy)
        self.l_s_v.setMinimumSize(QSize(20, 0))
        self.l_s_v.setText("0")
        self.l_s_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.l_s_horizontalLayout.addWidget(self.l_s_v)


        self.main_verticalLayout.addLayout(self.l_s_horizontalLayout)

#####################################################################################

        self.l_v_horizontalLayout = QHBoxLayout()
        self.l_v_horizontalSpacer = QSpacerItem(52, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.l_v_horizontalLayout.addItem(self.l_v_horizontalSpacer)

        self.l_v = QLabel()
        self.l_v.setText("V")
        self.l_v_horizontalLayout.addWidget(self.l_v)

        self.l_v_Slider = QSlider()
        self.l_v_Slider.setMaximum(250)
        self.l_v_Slider.setValue(0)
        self.l_v_Slider.setOrientation(Qt.Horizontal)
        self.l_v_horizontalLayout.addWidget(self.l_v_Slider)

        self.l_v_v = QLabel()
        sizePolicy.setHeightForWidth(self.l_v_v.sizePolicy().hasHeightForWidth())
        self.l_v_v.setSizePolicy(sizePolicy)
        self.l_v_v.setMinimumSize(QSize(20, 0))
        self.l_v_v.setText("0")
        self.l_v_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.l_v_horizontalLayout.addWidget(self.l_v_v)

        self.main_verticalLayout.addLayout(self.l_v_horizontalLayout)

        self.setLayout(self.main_verticalLayout)

#####################################################################################

        self.u_h_Slider.valueChanged.connect(self.u_h_valueChanged)
        self.u_s_Slider.valueChanged.connect(self.u_s_valueChanged)
        self.u_v_Slider.valueChanged.connect(self.u_v_valueChanged)
        self.l_h_Slider.valueChanged.connect(self.l_h_valueChanged)
        self.l_s_Slider.valueChanged.connect(self.l_s_valueChanged)
        self.l_v_Slider.valueChanged.connect(self.l_v_valueChanged)
        self.keyPressEvent = self.key_Press_Event


    def u_h_valueChanged(self):
        self.u_h_v.setText(f"{self.u_h_Slider.value()}")

    def u_s_valueChanged(self):
        self.u_s_v.setText(f"{self.u_s_Slider.value()}")

    def u_v_valueChanged(self):
        self.u_v_v.setText(f"{self.u_v_Slider.value()}")

    def l_h_valueChanged(self):
        self.l_h_v.setText(f"{self.l_h_Slider.value()}")

    def l_s_valueChanged(self):
        self.l_s_v.setText(f"{self.l_s_Slider.value()}")

    def l_v_valueChanged(self):
        self.l_v_v.setText(f"{self.l_v_Slider.value()}")

    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
                if self.u_h_Slider.value() != 255 or self.u_s_Slider.value() != 255 or self.u_v_Slider.value() != 255 or\
                        self.l_h_Slider.value() != 0 or self.l_s_Slider.value() != 0 or self.l_v_Slider.value() != 0:
                        self.seaved = True
                        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ui_ChangehsvWindow()
#     window.show()
#     sys.exit(app.exec_())
