import numpy as np
import cv2 

image = cv2.imread("./Img/123.png")
y,x = image.shape[:2]
src = np.float32([[50,50],[200,50],[50,200]])
dst = np.float32([[10,100],[200,20],[100,250]])
M = cv2.getAffineTransform(src,dst)
warped = cv2.warpAffine(image,M,(x,y))
cv2.imshow("Original", image) 
cv2.imshow("Warped", warped)
cv2.waitKey(0)

