import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('crying.jpg',0)
edges = cv.Canny(img,10,100)

res = np.hstack((img,edges))

cv.imshow("edge_Canny",res)
cv.waitKey(0)
cv.destroyAllWindows()



img = cv.imread('crying.jpg',cv.IMREAD_GRAYSCALE)
laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=11)  # x
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=11)  # y

cv.imshow("original",img)
cv.imshow("laplacian",laplacian)
cv.imshow("sobelx",sobelx)
cv.imshow("sobely",sobely)
cv.waitKey(0)
cv.destroyAllWindows()

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()