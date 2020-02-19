import cv2 as cv
import numpy as np

drawing=False
ix,iy=-1,-1

def draw_rect(event,x,y,flags,param):
    global ix,iy,drawing
    if event == cv.EVENT_LBUTTONDOWN:
        if drawing == True:
            drawing = False
            cv.rectangle(resized_img,(ix,iy),(x,y),(0,255,0),0)
        else:
            drawing = True
            ix,iy=x,y

img = cv.imread("./Cat03.jpg",1)

width = int(img.shape[1])
height = int(img.shape[0])
print("width is {}".format(width))
print("height is {}".format(height))

percentage_resize = 60
width_resized = int(img.shape[1] * percentage_resize / 100)
height_resized = int(img.shape[0] * percentage_resize / 100)
dim = (width_resized,height_resized)
resized_img = cv.resize(img,dim,interpolation=cv.INTER_AREA)
cv.namedWindow("resized")
cv.setMouseCallback("resized",draw_rect)
while(1):
    cv.imshow("resized",resized_img)
    k= cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

cv.imwrite("cat.bmp",resized_img)


if __name__ == "__main__":
    pass