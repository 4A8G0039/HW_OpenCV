import numpy as np
import cv2 as cv

filename = "./Img/wallpaper.png"
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #轉化灰度圖

gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None) #形態學運算，膨脹

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()