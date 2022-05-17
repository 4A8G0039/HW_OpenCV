import cv2 as cv
import numpy as np


src = cv.imread("./Img/wallpaper.png")

#Detect the keypoints using SIFT Detector
minHessian = 500
detector = cv.SIFT_create(minHessian)
keypoints = detector.detect(src)
#-- Draw keypoints
img_keypoints = np.empty((src.shape[0], src.shape[1], 3), dtype=np.uint8)
cv.drawKeypoints(src, keypoints, img_keypoints)
#-- Show detected (drawn) keypoints
cv.imshow('SURF Keypoints', img_keypoints)
cv.waitKey()