import math
import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np

class Ui_Hough_Line_Transform_Window(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Hough_Line_Transform_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Hough Line Transform (霍夫轉換)")
        self.setFixedSize(700, 200)
        self.seaved = False
        self.mainWindow = mainWindow
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


#Canny Edge Detection
#####################################################################################
        
        self.canny_edge_detection_horizontalLayout = QHBoxLayout()
        self.canny_edge_detection = QLabel()
        self.canny_edge_detection.setMinimumSize(QSize(120, 0))
        self.canny_edge_detection.setText("Canny Edge Detection :")
        self.canny_edge_detection_horizontalLayout.addWidget(self.canny_edge_detection)
        self.main_verticalLayout.addLayout(self.canny_edge_detection_horizontalLayout)

#Threshold_low value
        self.canny_threshold_low_horizontalLayout = QHBoxLayout()

        self.canny_threshold_low = QLabel()
        self.canny_threshold_low.setMinimumSize(QSize(120, 0))
        self.canny_threshold_low.setText("Threshold low value")
        self.canny_threshold_low_horizontalLayout.addWidget(self.canny_threshold_low)

        self.canny_threshold_low_Slider = QSlider()
        self.canny_threshold_low_Slider.setMaximum(226)
        self.canny_threshold_low_Slider.setValue(0)
        self.canny_threshold_low_Slider.setOrientation(Qt.Horizontal)
        self.canny_threshold_low_horizontalLayout.addWidget(self.canny_threshold_low_Slider)

        self.canny_threshold_low_value = QLabel()
        sizePolicy.setHeightForWidth(self.canny_threshold_low_value.sizePolicy().hasHeightForWidth())
        self.canny_threshold_low_value.setSizePolicy(sizePolicy)
        self.canny_threshold_low_value.setMinimumSize(QSize(30, 0))
        self.canny_threshold_low_value.setText("0")
        self.canny_threshold_low_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.canny_threshold_low_horizontalLayout.addWidget(self.canny_threshold_low_value)

        self.main_verticalLayout.addLayout(self.canny_threshold_low_horizontalLayout)

#####################################################################################
#Ratio value
        self.ratio_horizontalLayout = QHBoxLayout()

        self.ratio = QLabel()
        self.ratio.setMinimumSize(QSize(120, 0))
        self.ratio.setText("Ratio value")
        self.ratio_horizontalLayout.addWidget(self.ratio)

        self.ratio_Slider = QSlider()
        self.ratio_Slider.setMaximum(40)
        self.ratio_Slider.setValue(20)
        self.ratio_Slider.setPageStep(1)
        self.ratio_Slider.setOrientation(Qt.Horizontal)
        self.ratio_horizontalLayout.addWidget(self.ratio_Slider)

        self.ratio_value = QLabel()
        sizePolicy.setHeightForWidth(self.ratio_value.sizePolicy().hasHeightForWidth())
        self.ratio_value.setSizePolicy(sizePolicy)
        self.ratio_value.setMinimumSize(QSize(30, 0))
        self.ratio_value.setText("3.0")
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
        self.ksize_Slider.setValue(2)
        self.ksize_Slider.setPageStep(1)
        self.ksize_Slider.setOrientation(Qt.Horizontal)
        self.ksize_horizontalLayout.addWidget(self.ksize_Slider)

        self.ksize_value = QLabel()
        sizePolicy.setHeightForWidth(self.ksize_value.sizePolicy().hasHeightForWidth())
        self.ksize_value.setSizePolicy(sizePolicy)
        self.ksize_value.setMinimumSize(QSize(30, 0))
        self.ksize_value.setText("3")
        self.ksize_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ksize_horizontalLayout.addWidget(self.ksize_value)

        self.main_verticalLayout.addLayout(self.ksize_horizontalLayout)

        self.setLayout(self.main_verticalLayout)

#LINE
#####################################################################################

        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.main_verticalLayout.addWidget(self.line)

#Hough Line Transform
#####################################################################################
        
        self.hough_line_transform_horizontalLayout = QHBoxLayout()
        self.hough_line_transform = QLabel()
        self.hough_line_transform.setMinimumSize(QSize(500, 0))
        self.hough_line_transform.setText("Hough Line Transform :")
        self.hough_line_transform_horizontalLayout.addWidget(self.hough_line_transform)

        self.c_HoughLines = QCheckBox()
        self.c_HoughLines.setText("HoughLines")
        self.c_HoughLines.setChecked(False)
        self.hough_line_transform_horizontalLayout.addWidget(self.c_HoughLines)

        self.c_HoughLinesP = QCheckBox()
        self.c_HoughLinesP.setText("HoughLinesP")
        self.c_HoughLinesP.setChecked(True)
        self.hough_line_transform_horizontalLayout.addWidget(self.c_HoughLinesP)
        
        self.main_verticalLayout.addLayout(self.hough_line_transform_horizontalLayout)
        
#Threshold_low value
        self.hough_threshold_low_horizontalLayout = QHBoxLayout()

        self.hough_threshold_low = QLabel()
        self.hough_threshold_low.setMinimumSize(QSize(120, 0))
        self.hough_threshold_low.setText("Threshold low value")
        self.hough_threshold_low_horizontalLayout.addWidget(self.hough_threshold_low)

        self.hough_threshold_low_Slider = QSlider()
        self.hough_threshold_low_Slider.setMaximum(255)
        self.hough_threshold_low_Slider.setValue(150)
        self.hough_threshold_low_Slider.setOrientation(Qt.Horizontal)
        self.hough_threshold_low_horizontalLayout.addWidget(self.hough_threshold_low_Slider)

        self.hough_threshold_low_value = QLabel()
        sizePolicy.setHeightForWidth(self.hough_threshold_low_value.sizePolicy().hasHeightForWidth())
        self.hough_threshold_low_value.setSizePolicy(sizePolicy)
        self.hough_threshold_low_value.setMinimumSize(QSize(30, 0))
        self.hough_threshold_low_value.setText("150")
        self.hough_threshold_low_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.hough_threshold_low_horizontalLayout.addWidget(self.hough_threshold_low_value)

        self.main_verticalLayout.addLayout(self.hough_threshold_low_horizontalLayout)

#####################################################################################

        self.canny_threshold_low_Slider.valueChanged.connect(self.valueChanged)
        self.ratio_Slider.valueChanged.connect(self.valueChanged)
        self.ksize_Slider.valueChanged.connect(self.valueChanged)
        self.hough_threshold_low_Slider.valueChanged.connect(self.valueChanged)
        self.c_HoughLines.clicked.connect(self.c_HoughLines_valueChanged)
        self.c_HoughLinesP.clicked.connect(self.c_HoughLinesP_valueChanged)
        self.keyPressEvent = self.key_Press_Event
        self.closeEvent = self.close_Event

    def c_HoughLines_valueChanged(self):
        self.c_HoughLinesP.setChecked(False)
        self.valueChanged()
    def c_HoughLinesP_valueChanged(self):
        self.c_HoughLines.setChecked(False)        
        self.valueChanged()


    def valueChanged(self):
        self.canny_threshold_l_v = self.canny_threshold_low_Slider.value()
        self.canny_threshold_l_v += 29 if self.canny_threshold_low_Slider.value() > 0 else 0
        self.ratio_v = 1 + round(self.ratio_Slider.value() * 0.1, 1)
        self.ksize_v = (self.ksize_Slider.value()) * 2 - 1
        self.hough_threshold_l_v = self.hough_threshold_low_Slider.value()

        self.canny_threshold_low_value.setText(f"{self.canny_threshold_l_v}")
        self.ratio_value.setText(f"{self.ratio_v}")
        self.ksize_value.setText(f"{self.ksize_v}")
        self.hough_threshold_low_value.setText(f"{self.hough_threshold_l_v}")
        if self.canny_threshold_l_v == 0: show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
        else: show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Hough_Line_Transform(), p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)

    def Hough_Line_Transform(self):
        img = self.mainWindow.cImg_o.copy()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.blur(img_gray, (self.ksize_v, self.ksize_v))
        detected_edges = cv2.Canny(img_blur, self.canny_threshold_l_v, int(self.canny_threshold_l_v * self.ratio_v), self.ksize_v)
        cdst = cv2.cvtColor(detected_edges, cv2.COLOR_GRAY2BGR)
        
        if self.c_HoughLines.isChecked():
            lines = cv2.HoughLines(detected_edges, 1, np.pi / 180, self.hough_threshold_l_v, None, 0, 0)
            if lines is not None:
                for i in range(0, len(lines)):
                    rho = lines[i][0][0]
                    theta = lines[i][0][1]
                    a = math.cos(theta)
                    b = math.sin(theta)
                    x0 = a * rho
                    y0 = b * rho
                    pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
                    pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
                    cv2.line(cdst, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
        else:
            linesP = cv2.HoughLinesP(detected_edges, 1, np.pi / 180, self.hough_threshold_l_v, None, 50, 10)
            if linesP is not None:
                for i in range(0, len(linesP)):
                    l = linesP[i][0]
                    cv2.line(cdst, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
            
        return cdst

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
