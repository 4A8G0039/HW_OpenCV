import numpy as np
import cv2 
from imutils import perspective
image = cv2.imread("./Img/123.png") 
pts = np.array([(200,0), (400,0), (0,200), (200,200)])
# # 然後調用四角點轉換函數實現轉換 
warped = perspective.four_point_transform(image, pts)
# # 顯示轉換前後的圖像對比 
cv2.imshow("Original", image) 
cv2.imshow("Warped", warped) 
cv2.waitKey(0)