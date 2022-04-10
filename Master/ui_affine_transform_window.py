import sys
import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np

class Ui_Affine_Transform_Window(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Affine_Transform_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle(u"Affine Transform (仿射轉換)")
        self.setFixedSize(700, 400)
        self.mainWindow = mainWindow
        self.imgwidth = self.mainWindow.cImg_o.shape[1]
        self.imgheight = self.mainWindow.cImg_o.shape[0]
        self.seaved = False
        self.Affinetransform = np.zeros((1,1,3), np.uint8)
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


#Original
#####################################################################################
#X1
        self.o_x1_horizontalLayout = QHBoxLayout()
        self.Original_label = QLabel()
        sizePolicy.setHeightForWidth(self.Original_label.sizePolicy().hasHeightForWidth())
        self.Original_label.setSizePolicy(sizePolicy)
        self.Original_label.setMinimumSize(QSize(80, 0))
        self.Original_label.setText("Original :")
        self.o_x1_horizontalLayout.addWidget(self.Original_label)

        self.o_x1 = QLabel()
        self.o_x1.setText('X1')
        self.o_x1_horizontalLayout.addWidget(self.o_x1)

        self.o_x1_Slider = QSlider()
        self.o_x1_Slider.setMaximum(self.imgwidth)
        self.o_x1_Slider.setValue(0)
        self.o_x1_Slider.setOrientation(Qt.Horizontal)
        self.o_x1_horizontalLayout.addWidget(self.o_x1_Slider)

        self.o_x1_v = QLabel()
        sizePolicy.setHeightForWidth(self.o_x1_v.sizePolicy().hasHeightForWidth())
        self.o_x1_v.setSizePolicy(sizePolicy)
        self.o_x1_v.setMinimumSize(QSize(45, 0))
        self.o_x1_v.setText("0")
        self.o_x1_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.o_x1_horizontalLayout.addWidget(self.o_x1_v)


        self.main_verticalLayout.addLayout(self.o_x1_horizontalLayout)

#####################################################################################
#Y1
        self.o_y1_horizontalLayout = QHBoxLayout()
        self.o_y1_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.o_y1_horizontalLayout.addItem(self.o_y1_horizontalSpacer)

        self.o_y1 = QLabel()
        self.o_y1.setText("Y1")
        self.o_y1_horizontalLayout.addWidget(self.o_y1)

        self.o_y1_Slider = QSlider()
        self.o_y1_Slider.setMaximum(self.imgheight)
        self.o_y1_Slider.setValue(0)
        self.o_y1_Slider.setOrientation(Qt.Horizontal)
        self.o_y1_horizontalLayout.addWidget(self.o_y1_Slider)

        self.o_y1_v = QLabel()
        sizePolicy.setHeightForWidth(self.o_y1_v.sizePolicy().hasHeightForWidth())
        self.o_y1_v.setSizePolicy(sizePolicy)
        self.o_y1_v.setMinimumSize(QSize(45, 0))
        self.o_y1_v.setText("0")
        self.o_y1_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.o_y1_horizontalLayout.addWidget(self.o_y1_v)

        self.main_verticalLayout.addLayout(self.o_y1_horizontalLayout)

#####################################################################################
#X2
        self.o_x2_horizontalLayout = QHBoxLayout()
        self.o_x2_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.o_x2_horizontalLayout.addItem(self.o_x2_horizontalSpacer)

        self.o_x2 = QLabel()
        self.o_x2.setText("X2")
        self.o_x2_horizontalLayout.addWidget(self.o_x2)

        self.o_x2_Slider = QSlider()
        self.o_x2_Slider.setMaximum(self.imgwidth)
        self.o_x2_Slider.setValue(self.imgwidth)
        self.o_x2_Slider.setOrientation(Qt.Horizontal)
        self.o_x2_horizontalLayout.addWidget(self.o_x2_Slider)

        self.o_x2_v = QLabel()
        sizePolicy.setHeightForWidth(self.o_x2_v.sizePolicy().hasHeightForWidth())
        self.o_x2_v.setSizePolicy(sizePolicy)
        self.o_x2_v.setMinimumSize(QSize(45, 0))
        self.o_x2_v.setText(f"{self.imgwidth}")
        self.o_x2_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.o_x2_horizontalLayout.addWidget(self.o_x2_v)

        self.main_verticalLayout.addLayout(self.o_x2_horizontalLayout)

#####################################################################################
#Y2
        self.o_y2_horizontalLayout = QHBoxLayout()
        self.o_y2_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.o_y2_horizontalLayout.addItem(self.o_y2_horizontalSpacer)

        self.o_y2 = QLabel()
        self.o_y2.setText('Y2')
        self.o_y2_horizontalLayout.addWidget(self.o_y2)

        self.o_y2_Slider = QSlider()
        self.o_y2_Slider.setMaximum(self.imgheight)
        self.o_y2_Slider.setValue(0)
        self.o_y2_Slider.setOrientation(Qt.Horizontal)
        self.o_y2_horizontalLayout.addWidget(self.o_y2_Slider)

        self.o_y2_v = QLabel()
        sizePolicy.setHeightForWidth(self.o_y2_v.sizePolicy().hasHeightForWidth())
        self.o_y2_v.setSizePolicy(sizePolicy)
        self.o_y2_v.setMinimumSize(QSize(45, 0))
        self.o_y2_v.setText("0")
        self.o_y2_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.o_y2_horizontalLayout.addWidget(self.o_y2_v)


        self.main_verticalLayout.addLayout(self.o_y2_horizontalLayout)

#####################################################################################
#X3
        self.o_x3_horizontalLayout = QHBoxLayout()
        self.o_x3_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.o_x3_horizontalLayout.addItem(self.o_x3_horizontalSpacer)

        self.o_x3 = QLabel()
        self.o_x3.setText("X3")
        self.o_x3_horizontalLayout.addWidget(self.o_x3)

        self.o_x3_Slider = QSlider()
        self.o_x3_Slider.setMaximum(self.imgwidth)
        self.o_x3_Slider.setValue(0)
        self.o_x3_Slider.setOrientation(Qt.Horizontal)
        self.o_x3_horizontalLayout.addWidget(self.o_x3_Slider)

        self.o_x3_v = QLabel()
        sizePolicy.setHeightForWidth(self.o_x3_v.sizePolicy().hasHeightForWidth())
        self.o_x3_v.setSizePolicy(sizePolicy)
        self.o_x3_v.setMinimumSize(QSize(45, 0))
        self.o_x3_v.setText("0")
        self.o_x3_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.o_x3_horizontalLayout.addWidget(self.o_x3_v)

        self.main_verticalLayout.addLayout(self.o_x3_horizontalLayout)

#####################################################################################
#Y3
        self.o_y3_horizontalLayout = QHBoxLayout()
        self.o_y3_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.o_y3_horizontalLayout.addItem(self.o_y3_horizontalSpacer)

        self.o_y3 = QLabel()
        self.o_y3.setText("Y3")
        self.o_y3_horizontalLayout.addWidget(self.o_y3)

        self.o_y3_Slider = QSlider()
        self.o_y3_Slider.setMaximum(self.imgheight)
        self.o_y3_Slider.setValue(self.imgheight)
        self.o_y3_Slider.setOrientation(Qt.Horizontal)
        self.o_y3_horizontalLayout.addWidget(self.o_y3_Slider)

        self.o_y3_v = QLabel()
        sizePolicy.setHeightForWidth(self.o_y3_v.sizePolicy().hasHeightForWidth())
        self.o_y3_v.setSizePolicy(sizePolicy)
        self.o_y3_v.setMinimumSize(QSize(45, 0))
        self.o_y3_v.setText(f"{self.imgheight}")
        self.o_y3_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.o_y3_horizontalLayout.addWidget(self.o_y3_v)

        self.main_verticalLayout.addLayout(self.o_y3_horizontalLayout)

#LINE
#####################################################################################

        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.main_verticalLayout.addWidget(self.line)

#Destination 
#####################################################################################
#X1
        self.d_x1_horizontalLayout = QHBoxLayout()
        self.Destination_label = QLabel()
        sizePolicy.setHeightForWidth(self.Destination_label.sizePolicy().hasHeightForWidth())
        self.Destination_label.setSizePolicy(sizePolicy)
        self.Destination_label.setMinimumSize(QSize(80, 0))
        self.Destination_label.setText("Destination :")
        self.d_x1_horizontalLayout.addWidget(self.Destination_label)

        self.d_x1 = QLabel()
        self.d_x1.setText('X1')
        self.d_x1_horizontalLayout.addWidget(self.d_x1)

        self.d_x1_Slider = QSlider()
        self.d_x1_Slider.setMaximum(self.imgwidth)
        self.d_x1_Slider.setValue(0)
        self.d_x1_Slider.setOrientation(Qt.Horizontal)
        self.d_x1_horizontalLayout.addWidget(self.d_x1_Slider)

        self.d_x1_v = QLabel()
        sizePolicy.setHeightForWidth(self.d_x1_v.sizePolicy().hasHeightForWidth())
        self.d_x1_v.setSizePolicy(sizePolicy)
        self.d_x1_v.setMinimumSize(QSize(45, 0))
        self.d_x1_v.setText("0")
        self.d_x1_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.d_x1_horizontalLayout.addWidget(self.d_x1_v)


        self.main_verticalLayout.addLayout(self.d_x1_horizontalLayout)

#####################################################################################
#Y1
        self.d_y1_horizontalLayout = QHBoxLayout()
        self.d_y1_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.d_y1_horizontalLayout.addItem(self.d_y1_horizontalSpacer)

        self.d_y1 = QLabel()
        self.d_y1.setText("Y1")
        self.d_y1_horizontalLayout.addWidget(self.d_y1)

        self.d_y1_Slider = QSlider()
        self.d_y1_Slider.setMaximum(self.imgheight)
        self.d_y1_Slider.setValue(0)
        self.d_y1_Slider.setOrientation(Qt.Horizontal)
        self.d_y1_horizontalLayout.addWidget(self.d_y1_Slider)

        self.d_y1_v = QLabel()
        sizePolicy.setHeightForWidth(self.d_y1_v.sizePolicy().hasHeightForWidth())
        self.d_y1_v.setSizePolicy(sizePolicy)
        self.d_y1_v.setMinimumSize(QSize(45, 0))
        self.d_y1_v.setText("0")
        self.d_y1_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.d_y1_horizontalLayout.addWidget(self.d_y1_v)

        self.main_verticalLayout.addLayout(self.d_y1_horizontalLayout)

#####################################################################################
#X2
        self.d_x2_horizontalLayout = QHBoxLayout()
        self.d_x2_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.d_x2_horizontalLayout.addItem(self.d_x2_horizontalSpacer)

        self.d_x2 = QLabel()
        self.d_x2.setText("X2")
        self.d_x2_horizontalLayout.addWidget(self.d_x2)

        self.d_x2_Slider = QSlider()
        self.d_x2_Slider.setMaximum(self.imgwidth)
        self.d_x2_Slider.setValue(self.imgwidth)
        self.d_x2_Slider.setOrientation(Qt.Horizontal)
        self.d_x2_horizontalLayout.addWidget(self.d_x2_Slider)

        self.d_x2_v = QLabel()
        sizePolicy.setHeightForWidth(self.d_x2_v.sizePolicy().hasHeightForWidth())
        self.d_x2_v.setSizePolicy(sizePolicy)
        self.d_x2_v.setMinimumSize(QSize(45, 0))
        self.d_x2_v.setText(f"{self.imgwidth}")
        self.d_x2_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.d_x2_horizontalLayout.addWidget(self.d_x2_v)

        self.main_verticalLayout.addLayout(self.d_x2_horizontalLayout)

#####################################################################################
#Y2
        self.d_y2_horizontalLayout = QHBoxLayout()
        self.d_y2_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.d_y2_horizontalLayout.addItem(self.d_y2_horizontalSpacer)

        self.d_y2 = QLabel()
        self.d_y2.setText('Y2')
        self.d_y2_horizontalLayout.addWidget(self.d_y2)

        self.d_y2_Slider = QSlider()
        self.d_y2_Slider.setMaximum(self.imgheight)
        self.d_y2_Slider.setValue(0)
        self.d_y2_Slider.setOrientation(Qt.Horizontal)
        self.d_y2_horizontalLayout.addWidget(self.d_y2_Slider)

        self.d_y2_v = QLabel()
        sizePolicy.setHeightForWidth(self.d_y2_v.sizePolicy().hasHeightForWidth())
        self.d_y2_v.setSizePolicy(sizePolicy)
        self.d_y2_v.setMinimumSize(QSize(45, 0))
        self.d_y2_v.setText("0")
        self.d_y2_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.d_y2_horizontalLayout.addWidget(self.d_y2_v)


        self.main_verticalLayout.addLayout(self.d_y2_horizontalLayout)

#####################################################################################
#X3
        self.d_x3_horizontalLayout = QHBoxLayout()
        self.d_x3_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.d_x3_horizontalLayout.addItem(self.d_x3_horizontalSpacer)

        self.d_x3 = QLabel()
        self.d_x3.setText("X3")
        self.d_x3_horizontalLayout.addWidget(self.d_x3)

        self.d_x3_Slider = QSlider()
        self.d_x3_Slider.setMaximum(self.imgwidth)
        self.d_x3_Slider.setValue(0)
        self.d_x3_Slider.setOrientation(Qt.Horizontal)
        self.d_x3_horizontalLayout.addWidget(self.d_x3_Slider)

        self.d_x3_v = QLabel()
        sizePolicy.setHeightForWidth(self.d_x3_v.sizePolicy().hasHeightForWidth())
        self.d_x3_v.setSizePolicy(sizePolicy)
        self.d_x3_v.setMinimumSize(QSize(45, 0))
        self.d_x3_v.setText("0")
        self.d_x3_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.d_x3_horizontalLayout.addWidget(self.d_x3_v)

        self.main_verticalLayout.addLayout(self.d_x3_horizontalLayout)

#####################################################################################
#Y3
        self.d_y3_horizontalLayout = QHBoxLayout()
        self.d_y3_horizontalSpacer = QSpacerItem(86, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.d_y3_horizontalLayout.addItem(self.d_y3_horizontalSpacer)

        self.d_y3 = QLabel()
        self.d_y3.setText("Y3")
        self.d_y3_horizontalLayout.addWidget(self.d_y3)

        self.d_y3_Slider = QSlider()
        self.d_y3_Slider.setMaximum(self.imgheight)
        self.d_y3_Slider.setValue(self.imgheight)
        self.d_y3_Slider.setOrientation(Qt.Horizontal)
        self.d_y3_horizontalLayout.addWidget(self.d_y3_Slider)

        self.d_y3_v = QLabel()
        sizePolicy.setHeightForWidth(self.d_y3_v.sizePolicy().hasHeightForWidth())
        self.d_y3_v.setSizePolicy(sizePolicy)
        self.d_y3_v.setMinimumSize(QSize(45, 0))
        self.d_y3_v.setText(f"{self.imgheight}")
        self.d_y3_v.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.d_y3_horizontalLayout.addWidget(self.d_y3_v)

        self.main_verticalLayout.addLayout(self.d_y3_horizontalLayout)

        self.setLayout(self.main_verticalLayout)

#####################################################################################

        self.o_x1_Slider.valueChanged.connect(self.valueChanged)
        self.o_y1_Slider.valueChanged.connect(self.valueChanged)
        self.o_x2_Slider.valueChanged.connect(self.valueChanged)
        self.o_y2_Slider.valueChanged.connect(self.valueChanged)
        self.o_x3_Slider.valueChanged.connect(self.valueChanged)
        self.o_y3_Slider.valueChanged.connect(self.valueChanged)
        self.d_x1_Slider.valueChanged.connect(self.valueChanged)
        self.d_y1_Slider.valueChanged.connect(self.valueChanged)
        self.d_x2_Slider.valueChanged.connect(self.valueChanged)
        self.d_y2_Slider.valueChanged.connect(self.valueChanged)
        self.d_x3_Slider.valueChanged.connect(self.valueChanged)
        self.d_y3_Slider.valueChanged.connect(self.valueChanged)
        self.keyPressEvent = self.key_Press_Event
        self.closeEvent = self.close_Event

    def valueChanged(self):
        self.o_x1_v.setText(f"{self.o_x1_Slider.value()}")
        self.o_y1_v.setText(f"{self.o_y1_Slider.value()}")
        self.o_x2_v.setText(f"{self.o_x2_Slider.value()}")
        self.o_y2_v.setText(f"{self.o_y2_Slider.value()}")
        self.o_x3_v.setText(f"{self.o_x3_Slider.value()}")
        self.o_y3_v.setText(f"{self.o_y3_Slider.value()}")
        self.d_x1_v.setText(f"{self.d_x1_Slider.value()}")
        self.d_y1_v.setText(f"{self.d_y1_Slider.value()}")
        self.d_x2_v.setText(f"{self.d_x2_Slider.value()}")
        self.d_y2_v.setText(f"{self.d_y2_Slider.value()}")
        self.d_x3_v.setText(f"{self.d_x3_Slider.value()}")
        self.d_y3_v.setText(f"{self.d_y3_Slider.value()}")
        img = self.mainWindow.cImg_o.copy()
        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Img_Affine_Transform(img), p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)

    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()
        if event.key() == Qt.Key_Delete or event.key() == Qt.Key_Backspace:
            self.o_x1_Slider.setValue(0)
            self.o_y1_Slider.setValue(0)
            self.o_x2_Slider.setValue(self.imgwidth)
            self.o_y2_Slider.setValue(0)
            self.o_x3_Slider.setValue(0)
            self.o_y3_Slider.setValue(self.imgheight)
            self.d_x1_Slider.setValue(0)
            self.d_y1_Slider.setValue(0)
            self.d_x2_Slider.setValue(self.imgwidth)
            self.d_y2_Slider.setValue(0)
            self.d_x3_Slider.setValue(0)
            self.d_y3_Slider.setValue(self.imgheight)

    def close_Event(self, event):
        if self.seaved:
            self.mainWindow.cImg_o = self.Img_Affine_Transform(self.mainWindow.cImg_o)
            self.mainWindow.qImg, self.mainWindow.cImg_r, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
            self.mainWindow.show_img()
        else:
            self.mainWindow.show_img()

    def Img_Affine_Transform(self, img):
        y, x, _ = img.shape
        src = np.float32([[self.o_x1_Slider.value(), self.o_y1_Slider.value()], [self.o_x2_Slider.value(), self.o_y2_Slider.value()], [self.o_x3_Slider.value(), self.o_y3_Slider.value()]])
        dst = np.float32([[self.d_x1_Slider.value(), self.d_y1_Slider.value()], [self.d_x2_Slider.value(), self.d_y2_Slider.value()], [self.d_x3_Slider.value(), self.d_y3_Slider.value()]])
        M = cv2.getAffineTransform(src, dst)
        img = cv2.warpAffine(img,M,(x,y))
        return img

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Ui_Affine_Transform_Window(100, 2000)
#     window.show()
#     sys.exit(app.exec_())