import cv2 as cv

img = cv.imread("./Resources/Photos/0003.jpeg")
cv.imshow('0003.jpeg', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray Image', gray)

cv.waitKey(0)
