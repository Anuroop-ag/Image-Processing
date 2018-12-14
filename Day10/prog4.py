'''
first and second order derivative of
single dimension image:
60 60 100 100 100
'''

import cv2
import numpy as np

img = np.array([0,0,60,60,100,100,100,0,0])
r = img.size

###### FIRST DERIVATIVE ################
fd = []
for i in range(0,r-1):
    fd.append(img[i+1]-img[i])
print('FIRST DERIVATIVE')    
print(fd)

###### SECOND DERIVATIVE ################
sd =[]
r = len(fd)
for i in range(0,r-1):
    sd.append(fd[i+1]-fd[i])
print('SECOND DERIVATIVE')
print(sd) 
