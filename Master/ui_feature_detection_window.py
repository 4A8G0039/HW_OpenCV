import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np

class Ui_Feature_Detection_Window(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Feature_Detection_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Feature Detection (特徵檢測)")
        self.setFixedSize(700, 50)
        self.seaved = False
        self.mainWindow = mainWindow
        self.feature_v = 200
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#####################################################################################
#Feature value
        self.feature_horizontalLayout = QHBoxLayout()

        self.feature = QLabel()
        self.feature.setMinimumSize(QSize(100, 0))
        self.feature.setText("Feature value")
        self.feature_horizontalLayout.addWidget(self.feature)

        self.feature_Slider = QSlider()
        self.feature_Slider.setRange(1, 20)
        self.feature_Slider.setValue(4)
        self.feature_Slider.setPageStep(1)
        self.feature_Slider.setOrientation(Qt.Horizontal)
        self.feature_horizontalLayout.addWidget(self.feature_Slider)

        self.feature_value = QLabel()
        sizePolicy.setHeightForWidth(self.feature_value.sizePolicy().hasHeightForWidth())
        self.feature_value.setSizePolicy(sizePolicy)
        self.feature_value.setMinimumSize(QSize(30, 0))
        self.feature_value.setText("200")
        self.feature_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.feature_horizontalLayout.addWidget(self.feature_value)


        self.main_verticalLayout.addLayout(self.feature_horizontalLayout)

        self.setLayout(self.main_verticalLayout)


#####################################################################################

        self.feature_Slider.valueChanged.connect(self.valueChanged)
        self.keyPressEvent = self.key_Press_Event
        self.closeEvent = self.close_Event

        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Feature_Detector(), p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)

    def valueChanged(self):
        self.feature_v = self.feature_Slider.value() * 50
        self.feature_value.setText(f"{self.feature_v}")
        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Feature_Detector(), p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)

    def Feature_Detector(self):
        #Detect the keypoints using SIFT Detector
        nfeatures = self.feature_v
        src = self.mainWindow.cImg_o.copy()
        detector = cv2.SIFT_create(nfeatures)
        keypoints = detector.detect(src)
        #-- Draw keypoints
        img_keypoints = np.empty((src.shape[0], src.shape[1], 3), dtype=np.uint8)
        cv2.drawKeypoints(src, keypoints, img_keypoints)
        return img_keypoints

    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()

    def close_Event(self, event):
        if self.seaved:
            self.mainWindow.cImg_o = self.Feature_Detector()
            self.mainWindow.qImg, self.mainWindow.cImg_r, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
            self.mainWindow.show_img()
        else:
            self.mainWindow.show_img()
