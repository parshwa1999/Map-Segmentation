#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:48:38 2020

@author: parshwa
"""
import cv2
import numpy as np

img = cv2.imread("1.png", 0)
img[img>127] = 255
img[img<127] = 0

img = cv2.Canny(img, 30, 200)

image, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print("Number of Contours found = " + str(len(contours))) 


f = open("Road1.csv","w+")
f.write("id,geom\n")
for i in range(len(contours)):
  contours[i] = np.squeeze(contours[i], axis = 1)
  f.write(str(i) + ",\"POLYGON ((")
  for j in contours[i]:
    f.write(str(j[0]) + " " + str(j[1]*-1) + ", ")
    f.write(str(contours[i][0][0]) + " " + str(contours[i][0][1]*-1) + "))\"\n")

f.close()


#print(contours[6])
