import random
import numpy as np
import os
import cv2
def noisy(noise_typ,image):
    if noise_typ == "gauss":
        mean = 0
        sigma = 0.05
        img = image / 255
        # 隨機生成高斯 noise (float + float)
        noise = np.random.normal(mean, sigma, img.shape)
        # noise + 原圖
        gaussian_out = img + noise
        # 所有值必須介於 0~1 之間，超過1 = 1，小於0 = 0
        gaussian_out = np.clip(gaussian_out, 0, 1)
        
        # 原圖: float -> int (0~1 -> 0~255)
        gaussian_out = np.uint8(gaussian_out*255)
        # noise: float -> int (0~1 -> 0~255)
        noise = np.uint8(noise*255)
        return gaussian_out
    elif noise_typ == "s&p":
        row,col,ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))for i in image.shape]
        out[coords] = 1
        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "saltpepper":
        '''
        添加椒盐噪声
        image:原始图片
        prob:噪声比例
        '''
        prob = 0.01
        output = np.zeros(image.shape,np.uint8)
        noise_out = np.zeros(image.shape,np.uint8)
        thres = 1 - prob
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                rdn = random.random()#随机生成0-1之间的数字
                if rdn < prob:#如果生成的随机数小于噪声比例则将该像素点添加黑点，即椒噪声
                    output[i][j] = 0
                    noise_out[i][j] = 0
                elif rdn > thres:#如果生成的随机数大于（1-噪声比例）则将该像素点添加白点，即盐噪声
                    output[i][j] = 255
                    noise_out[i][j] = 255
                else:
                    output[i][j] = image[i][j]#其他情况像素点不变
                    noise_out[i][j] = 100
        result = [noise_out,output]#返回椒盐噪声和加噪图像
        return result


if __name__ == "__main__":
    image = cv2.imread("./Img/wallpaper.png")
    cv2.imshow("image", image)
    gauss = noisy("gauss", image)
    cv2.imencode('.jpg', gauss)[1].tofile("./Img/wallpaper_g.png")
    cv2.imshow("saltpepper", gauss)
    cv2.waitKey()