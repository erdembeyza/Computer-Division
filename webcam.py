import cv2 as cv
webcam= cv.VideoCapture(0)

while True:
  ret, frame= webcam.read()
  cv.imshow("pencere", frame)
  cv.waitKey(0) & 0xFF == ord("q") #yapmazsan sürekli açık kalır
  break

webcam.release()
cv.destroyAllWindows()  