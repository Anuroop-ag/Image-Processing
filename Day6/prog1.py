'''
Separate color image into 3 separate R,G,B
#Enhance R plane by +30
#Enhance G plane by -30
#Enhance B plane by +20

Combine the resultant R,G,B to set new colour image

'''
import cv2
import numpy as np

img= cv2.imread('one.jpg',-1)
#img2= cv2.imread('one.jpg',-1)
#img3= cv2.imread('one.jpg',-1)
#img4= cv2.imread('one.jpg',-1)

row,col,channel = img.shape

b,g,r = cv2.split(img)
##############BLUE#############################
#cv2.imshow('blue.jpg',b)
#cv2.waitKey(0)

for i in range(0,row):
    for j in range(0,col):
        if(b[i,j]>235):
            b[i,j]=255
        else:
            b[i,j]=b[i,j]+20

#cv2.imshow('enhanced_blue.jpg',b)
#cv2.waitKey(0)
#################RED#########################
#cv2.imshow('red.jpg',r)
#cv2.waitKey(0)

for i in range(0,row):
    for j in range(0,col):
        if(r[i,j]>225):
            r[i,j]=255
        else:
            r[i,j]=r[i,j]+30

#cv2.imshow('enhanced_red.jpg',r)
#cv2.waitKey(0)

###############GREEN########################

#cv2.imshow('green.jpg',g)
#cv2.waitKey(0)

for i in range(0,row):
    for j in range(0,col):
        if(g[i,j]<30):
            g[i,j]=0
        else:
            g[i,j]=g[i,j]-30

#cv2.imshow('enhanced_green.jpg',r)
#cv2.waitKey(0)

#############################################
temp_img = cv2.imread('one.jpg',-1)
for i in range(0,row):
    for j in range(0,col):
        temp_img[i,j,0] = b[i,j]
        temp_img[i,j,1] = g[i,j]
        temp_img[i,j,2] = r[i,j]
        

res = np.hstack((img,temp_img))
cv2.imwrite('result_bgr.jpg',res)
cv2.destroyAllWindows()
