import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('low_contrast.jpg',cv.IMREAD_GRAYSCALE)
plt.hist(img.ravel(),256,[0,256]);plt.show()


def hist(img):
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()


img = cv.imread('low_contrast.jpg',0)
hist(img)

img = cv.imread('low_contrast.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv.imshow("Equalization",res)
hist(equ)
cv.waitKey(0)
cv.destroyAllWindows()


img = cv.imread('low_contrast.jpg',0)
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
res = np.hstack((img,cl1))
cv.imshow("CLAHE",res)
hist(cl1)
cv.waitKey(0)
cv.destroyAllWindows()