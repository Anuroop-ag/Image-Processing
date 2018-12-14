import cv2
import numpy as np 

img = cv2.imread('gauss.png',0)
#gauss_filter = [[1,2,1],[2,4,2],[1,2,1]]

temp = img
row,col = img.shape
for i in range(1,row-1):
	for j in range(1,col-1):
		temp[i,j] = (1 * img[i-1,j-1] + 2 * img[i-1,j] + 1 * img[i-1,j+1] + 2 * img[i,j-1] + 4 * img[i,j] + 2 * img[i,j+1] + 1 * img[i+1,j-1] + 2 * img[i+1,j] + 1 * img[i+1,j+1])/16
res = np.hstack((img,temp))
cv2.imwrite('gaussian_removed.png',res)

#remove gaussian noise
#gaussian filter

