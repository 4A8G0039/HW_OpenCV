import cv2 as cv
import numpy as np


img1 = cv.imread(".\Img\Feature_Description__1.png")
img2 = cv.imread(".\Img\Feature_Description__2.png")
#-- Step 1: Detect the keypoints using SURF Detector, compute the descriptors
minHessian = 200
detector = cv.SIFT_create(minHessian)
keypoints1, descriptors1 = detector.detectAndCompute(img1, None)
keypoints2, descriptors2 = detector.detectAndCompute(img2, None)

#-- Step 2: Matching descriptor vectors with a brute force matcher
matcher = cv.BFMatcher()
matches = matcher.knnMatch(descriptors1, descriptors2, k=2)

#--Step 3: Apply Ratio Test
good = []
for m,n in matches:
    if m.distance < 0.5*n.distance:
        good.append([m])

#-- Draw matches
img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
cv.drawMatchesKnn(img1, keypoints1, img2, keypoints2, good, img_matches)
#-- Show detected (drawn) keypoints
cv.imshow('SURF Keypoints', img_matches)
cv.waitKey()

