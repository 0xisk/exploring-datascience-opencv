import cv2 as cv

img = cv.imread("./Resources/Photos/0003.jpeg")
cv.imshow('Weirdo', img)

cv.waitKey(0)
