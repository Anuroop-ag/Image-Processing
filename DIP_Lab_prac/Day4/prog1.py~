'''Write a program for point processing based image enhancement using
a.Log and inverse log transformations 
b.Gamma correction(power law transformation) with negative and positive value of gamma'''

import cv2
import numpy as np

####################Log transform#####################################
img = cv2.imread('Transformation.png',-1)
#row,col,channel = img.shape
row = np.size(img[0])
col = np.size(img[1])
c=20
for i in range(0,row):
    for j in range(0,col):
        try:
            img[i,j] = c*np.log(img[i,j]+1)
        except IndexError:
            continue
            
        

cv2.imshow('log_transform',img)
cv2.waitKey(0) 
        
#################Inverse log#####################################        
img = cv2.imread('Transformation.png',-1)
#row,col,channel = img.shape
row = np.size(img[0])
col = np.size(img[1])

for i in range(0,row):
    for j in range(0,col):
        try:
            img[i,j] = np.exp(img[i,j]) * (np.log(255)/(255-1)-1)
        except IndexError:
            continue
            
        

cv2.imshow('invlog_transform',img)
cv2.waitKey(0) 

################Gamma correction###################################
img = cv2.imread('Transformation.png',-1)
#row,col,channel = img.shape
row = np.size(img[0])
col = np.size(img[1])
c=20
gamma = 8
for i in range(0,row):
    for j in range(0,col):
        try:
            img[i,j] = c*img[i,j]**gamma
        except IndexError:
            continue
            
        

cv2.imshow('gamma_correction',img)
cv2.waitKey(0) 
        
          
