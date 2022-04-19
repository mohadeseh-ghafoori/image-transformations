import cv2 as cv
img=cv.imread("G:\learn opencv/T.tif")
cv.imshow("original image", img)
#convert RGB to gray scale 
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray scale image", gray_img)
#blur image
blurred_img=cv.GaussianBlur(gray_img, (3,3),cv.BORDER_DEFAULT)
cv.imshow("blurred image",blurred_img)
cv.waitKey(0)