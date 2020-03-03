import cv2 as cv
import numpy as np
import random

img = np.ones((100,200,3),np.uint8)*100
cv.line(img,(0,0),(200,100),(255,255,255),5)
cv.line(img,(200,0),(0,100),(255,255,255),5)
cv.imshow("grayscale",img)
cv.waitKey(0)
cv.destroyAllWindows()


img = np.ones((50,200,3),np.uint8)
img[...] =[0,100,0]
cv.line(img,(0,0),(200,50),(255,0,0),5)
cv.line(img,(200,0),(0,50),(0,0,255),5)
cv.imshow("grayscale",img)
cv.waitKey(0)
cv.destroyAllWindows()

img = cv.imread("./crying.jpg",1)
cv.imshow("normal",img)
img_grey = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow("gray",img_grey)
cv.waitKey(0)
cv.destroyAllWindows()


img = cv.imread("./crying.jpg")
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        rdn=random.randint(1,100)
        if rdn <= 5 :
            img[i][j]=[0,0,0]
        elif rdn >=95:
            img[i][j]=[255,255,255]
cv.imshow("noise",img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("noise.jpg",img)

img = cv.imread("./colours.png")
b,r,g = cv.split(img)
blue = np.zeros((int(img.shape[0]),int(img.shape[1]),3),np.uint8)
blue[:,:,0]=b
red = np.zeros((int(img.shape[0]),int(img.shape[1]),3),np.uint8)
red[:,:,1]=r
green = np.zeros((int(img.shape[0]),int(img.shape[1]),3),np.uint8)
green[:,:,2]=g
cv.imshow("original",img)
cv.imshow("blue",blue)
cv.imshow("red",red)
cv.imshow("green",green)
cv.waitKey(0)
cv.destroyAllWindows()

img = cv.imread("./crying.jpg")
img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
h,s,v = cv.split(img_hsv)
hsv_img = cv.merge([h,s,v])
img_bgr = cv.cvtColor(hsv_img,cv.COLOR_HSV2BGR)
cv.imshow("merged_hsv",hsv_img)
cv.imshow("merged_bgr",img_bgr)
cv.imshow("hue",h)
cv.imshow("sat",s)
cv.imshow("vue",v)
cv.waitKey(0)
cv.destroyAllWindows()


if __name__ == "__main__":
    pass