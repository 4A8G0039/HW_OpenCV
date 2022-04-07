import numpy as np
import cv2
upper = np.array([255, 255, 255])
lower = np.array([0, 0, 0])
img = cv2.imdecode(np.fromfile('./Img/IMG_4899.JPG',dtype=np.uint8),-1)
cv2.imshow('i1',img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
img = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('i',img)
cv2.waitKey()