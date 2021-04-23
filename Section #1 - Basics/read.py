import cv2 as cv

img = cv.imread("../Resources/Photos/cat.jpg")

img_large = cv.imread("../Resources/Photos/cat_large.jpg")

# cv.imshow('Cat', img)
cv.imshow('Cat', img_large)

cv.waitKey(0)
