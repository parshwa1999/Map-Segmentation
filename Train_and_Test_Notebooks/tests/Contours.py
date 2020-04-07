#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:48:38 2020

@author: parshwa
"""
import cv2
import numpy as np

img = cv2.imread("Img0_mask.png", 0)
ori = cv2.imread("Img0.png", 0)
img[img>127] = 255
img[img<127] = 0

#img = cv2.Canny(img, 30, 200)

contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#contours = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
#cnts = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

print("Number of Contours found = " + str(len(contours))) 

ori = cv2.drawContours(ori, contours, -1, (0,255,0), 3)

print(type(np.array(contours)))
#cv2.drawContours(ori, np.asarray(contours), -1, (0, 255, 0), 3) 
  
cv2.imshow('Contours', ori) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
