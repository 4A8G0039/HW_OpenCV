import cv2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


def img_resize(image, p = True):
    height, width = image.shape[0], image.shape[1]
    # 设置新的图片分辨率框架
    height_new = 960
    width_new = 1440
    # 判断图片的长宽比率
    if width / height >= width_new / height_new:
        img_new = cv2.resize(image, (width_new, int(height * width_new / width + 0.5)))
    else:
        img_new = cv2.resize(image, (int(width * height_new / height + 0.5), height_new))
    if p:print(f'Show_Height : {img_new.shape[0]}, Show_Width : {img_new.shape[1]}')
    return img_new

def SaveFile(cImg_o):
    cv2.imencode('.png', cImg_o)[1].tofile(".\Img\Feature_Description__2.png")

img = cv2.imread(".\Img\Feature_Description_2.png")
SaveFile(img_resize(img))