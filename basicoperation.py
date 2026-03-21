import os
import cv2 as cv
from numpy.ma.core import resize

image= cv.imread(os.path.join(".", "cat.jpg"))
print(image.shape)
#h,w,ch ççıktısı verdi

resize_images=cv.resize(image,(40,48))
print(resize_images.shape)
#boyutları güncellendi, boyutları çıktı olarak verdi

cv.imshow("cat", image)
cv.imshow("resize", resize_images)
cv.waitKey(0)
#ekranda bastırıldı