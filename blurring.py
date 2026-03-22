import os
import cv2 as cv
img= cv.imread(os.path.join(".", "dogs.jpg"))

resize_images=cv.resize(img,(600,488))
k_size=77
blur_img=cv.blur(resize_images, (k_size, k_size))
cv.imshow("kopek", blur_img)
cv.imshow("img",resize_images)
cv.waitKey()