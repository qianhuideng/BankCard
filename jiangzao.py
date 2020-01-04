#-*- coding: utf-8 -*-
import cv2  
import numpy as np

img = cv2.imread('C:/Users/22018/Desktop/deng/ConsoleApplication2/flower.jpg')  
# 噪声点数量
coutn = 100000
for k in range(0,coutn):
    # 获取图像噪声点的随机位置
    xi = int(np.random.uniform(0,img.shape[1]))
    xj = int(np.random.uniform(0,img.shape[0]))
    #加噪
    if img.ndim == 2:
        # 灰度图像
        img[xj,xi] = 255
    elif img.ndim == 3:
        # 非灰度图像，图像加噪
        img[xj,xi,0] = 25
        img[xj,xi,1] = 20
        img[xj,xi,2] = 20
cv2.namedWindow('img')
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
