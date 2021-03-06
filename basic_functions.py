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
#edge detection canny
canny=cv.Canny(gray_img,50,100)
cv.imshow("canny edge", canny)
#edge detection laplacian
lap=cv.Laplacian(gray_img,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("laplacian edge detection",lap)
#edge detection sobel
sobelx=cv.Sobel(gray_img,cv.CV_64F,1,0)
sobely=cv.Sobel(gray_img,cv.CV_64F,0,1)
cv.imshow("sobel y",sobely)
cv.imshow("sobel x",sobelx)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow("sobel",combined_sobel)
#dilate : thicken edges 
dilated_img=cv.dilate(canny,(7,7),iterations=10)
cv.imshow("dilated image", dilated_img)
#erode : erode thick edges(thin them)
eroded_img=cv.erode(dilated_img,(7,7),iterations=5)
cv.imshow("eroded image",eroded_img)
#scaling 
resized_img=cv.resize(img,None,fx=0.5,fy=0.5) # or cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("resized image",resized_img)
#crop
cropped_img=img[100:150,20:100]
cv.imshow("cropped image",cropped_img)
#translation 
def translate(img,tx,ty): 
    width,height = img.shape[:2]
    trans_mx=np.float32([[1,0,tx],[0,1,ty],[0,0,1]])
    return cv.warpPerspective(img,trans_mx, (width,height))
translated_img=translate(img,20,100) # +x --> right   -x --> left    +y --> down   -y --> up
cv.imshow("translated image",translated_img)
#rotation 
def rotation(img,angle,rotpoint=None):
    width,height = img.shape[:2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)
    rot_mx=cv.getRotationMatrix2D(rotpoint,angle,1)
    return cv.warpAffine(img,rot_mx, (width,height))
    #return cv.rotate(img,cv.ROTATE_90_CLOCKWISE)  #this method rotates image by a specific angle not an arbitrary one, use rotate codes
    #or for working with 3*3 matrix follow the structure below
    #angle = np.radians(angle)
    #rot_mx=M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
    #        	[np.sin(angle), np.cos(angle), 0],
    #        	[0, 0, 1]])
    #return cv.warpPerspective(img,rot_mx, (width,height))
rotated_img=rotation(img,45) #positive angles are counter clockwise
#note: if you rotated_rotated_im=rotation(rotated_img,45), it won't get you 90 degree rotation, some balck prts will be introduced to image
#when it's rotated, so that black part will be rotated as a part of this process, and does not lead to 90 degree rotation
cv.imshow("rotated image",rotated_img)
#flip
flipped_img=cv.flip(img,0)  #0 --> flip around x-axis   1--> flip around y-axis   -1--> flip around both axes 
cv.imshow("flipped img",flipped_img)
# Shear
width,height = img.shape[:2]
x_axis = np.float32([[1, 0.7, 0],
                      [0, 1 ,  0],
                      [0, 0 ,  1]])
y_axis = np.float32([[1  , 0, 0],
                      [0.2, 1, 0],
                      [0  , 0, 1]])
sheared_x_img = cv.warpPerspective(img, x_axis, (int(height*1.5),int(width*1.5)))
sheared_y_img = cv.warpPerspective(img, y_axis, (int(height*1.5),int(width*1.5)))

cv.namedWindow('sheared x-axis', cv.WINDOW_NORMAL)
cv.imshow('sheared x-axis', sheared_x_img)
cv.namedWindow('sheared y-axis', cv.WINDOW_NORMAL)
cv.imshow('sheared y-axis', sheared_y_img)
cv.waitKey(0)