import os
import cv2 as cv
img= cv.imread(os.path.join(".", "bird.jpg"))

img_r= cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV) #renk ayrımları için

cv.imshow("r_im", img_r)
cv.imshow("gray", img_gray)
cv.imshow("image", img)
cv.imshow("hsv", img_hsv)
cv.waitKey()