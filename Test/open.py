import cv2 as cv
img = cv.imread('tax_calculator_pytest.jpg')
cv.imshow('window', img)
print(img.shape)
cv.waitKey()