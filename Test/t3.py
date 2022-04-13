import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import cv2
from t2 import *

import numpy as np


class TextEditDemo(QWidget):
    def __init__(self, image):
        super(TextEditDemo, self).__init__()
        self.setWindowTitle("Blur (均值濾波)")
        self.setFixedSize(700, 100)
        self.form_num = 2
        self.image = image

        self.form = [Ui_Blur(self.image) ,Box_Filter(self.image)]
        # self.form1 = Ui_Blur(self.image)
        # self.form2 = Box_Filter(self.image)

        widget = QWidget()
        self.stacked_layout = QStackedLayout()
        widget.setLayout(self.stacked_layout)
        self.stacked_layout.addWidget(self.form[0])
        self.stacked_layout.addWidget(self.form[1])

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 5, 0, 0)
        layout.addWidget(widget)
        self.setLayout(layout)

        self.Top_menubar = QMenuBar(self) #新增一個QMenuBar命名為Top_menubar
        self.Top_menubar.setGeometry(QRect(0, 0, 600, 25)) #設定Top_menubar的尺寸
        
        self.Blur_action = QAction(self)
        self.Blur_action.setText("Blur (均值濾波)")
        self.Blur2_action = QAction(self)
        self.Blur2_action.setText("Blur2 (均值濾波2)")
        self.Top_menubar.addAction(self.Blur_action)
        self.Top_menubar.addAction(self.Blur2_action)
        self.Blur_action.triggered.connect(self.Blur_Clicked)
        self.Blur2_action.triggered.connect(self.Blur2_Clicked)

    def Blur_Clicked(self):
        cv2.imshow("o", self.image)
        self.setWindowTitle("Blur (均值濾波)")
        self.stacked_layout.setCurrentIndex(0)
        self.form[0].img_update()


    def Blur2_Clicked(self):
        cv2.imshow("o", self.image)
        self.setWindowTitle("Blur2 (均值濾波)")
        self.stacked_layout.setCurrentIndex(1)
        self.form[1].img_update()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    image = cv2.imread("./Img/wallpaper_gauss_h.jpg")
    win = TextEditDemo(image)
    win.show()
    sys.exit(app.exec_())