'''
WAP to read five image from folder A,5 image form folder B,then convert them
into binary image and save all of them in folder C

'''

import cv2
import numpy as np


def con_to_bin(img,num):
    row,col=img.shape
    for i in range(0,row):
        for j in range(0,col):
            if(img[i,j]>=128):
                img[i,j]=255
            else:
                img[i,j]=0
    cv2.imwrite('C/'+str(num)+'.jpg',img)



img_a_1 = cv2.imread('A/a_2.jpg',0)
img_a_2 = cv2.imread('A/a_2.jpg',0)
img_a_3 = cv2.imread('A/a_3.jpg',0)
img_a_4 = cv2.imread('A/a_4.jpg',0)
img_a_5 = cv2.imread('A/a_5.jpg',0)

img_b_1 = cv2.imread('B/b_1.jpg',0)
img_b_2 = cv2.imread('B/b_2.jpg',0)
img_b_3 = cv2.imread('B/b_3.jpg',0)
img_b_4 = cv2.imread('B/b_4.jpg',0)
img_b_5 = cv2.imread('B/b_5.jpg',0)

num = 1

con_to_bin(img_a_1,num)
num = num+1
con_to_bin(img_a_2,num)
num = num+1
con_to_bin(img_a_3,num)
num = num+1
con_to_bin(img_a_4,num)
num = num+1
con_to_bin(img_a_5,num)
num = num+1
con_to_bin(img_b_1,num)
num = num+1
con_to_bin(img_b_2,num)
num = num+1
con_to_bin(img_b_3,num)
num = num+1
con_to_bin(img_b_4,num)
num = num+1
con_to_bin(img_b_5,num)
num = num+1

#cv2.imshow('img',img_a_1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

