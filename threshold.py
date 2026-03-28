import cv2 as cv
img=cv.imread("bear.jpg", cv.IMREAD_COLOR)

#görseli ölçekledirme
cv.namedWindow("bear", cv.WINDOW_NORMAL) 
cv.imshow("bear", img)
cv.waitKey(10)
"----------"
gri=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.namedWindow("gri", cv.WINDOW_NORMAL) 
cv.imshow("gri", gri)
"----------"
#EŞİKLEME: görüntüyü sadece siyah beyazdan oluşan binary matrise indirgeyerek arka plandan ayırmak
ret, yeni=cv.threshold(gri, 100, 255, cv.THRESH_BINARY)
#100den büyükse beyaz, 100den kucukse siyah
#ret: eşik değeri, yeni: eşikleme sonucu
cv.namedWindow("yeni", cv.WINDOW_NORMAL) 
cv.imshow("yeni", yeni)

cv.waitKey(0)
cv.destroyAllWindows()