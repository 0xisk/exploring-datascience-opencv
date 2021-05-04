import cv2 as cv

img = cv.imread("./Resources/Photos/0003.jpeg")
cv.imshow('Weirdo', img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

cv.waitKey(0)
