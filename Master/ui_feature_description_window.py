import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np

class Ui_Feature_Description_Window(QWidget):
    def __init__(self, mainWindow):
        super(Ui_Feature_Description_Window, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Feature Description (特徵匹配)")
        self.setFixedSize(700, 50)
        self.mainWindow = mainWindow
        self.seaved = False
        self.feature_v = 200
        self.img_matc = self.OpenImg()
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

        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Feature_Detection_macher(), p = False)
        self.mainWindow.show_img(show_img)

    def valueChanged(self):
        self.feature_v = self.feature_Slider.value() * 50
        self.feature_value.setText(f"{self.feature_v}")
        show_img, _, _ = self.mainWindow.cvimgTOqtimg(self.Feature_Detection_macher(), p = False)
        self.mainWindow._window.Img_Lable.setPixmap(show_img)

    def Feature_Detection_macher(self):
        #Detect the keypoints using SIFT Detector
        nfeatures = self.feature_v
        img1 = self.mainWindow.cImg_o.copy()
        img2 = self.img_matc
        detector = cv2.SIFT_create(nfeatures)
        keypoints1, descriptors1 = detector.detectAndCompute(img1, None)
        keypoints2, descriptors2 = detector.detectAndCompute(img2, None)

        #-- Step 2: Matching descriptor vectors with a brute force matcher
        matcher = cv2.BFMatcher()
        matches = matcher.knnMatch(descriptors1, descriptors2, k=2)

        #--Step 3: Apply Ratio Test
        good = []
        for m,n in matches:
            if m.distance < 0.5*n.distance:
                good.append([m])

        #-- Draw matches
        img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
        cv2.drawMatchesKnn(img1, keypoints1, img2, keypoints2, good, img_matches)
        return img_matches

    def OpenImg(self):
        filename, _ = QFileDialog.getOpenFileName(self, "OpenFile", "./Img", "Image Files(*.png *.jpg *.jpeg *.bmp *.tif)")
        if filename != "":
            Img = cv2.imdecode(np.fromfile(filename,dtype=np.uint8),1)
            return Img

    def key_Press_Event(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.seaved = True
            self.close()

    def close_Event(self, event):
        if self.seaved:
            self.mainWindow.cImg_o = self.Feature_Detection_macher()
            self.mainWindow.qImg, self.mainWindow.cImg_r, _ = self.mainWindow.cvimgTOqtimg(self.mainWindow.cImg_o, p = False)
            self.mainWindow.show_img()
        else:
            self.mainWindow.show_img()
