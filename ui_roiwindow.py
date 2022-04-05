import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np


class Ui_ROIWindow(QWidget):
    def __init__(self, cRoi_o, cRoi_r, qRoi):
        super(Ui_ROIWindow, self).__init__()
        self.setWindowTitle("ROI")
        self.setFixedSize(300, 300)
        self.cRoi_o = cRoi_o
        self.cRoi_r = cRoi_r
        self.qRoi = qRoi
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.flag = False
        self.seave = False
        self.label = QLabel(self)
        self.label.setFixedSize(300, 300)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.addWidget(self.label, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.setLayout(self.verticalLayout)
        self.show_img(self.qRoi)
        self.label.mousePressEvent = self.show_mouse_press
        self.label.mouseReleaseEvent = self.show_mouse_release
        self.label.mouseMoveEvent = self.show_mouse_move
        self.keyPressEvent = self.key_Press_Event
        
        
    def show_img(self, qimg):
        width = qimg.size().width()
        height = qimg.size().height()
        self.label.setPixmap(qimg)
        self.label.setFixedSize(width, height)

        if width >= 300:
            if height >= 300:
                self.setFixedSize(width, height)
            else:
                self.setFixedSize(width, 300)
        else:
            if height >= 300:
                self.setFixedSize(300, height)
            else:
                self.setFixedSize(300, 300)

        self.move(((QApplication.desktop().width() - self.width())/2), ((QApplication.desktop().height() - self.height())/2) + 5)

    def show_mouse_press(self, event):
        print(f"[show_mouse_press] {event.x()=}, {event.y()=}, {event.button()=}")
        self.flag = True

    def show_mouse_move(self, event):
        if self.flag == True:
            self.x0 = event.x()
            self.y0 = event.y()

        print(f"[show_mouse_move] {event.x()=}, {event.y()=}, {event.button()=}")
        self.cRoiheight, self.cRoiwidth, _ = self.cRoi_r.shape
        if event.x() <= 0:
            self.x1 = 0
        elif event.x() >= self.cRoiwidth:
            self.x1 = self.cRoiwidth
        else:
            self.x1 = event.x()

        if event.y() <= 0:
            self.y1 = 0
        elif event.y() >= self.cRoiheight:
            self.y1 = self.cRoiheight
        else:
            self.y1 = event.y()

        ncImg = self.cRoi_r.copy()
        cv2.rectangle(ncImg, (self.x0, self.y0), (self.x1, self.y1), (0, 0, 255), 2)
        nqImg = self.cvimgTOqtimg(ncImg)
        self.label.setPixmap(nqImg)
        self.flag = False

    def show_mouse_release(self, event):
        print(f"[show_mouse_release] {event.x()=}, {event.y()=}, {event.button()=}")
        self.flag = False

    def key_Press_Event(self, event):
        print(f"[key_Press_Event] {event.key()=}")
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.seave == False and self.x0 != self.x1 and self.y0 != self.y1:
                (self.x0, self.x1) = (self.x0, self.x1) if self.x0 < self.x1 else (self.x1, self.x0)
                (self.y0, self.y1) = (self.y0, self.y1) if self.y0 < self.y1 else (self.y1, self.y0)
                self.label.mousePressEvent = None
                self.label.mouseReleaseEvent = None
                self.label.mouseMoveEvent = None
                self.show_img(self.cvimgTOqtimg(self.cRoi_r[self.y0 : self.y1, self.x0 : self.x1]))
                self.seave = True
                print("Height : %d, Width : %d" % (self.y1 - self.y0, self.x1 - self.x0))

            elif self.seave:
                x = self.cRoi_o.shape[0] / self.cRoi_r.shape[0]
                filename, _ = QFileDialog.getSaveFileName(self, "SaveFile", "./", "Image Files(*.png *.jpg *.jpeg *.bmp *.tif)")
                cv2.imencode('.png', self.cRoi_o[int(self.y0 * x): int(self.y1 * x), int(self.x0  * x): int(self.x1 * x)])[1].tofile(filename)
                print("Save Path :", filename)
                self.close()

        if self.seave and event.key() == Qt.Key_Delete or event.key() == Qt.Key_Backspace:
            self.x0 = 0
            self.y0 = 0
            self.x1 = 0
            self.y1 = 0
            self.flag = False
            self.seave = False
            self.show_img(self.qRoi)
            self.label.mousePressEvent = self.show_mouse_press
            self.label.mouseReleaseEvent = self.show_mouse_release
            self.label.mouseMoveEvent = self.show_mouse_move


    def cvimgTOqtimg(self, cvImg):
        height, width, depth = cvImg.shape
        cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
        qtImg = QImage(cvImg.data, width, height, width * depth, QImage.Format_RGB888)
        return QPixmap(qtImg)

    def swap(a, b):
        tmp = a
        a = b
        b = tmp