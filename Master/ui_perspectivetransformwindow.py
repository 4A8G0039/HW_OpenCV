import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from scipy.spatial import distance as dist
import numpy as np


class Ui_PerspectivetransformWindow(QWidget):
    def __init__(self, cRoi_o, cRoi_r, qRoi):
        super(Ui_PerspectivetransformWindow, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Perspective Transform")
        self.setFixedSize(300, 300)
        self.cRoi_o = cRoi_o
        self.cRoi_r = cRoi_r
        self.qRoi = qRoi
        self.pts = []
        self.seave = False
        self.seaved = False
        self.label = QLabel(self)
        self.label.setFixedSize(300, 300)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.addWidget(self.label, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.setLayout(self.verticalLayout)
        self.show_img(self.qRoi)
        self.label.mousePressEvent = self.mouse_Press_Event
        self.keyPressEvent = self.key_Press_Event
        
    
    def cvimgTOqtimg(self, cvImg):
        height, width, depth = cvImg.shape
        cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
        qtImg = QImage(cvImg.data, width, height, width * depth, QImage.Format_RGB888)
        return QPixmap(qtImg)

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

        # self.move(((QApplication.desktop().width() - self.width())/2), ((QApplication.desktop().height() - self.height())/2) + 5)

    def order_points(self, pts): 
        # sort the points based on their x-coordinates
        xSorted = pts[np.argsort(pts[:, 0]), :]

        # grab the left-most and right-most points from the sorted
        # x-roodinate points
        leftMost = xSorted[:2, :]
        rightMost = xSorted[2:, :]

        # now, sort the left-most coordinates according to their
        # y-coordinates so we can grab the top-left and bottom-left
        # points, respectively
        leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
        (tl, bl) = leftMost

        # now that we have the top-left coordinate, use it as an
        # anchor to calculate the Euclidean distance between the
        # top-left and right-most points; by the Pythagorean
        # theorem, the point with the largest distance will be
        # our bottom-right point
        D = dist.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
        (br, tr) = rightMost[np.argsort(D)[::-1], :]

        # return the coordinates in top-left, top-right,
        # bottom-right, and bottom-left order
        return np.array([tl, tr, br, bl], dtype="float32")

    def four_point_transform(self, image, pts): 
        # obtain a consistent order of the points and unpack them
        # individually
        rect = self.order_points(pts)
        (tl, tr, br, bl) = rect

        # compute the width of the new image, which will be the
        # maximum distance between bottom-right and bottom-left
        # x-coordiates or the top-right and top-left x-coordinates
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))

        # compute the height of the new image, which will be the
        # maximum distance between the top-right and bottom-right
        # y-coordinates or the top-left and bottom-left y-coordinates
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))

        # now that we have the dimensions of the new image, construct
        # the set of destination points to obtain a "birds eye view",
        # (i.e. top-down view) of the image, again specifying points
        # in the top-left, top-right, bottom-right, and bottom-left
        # order
        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype="float32")

        # compute the perspective transform matrix and then apply it
        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

        # return the warped image
        return warped

    def mouse_Press_Event(self, event):
        print(f"[show_mouse_press] {event.x()=}, {event.y()=}, {event.button()=}")
        self.pts.append([event.x(),event.y()])
        if len(self.pts) > 4 : self.pts.pop(0)
        ncImg = self.cRoi_r.copy()
        for x,y in self.pts:
            cv2.circle(ncImg, (x, y), 5, (0, 0, 255), thickness=-1)
        nqImg = self.cvimgTOqtimg(ncImg)
        self.label.setPixmap(nqImg)

    def key_Press_Event(self, event):
        print(f"[key_Press_Event] {event.key()=}")
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.seave == False and len(self.pts) == 4:
                self.label.mousePressEvent = None
                self.show_img(self.cvimgTOqtimg(self.four_point_transform(self.cRoi_r, np.array(self.pts))))
                self.seave = True

            elif self.seave:
                self.cRoi_o = self.four_point_transform(self.cRoi_r, np.array(self.pts))
                self.seaved = True
                self.close()

        if self.seave and event.key() == Qt.Key_Delete or event.key() == Qt.Key_Backspace:
            self.pts = []
            self.seave = False
            self.show_img(self.qRoi)
            self.label.mousePressEvent = self.mouse_Press_Event