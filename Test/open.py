import numpy as np
import cv2
img = cv2.imdecode(np.fromfile('./Img/123.png',dtype=np.uint8),-1)
cv2.imshow('i',img)



cv2.waitKey()