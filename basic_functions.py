import numpy as np
import cv2 as cv
img=cv.imread("G:\learn opencv/T.tif")
cv.imshow("original image", img)
#convert RGB to gray scale 
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray scale image", gray_img)
#blur image
blurred_img=cv.GaussianBlur(gray_img, (3,3),cv.BORDER_DEFAULT)  #or use your own sigma not default 
cv.imshow("blurred image",blurred_img)
#edge detection
canny=cv.Canny(gray_img,50,100)
cv.imshow("canny edge", canny)
#dilate : thicken edges 
dilated_img=cv.dilate(canny,(7,7),iterations=10)
cv.imshow("dilated image", dilated_img)
#erode : erode thick edges(thin them)
eroded_img=cv.erode(dilated_img,(7,7),iterations=5)
cv.imshow("eroded image",eroded_img)
#scaling 
resized_img=cv.resize(img,None,fx=0.2,fy=0.3) # or cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("resized image",resized_img)
#crop
cropped_img=img[100:150,20:100]
cv.imshow("cropped image",cropped_img)
#translation 
def translate(img,tx,ty): 
    width,height = img.shape[:2]
    trans_mx=np.float32([[1,0,tx],[0,1,ty],[0,0,1]])
    return cv.warpPerspective(img,trans_mx, (width,height))
translated_img=translate(img,20,50)
cv.imshow("translated image",translated_img)
cv.waitKey(0)