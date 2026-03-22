import os
from os import waitpid

import cv2 as cv
img= cv.imread(os.path.join(".", "dogs.jpg"))

resize_img= cv.resize(img, (600,488))

start_y, end_y=100,300
start_x ,end_x=100,450

k=33
#görüntünün kopyasını oluştur
select_blur= resize_img.copy()
#ilgili parçayı bellekte ayır
roi_blur=select_blur[start_y: end_y, start_x:end_x]. copy()
#kopyalanan bölgeye bulanıklaştırma uygula
roi=cv.blur(roi_blur, (k,k))
#bulanıklaşan bölgeyi netin üstüne yapıştır
select_blur[start_y:end_y, start_x:end_x]= roi

cv.imshow("bugulu", select_blur)
"-----------"
"tüm görüntü bulanık"
full_blur= cv.blur(resize_img, (k,k))
roi_full= resize_img[start_y:end_y, start_x:end_x]. copy()
full_select= full_blur.copy()
full_select[start_y:end_y, start_x:end_x] = roi_full

cv.imshow("full bugulu", full_select)
cv.waitKey()
cv.destroyWindow()