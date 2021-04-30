import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/0003.jpeg")

cv.imshow('Weirdo', img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)
