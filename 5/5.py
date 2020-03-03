import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("noise.jpg")

mean = cv.blur(img,(5,5))

gaussian = cv.GaussianBlur(img,(11,11),0)

median = cv.medianBlur(img,5)

bilateral = cv.bilateralFilter(img,9,1001,1001)


res1 = np.hstack((img,mean))
res2 = np.hstack((img,gaussian))
res3 = np.hstack((img,median))
res4 = np.hstack((img,bilateral))



cv.imshow("mean",res1)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("gaussian",res2)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("median",res3)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("bilateral",res4)
cv.waitKey(0)
cv.destroyAllWindows()