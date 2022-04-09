import numpy as np
import cv2 

def order_points(pts): 
    # 按照順時針初始化四個角點的坐標，分別是：左上，右上，右下，左下。並給它們分配內存空間 
    rect = np.zeros((4, 2), dtype = "float32") 
    # # 左上坐標之和最小 # 而右下坐標之和最大 
    s = pts.sum(axis = 1) 
    rect[0] = pts[np.argmin(s)] 
    rect[2] = pts[np.argmax(s)] 
    # 現在計算坐標點之間的差值 #
    #  右上角坐標差值最小而左下角坐標差值最大 
    diff = np.diff(pts, axis = 1) 
    rect[1] = pts[np.argmin(diff)] 
    rect[3] = pts[np.argmax(diff)] 
    # 返回四點坐標列表 
    return rect

def four_point_transform(image, pts): 
    # 調用上面的函數來獲取四個角點坐標 
    rect = order_points(pts) 
    (tl, tr, br, bl) = pts 
    # 計算轉換後新圖的寬度尺寸，寬度就是右下和左下或左上和右上點的x坐標之差的最大值 
    widthA = np.sqrt(np.sum((br - bl) ** 2))
    widthB = np.sqrt(np.sum((tr - tl) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    # 計算轉換後新圖的高度尺寸，即左上和左下或右上和右下點的y坐標之差的最大值 
    heightA = np.sqrt(np.sum((tr - br) ** 2))
    heightB = np.sqrt(np.sum((tl - bl) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    #重新定义新的图像的四边顶点的坐标
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")
    # 计算透视矩阵，并且变化应用
    M = cv2.getPerspectiveTransform(rect, dst)
    print(M)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    return warped
    

# 載入圖像的已知四角點的坐標，這個實例中我們需要手動輸入已知四角點的坐標，後面的案例我們會通過 
# # 代碼自動獲取目標圖像的四個角點坐標來實現。 
image = cv2.imread("./Img/123.png") 
pts = np.array([(200,0), (400,200), (200,401), (0,200)])
# # 然後調用四角點轉換函數實現轉換 
warped = four_point_transform(image, pts) 
# # 顯示轉換前後的圖像對比 
cv2.imshow("Original", image) 
cv2.imshow("Warped", warped) 
cv2.waitKey(0)

