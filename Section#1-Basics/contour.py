import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/0003.jpeg")

cv.imshow('Weirdo', img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)


cv.waitKey(0)
