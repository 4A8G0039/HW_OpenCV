import cv2
import random
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np

class Ui_Morphology_Transformations_Window(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Morphology_Transformations_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Morphology Transformations (形態轉換)")
        self.setFixedSize(700, 120)
        self.mainWindow = mainWindow
        self.seaved = False
        self.morphological_type_value = 0
        self.morphShapes_type_value = 0
        self.ksize_v = 1
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
#Morphological type
#####################################################################################

        self.morphological_label_horizontalLayout = QHBoxLayout()
        self.morphological_label = QLabel()
        self.morphological_label.setMinimumSize(QSize(120, 0))
        self.morphological_label.setText("Morphological type :")
        self.morphological_label_horizontalLayout.addWidget(self.morphological_label)
        self.main_verticalLayout.addLayout(self.morphological_label_horizontalLayout)

        self.morphological_type_horizontalLayout = QHBoxLayout()
        self.c_Erosion = QCheckBox()
        self.c_Erosion.setText("Erosion")
        self.c_Erosion.setChecked(True)
        self.morphological_type_horizontalLayout.addWidget(self.c_Erosion)

        self.c_Dilation = QCheckBox()
        self.c_Dilation.setText("Dilation")
        self.c_Dilation.setChecked(False)
        self.morphological_type_horizontalLayout.addWidget(self.c_Dilation)

        self.c_Opening = QCheckBox()
        self.c_Opening.setText("Opening")
        self.c_Opening.setChecked(False)
        self.morphological_type_horizontalLayout.addWidget(self.c_Opening)

        self.c_Closing = QCheckBox()
        self.c_Closing.setText("Closing")
        self.c_Closing.setChecked(False)
        self.morphological_type_horizontalLayout.addWidget(self.c_Closing)

        self.c_Gradient = QCheckBox()
        self.c_Gradient.setText("Gradient")
        self.c_Gradient.setChecked(False)
        self.morphological_type_horizontalLayout.addWidget(self.c_Gradient)

        self.c_Top_Hat = QCheckBox()
        self.c_Top_Hat.setText("Top Hat")
        self.c_Top_Hat.setChecked(False)
        self.morphological_type_horizontalLayout.addWidget(self.c_Top_Hat)

        self.c_Black_Hat = QCheckBox()
        self.c_Black_Hat.setText("Black Hat")
        self.c_Black_Hat.setChecked(False)
        self.morphological_type_horizontalLayout.addWidget(self.c_Black_Hat)

        self.c_Skeletonize = QCheckBox()
        self.c_Skeletonize.setText("Skeletonize")
        self.c_Skeletonize.setChecked(False)
        self.morphological_type_horizontalLayout.addWidget(self.c_Skeletonize)

        self.c_Perimeter = QCheckBox()
        self.c_Perimeter.setText("Perimeter")
        self.c_Perimeter.setChecked(False)
        self.morphological_type_horizontalLayout.addWidget(self.c_Perimeter)
        
        self.main_verticalLayout.addLayout(self.morphological_type_horizontalLayout)

#MorphShapes type
#####################################################################################

        self.morphShapes_label_horizontalLayout = QHBoxLayout()
        self.morphShapes_label = QLabel()
        self.morphShapes_label.setMinimumSize(QSize(120, 0))
        self.morphShapes_label.setText("MorphShapes type :")
        self.morphShapes_label_horizontalLayout.addWidget(self.morphShapes_label)
        self.main_verticalLayout.addLayout(self.morphShapes_label_horizontalLayout)
        
        self.morphShapes_type_horizontalLayout = QHBoxLayout()

        self.c_Rect = QCheckBox()
        self.c_Rect.setText("Rect")
        self.c_Rect.setChecked(True)
        self.morphShapes_type_horizontalLayout.addWidget(self.c_Rect)

        self.c_Cross = QCheckBox()
        self.c_Cross.setText("Cross")
        self.c_Cross.setChecked(False)
        self.morphShapes_type_horizontalLayout.addWidget(self.c_Cross)

        self.c_Ellipse = QCheckBox()
        self.c_Ellipse.setText("Ellipse")
        self.c_Ellipse.setChecked(False)
        self.morphShapes_type_horizontalLayout.addWidget(self.c_Ellipse)
        
        self.main_verticalLayout.addLayout(self.morphShapes_type_horizontalLayout)

#####################################################################################
#Ksize value
        self.ksize_horizontalLayout = QHBoxLayout()

        self.ksize = QLabel()
        self.ksize.setMinimumSize(QSize(120, 0))
        self.ksize.setText("Ksize value")
        self.ksize_horizontalLayout.addWidget(self.ksize)

        self.ksize_Slider = QSlider()
        self.ksize_Slider.setMaximum(21)
        self.ksize_Slider.setValue(1)
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


#####################################################################################

        self.c_Erosion.clicked.connect(self.c_Erosion__valueChanged)
        self.c_Dilation.clicked.connect(self.c_Dilation__valueChanged)
        self.c_Opening.clicked.connect(self.c_Opening__valueChanged)
        self.c_Closing.clicked.connect(self.c_Closing__valueChanged)
        self.c_Gradient.clicked.connect(self.c_Gradient__valueChanged)
        self.c_Top_Hat.clicked.connect(self.c_Top_Hat__valueChanged)
        self.c_Black_Hat.clicked.connect(self.c_Black_Hat__valueChanged)
        self.c_Skeletonize.clicked.connect(self.c_Skeletonize__valueChanged)
        self.c_Perimeter.clicked.connect(self.c_Perimeter__valueChanged)
        self.c_Rect.clicked.connect(self.c_Rect__valueChanged)
        self.c_Cross.clicked.connect(self.c_Cross__valueChanged)
        self.c_Ellipse.clicked.connect(self.c_Ellipse__valueChanged)
        self.ksize_Slider.valueChanged.connect(self.valueChanged)
        self.keyPressEvent = self.key_Press_Event
        self.closeEvent = self.close_Event

        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Morphology_Operations(), p = False)
        self.mainWindow.show_img(show_img)


    def valueChanged(self):
        self.ksize_v = self.ksize_Slider.value()
        self.ksize_value.setText(f"{self.ksize_v * 2 + 1}") if self.ksize_v > 0 else self.ksize_value.setText(f"{self.ksize_v}")

        if self.ksize_v > 0: show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Morphology_Operations(), p = False)
        else: show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
        self.mainWindow.show_img(show_img)

    def c_Erosion__valueChanged(self):
        self.morphological_type_value = 0
        self.checkbox_setting()
        self.valueChanged()

    def c_Dilation__valueChanged(self):
        self.morphological_type_value = 1
        self.checkbox_setting()
        self.valueChanged()

    def c_Opening__valueChanged(self):
        self.morphological_type_value = 2
        self.checkbox_setting()
        self.valueChanged()

    def c_Closing__valueChanged(self):
        self.morphological_type_value = 3
        self.checkbox_setting()
        self.valueChanged()

    def c_Gradient__valueChanged(self):
        self.morphological_type_value = 4
        self.checkbox_setting()
        self.valueChanged()

    def c_Top_Hat__valueChanged(self):
        self.morphological_type_value = 5
        self.checkbox_setting()
        self.valueChanged()

    def c_Black_Hat__valueChanged(self):
        self.morphological_type_value = 6
        self.checkbox_setting()
        self.valueChanged()

    def c_Skeletonize__valueChanged(self):
        self.morphological_type_value = 7
        self.checkbox_setting()
        self.valueChanged()

    def c_Perimeter__valueChanged(self):
        self.morphological_type_value = 8
        self.checkbox_setting()
        self.valueChanged()

    def c_Rect__valueChanged(self):
        self.morphShapes_type_value = 0
        self.checkbox_setting(True)
        self.valueChanged()

    def c_Cross__valueChanged(self):
        self.morphShapes_type_value = 1
        self.checkbox_setting(True)
        self.valueChanged()

    def c_Ellipse__valueChanged(self):
        self.morphShapes_type_value = 2
        self.checkbox_setting(True)
        self.valueChanged()

    def checkbox_setting(self, shap = False):
        morphological_c_list = [ self.c_Erosion, self.c_Dilation, self.c_Opening, self.c_Closing, self.c_Gradient,\
             self.c_Top_Hat, self.c_Black_Hat, self.c_Skeletonize, self.c_Perimeter]
        morphShapes_c_list = [ self.c_Rect, self.c_Cross, self.c_Ellipse]
        c_list = morphological_c_list if not shap else morphShapes_c_list
        c_check_num = self.morphological_type_value if not shap else self.morphShapes_type_value
        for i, checkbox in enumerate(c_list):
            checkbox.setChecked(False) if i != c_check_num else checkbox.setChecked(True)
                

    def Morphology_Operations(self):
        src = self.mainWindow.cImg_o.copy()
        morph_elem_dic = {0: cv2.MORPH_RECT, 1: cv2.MORPH_CROSS, 2: cv2.MORPH_ELLIPSE}
        if self.morphological_type_value <= 6:
            morph_op_dic = {0: cv2.MORPH_ERODE, 1: cv2.MORPH_DILATE, 2: cv2.MORPH_OPEN, 3: cv2.MORPH_CLOSE, 4: cv2.MORPH_GRADIENT, 5: cv2.MORPH_TOPHAT, 6: cv2.MORPH_BLACKHAT}
            element = cv2.getStructuringElement(morph_elem_dic[self.morphShapes_type_value], (self.ksize_v * 2 + 1, self.ksize_v * 2 + 1), (self.ksize_v, self.ksize_v))
            dst = cv2.morphologyEx(src, morph_op_dic[self.morphological_type_value], element)
        elif self.morphological_type_value == 7:
            element = cv2.getStructuringElement(morph_elem_dic[self.morphShapes_type_value], (self.ksize_v * 2 + 1, self.ksize_v * 2 + 1))
            img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            size = np.size(img)
            dst = np.zeros(img.shape, np.uint8)
            _, img = cv2.threshold(img, 127, 255, 0)
            done = False

            while(not done):
                eroded = cv2.erode(img, element)
                temp = cv2.dilate(eroded, element)
                temp = cv2.subtract(img, temp)
                dst = cv2.bitwise_or(dst, temp)
                img = eroded.copy()
                zeros = size - cv2.countNonZero(img)
                if zeros == size:
                    done = True
            dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
        elif self.morphological_type_value == 8:
            img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            kernel = np.ones((self.ksize_v * 2 + 1, self.ksize_v * 2 + 1), np.uint8)
            dilation = cv2.dilate(img, kernel, iterations = 1)
            dst = dilation - img            
            dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
        return dst


    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()

    def close_Event(self, event):
        if self.seaved and self.ksize_v > 0:
            self.mainWindow.cImg_o = self.Morphology_Operations()
            self.mainWindow.qImg, self.mainWindow.cImg_r, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
            self.mainWindow.show_img()
        else:
            self.mainWindow.show_img()
