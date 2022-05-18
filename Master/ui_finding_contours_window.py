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
        self.setFixedSize(700, 70)
        self.mainWindow = mainWindow
        self.seaved = False
        self.main_verticalLayout = QVBoxLayout()

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

#####################################################################################
        self.contour_type_horizontalLayout = QHBoxLayout()


        # self.c_contour = QCheckBox()
        # self.c_contour.setText("Contour")
        # self.c_contour.setChecked(False)
        # self.contour_type_horizontalLayout.addWidget(self.c_contour)

        self.c_convex_hull = QCheckBox()
        self.c_convex_hull.setText("Convex Hull")
        self.c_convex_hull.setChecked(False)
        self.contour_type_horizontalLayout.addWidget(self.c_convex_hull)

        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.contour_type_horizontalLayout.addWidget(self.line)

        self.c_box = QCheckBox()
        self.c_box.setText("Box")
        self.c_box.setChecked(False)
        self.contour_type_horizontalLayout.addWidget(self.c_box)

        self.c_circle = QCheckBox()
        self.c_circle.setText("Circle")
        self.c_circle.setChecked(False)
        self.contour_type_horizontalLayout.addWidget(self.c_circle)

        self.line2 = QFrame()
        self.line2.setFrameShape(QFrame.VLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.contour_type_horizontalLayout.addWidget(self.line2)

        self.c_rotated_box = QCheckBox()
        self.c_rotated_box.setText("Rotated Box")
        self.c_rotated_box.setChecked(False)
        self.contour_type_horizontalLayout.addWidget(self.c_rotated_box)

        self.c_ellipse = QCheckBox()
        self.c_ellipse.setText("Ellipse")
        self.c_ellipse.setChecked(False)
        self.contour_type_horizontalLayout.addWidget(self.c_ellipse)
        
        self.main_verticalLayout.addLayout(self.contour_type_horizontalLayout)

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

        # self.c_contour.clicked.connect(self.c_contour_valueChanged)
        self.c_convex_hull.clicked.connect(self.c_convex_hull_valueChanged)
        self.c_box.clicked.connect(self.c_box__circle_valueChanged)
        self.c_circle.clicked.connect(self.c_box__circle_valueChanged)
        self.c_rotated_box.clicked.connect(self.c_rotated_box__ellipse_valueChanged)
        self.c_ellipse.clicked.connect(self.c_rotated_box__ellipse_valueChanged)
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

    # def c_contour_valueChanged(self):
    #     self.checkbox_setting([0])

    def c_convex_hull_valueChanged(self):
        self.checkbox_setting([0])
        self.valueChanged()

    def c_box__circle_valueChanged(self):
        self.checkbox_setting([1, 2])
        self.valueChanged()

    def c_rotated_box__ellipse_valueChanged(self):
        self.checkbox_setting([3, 4])
        self.valueChanged()

    def checkbox_setting(self, c_check_list):
        c_list = [ self.c_convex_hull, self.c_box, self.c_circle, self.c_rotated_box, self.c_ellipse]
        for i, checkbox in enumerate(c_list):
            if i not in c_check_list:
                checkbox.setChecked(False)

    def Finding_Contours(self):
        threshold = self.threshold_v
        src = self.mainWindow.cImg_o.copy()
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        src_gray = cv2.blur(src_gray, (3,3))
        # Detect edges using Canny
        canny_output = cv2.Canny(src_gray, threshold, threshold * 2)
        # Find contours
        contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if self.c_convex_hull.isChecked():
            hull_list = []
            for i in range(len(contours)):
                hull = cv2.convexHull(contours[i])
                hull_list.append(hull)

        if self.c_box.isChecked() or self.c_circle.isChecked():
            contours_poly = [None]*len(contours)
            boundRect = [None]*len(contours)
            centers = [None]*len(contours)
            radius = [None]*len(contours)
            for i, c in enumerate(contours):
                contours_poly[i] = cv2.approxPolyDP(c, 3, True)
                boundRect[i] = cv2.boundingRect(contours_poly[i])
                centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

        if self.c_rotated_box.isChecked() or self.c_ellipse.isChecked():
            minRect = [None]*len(contours)
            minEllipse = [None]*len(contours)
            for i, c in enumerate(contours):
                minRect[i] = cv2.minAreaRect(c)
                if c.shape[0] > 5:
                    minEllipse[i] = cv2.fitEllipse(c)


        # Draw contours
        drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        for i, c in enumerate(contours):
            color = (random.randint(0,256), random.randint(0,256), random.randint(0,256))
            if not self.c_convex_hull.isChecked() and not self.c_box.isChecked() and not self.c_circle.isChecked() and not self.c_rotated_box.isChecked() and not self.c_ellipse.isChecked(): 
                cv2.drawContours(drawing, contours, i, color, 2, cv2.LINE_8, hierarchy, 0)
            if self.c_convex_hull.isChecked() or self.c_rotated_box.isChecked() or self.c_ellipse.isChecked(): 
                cv2.drawContours(drawing, contours, i, color)
            if self.c_box.isChecked() or self.c_circle.isChecked(): cv2.drawContours(drawing, contours_poly, i, color)

            if self.c_convex_hull.isChecked(): cv2.drawContours(drawing, hull_list, i, color)

            if self.c_box.isChecked(): cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
                (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
            if self.c_circle.isChecked(): cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)

            if self.c_rotated_box.isChecked():
                box = cv2.boxPoints(minRect[i])
                box = np.intp(box) 
                cv2.drawContours(drawing, [box], 0, color)
            if self.c_ellipse.isChecked():
                if c.shape[0] > 5:
                    cv2.ellipse(drawing, minEllipse[i], color, 2)

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
