import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/0003.jpeg")
cv.imshow('Weirdo', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)


cv.waitKey(0)
