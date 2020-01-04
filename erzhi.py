#-*- coding: utf-8 -*-
import cv2  
  
image = cv2.imread('C:/Users/22018/Desktop/deng/ConsoleApplication2/flower.jpg')  
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  
cv2.threshold(image, 140, 255, 0, image)  
  
cv2.namedWindow("Image")  
cv2.imshow("Image", image)  
cv2.waitKey(0)  
