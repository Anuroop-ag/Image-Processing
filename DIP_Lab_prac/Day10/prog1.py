import cv2
import numpy as np 

img = cv2.imread('lenna.png',0)
row,col = img.shape
temp = img
temp2 = img
temp3 = img

######## SOBEL ###############################################

sobelx = [[-1,-2,-1],[0,0,0],[1,2,1]]
sobely = [[-1,0,1],[-2,0,2],[-1,0,1]]
sobelx = np.array(sobelx)
sobely = np.array(sobely)
temp = cv2.filter2D(img, -1, sobelx)
temp2 = cv2.filter2D(img, -1, sobely)
temp3 = cv2.addWeighted(temp,0.5,temp2,0.5,0)
cv2.imwrite('sobelx.png',temp)
cv2.imwrite('sobely.png',temp2)
cv2.imwrite('sobel.png',temp3)


####### ROBERTS ################################################
robx = [[-1,0],[0,1]]
roby = [[0,-1],[1,0]]
robx = np.array(robx)
roby = np.array(roby)
temp = cv2.filter2D(img, -1, robx)
temp2 = cv2.filter2D(img, -1, roby)
temp3 = cv2.addWeighted(temp,0.5,temp2,0.5,0)
cv2.imwrite('robx.png',temp)
cv2.imwrite('roby.png',temp2)
cv2.imwrite('rob.png',temp3)


####### PREWITTS ############################################

prewittx = [[-1,-1,-1],[0,0,0],[1,1,1]]
prewitty = [[-1,0,1],[-1,0,1],[-1,0,1]]
prewittx = np.array(prewittx)
prewitty = np.array(prewitty)
temp = cv2.filter2D(img, -1, prewittx)
temp2 = cv2.filter2D(img, -1, prewitty)
temp3 = cv2.addWeighted(temp,0.5,temp2,0.5,0)
cv2.imwrite('prewittx.png',temp)
cv2.imwrite('prewitty.png',temp2)
cv2.imwrite('prewitt.png',temp3)


###### KIRSCH ###########################################

kirsch = [[5,5,5],[-3,0,-3],[-3,-3,-3]]
kirsch = np.array(kirsch)
temp = cv2.filter2D(img, -1, kirsch)
cv2.imwrite('kirsch.png',temp)
