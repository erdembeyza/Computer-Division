"""import os
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
#ekranda bastırıldı"""

"""------------"""
#crop
import matplotlib.pyplot as plt
import os
import cv2 as cv
img= cv.imread(os.path.join(".", "cat.jpg"))
print(img.shape)
crop_img= img[120:640,420:840]
#yukarıdan 120 pikselden 640. piksele kadar. soldan 420.den 840.piksele kadar
cv.imshow("img", img)
cv.imshow("crop_img", crop_img)
cv.waitKey(0)

#koordinatları görebilmek için: matplot kütüphanesi
img_rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()