'''
1.Robert's operator
2.prewitt's operator
3.sobel's operator
4.kirch's operator
'''

import cv2
import numpy as np

img = cv2.imread('lenna.png',0)
gray_img = img
rows,col = img.shape
##### SOBEL ##################

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

sob_res = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
cv2.imwrite('sob_res.png',sob_res)

####### ROBERTS ################################################################

cross_v = np.array( [[ 0, 0, 0 ],
                             [ 0, 1, 0 ],
                             [ 0, 0,-1 ]] )

cross_h = np.array( [[ 0, 0, 0 ],
                             [ 0, 0, 1 ],
                             [ 0,-1, 0 ]] )
                             
                             
vertical = img
horizontal = img

for i in range(1,rows-1):
    for j in range(1,col-1):
        vertical[i,j] = img[i,j]*cross_v[1,1] + img[i-1,j-1]*cross_v[0,0] + img[i-1,j]*cross_v[0,1] + img[i-1,j+1]*cross_v[0,2] + img[i,j-1]*cross_v[1,0] + img[i,j+1]*cross_v[1,2] + img[i+1,j-1]*cross_v[2,0] + img[i+1,j]*cross_v[2,1] + img[i+1,j+1]*cross_v[2,2] 
        

for i in range(1,rows-1):
    for j in range(1,col-1):
        horizontal[i,j] = img[i,j]*cross_h[1,1] + img[i-1,j-1]*cross_h[0,0] + img[i-1,j]*cross_h[0,1] + img[i-1,j+1]*cross_h[0,2] + img[i,j-1]*cross_h[1,0] + img[i,j+1]*cross_h[1,2] + img[i+1,j-1]*cross_h[2,0] + img[i+1,j]*cross_h[2,1] + img[i+1,j+1]*cross_h[2,2] 
        
rob_res = np.sqrt( np.square(horizontal) + np.square(vertical))
cv2.imwrite('rob_res.png',vertical)

##### PREWITT ##########################################################
cross_v = np.array( [[ -1, 0, 1 ],
                             [ -1, 0, 1 ],
                             [ -1, 0, 1 ]] )

cross_h = np.array( [[ -1, -1, -1 ],
                             [ 0, 0, 0 ],
                             [ 1, 1, 1 ]] )

img_gaussian = cv2.GaussianBlur(gray_img,(3,3),0)
img_prewittx = cv2.filter2D(img_gaussian, -1, cross_h)
img_prewitty = cv2.filter2D(img_gaussian, -1, cross_v)

cv2.imwrite("pre_res_x.png", img_prewittx)
cv2.imwrite("pre_res_y.png", img_prewitty)
cv2.imwrite("pre_res.png", img_prewittx + img_prewitty)

##### KIRSCH ####################################

cross_v = np.array( [[ 5, 5, 5 ],
                             [ -3, 0, -3 ],
                             [ -3, -3, -3 ]] )
vertical = img
                             
for i in range(1,rows-1):
    for j in range(1,col-1):
        vertical[i,j] = img[i,j]*cross_v[1,1] + img[i-1,j-1]*cross_v[0,0] + img[i-1,j]*cross_v[0,1] + img[i-1,j+1]*cross_v[0,2] + img[i,j-1]*cross_v[1,0] + img[i,j+1]*cross_v[1,2] + img[i+1,j-1]*cross_v[2,0] + img[i+1,j]*cross_v[2,1] + img[i+1,j+1]*cross_v[2,2] 
        
cv2.imwrite('kirsch_res.png', vertical)
                         
