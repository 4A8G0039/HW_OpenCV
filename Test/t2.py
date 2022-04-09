import numpy as np
import cv2 
from imutils import perspective
img = cv2.imread("./Img/123.png")
y, x, _ = img.shape
print(x, y)
xadd = -50
yadd = -100
img = cv2.copyMakeBorder(img, x, x, x, x, cv2.BORDER_CONSTANT, value=(0, 0, 0))
ny, nx, _ = img.shape
cv2.imshow("Original", img[x:x+y, x:x*2])

M = np.float32([[1,0,xadd],[0,1,yadd]])
dst = cv2.warpAffine(img,M,(nx,ny))

cv2.imshow("dst1", dst[x:x+y, x:x*2])

M = cv2.getRotationMatrix2D((nx/2+xadd, ny/2+yadd), 20, 1)
dst = cv2.warpAffine(dst, M, (nx, ny))

cv2.imshow("dst2", dst[x:x+y, x:x*2])
cv2.waitKey(0)