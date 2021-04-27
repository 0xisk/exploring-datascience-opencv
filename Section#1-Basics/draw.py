import cv2 as cv
import numpy as np

# Working on a Blank Image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Point the image a certain colour
blank[:] = 0, 255, 0
cv.imshow('Green Blank', blank)

blank[:] = 0, 0, 255
cv.imshow('Red Blank', blank)

# Cutting a certain portion of the image
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Cut Blank', blank)

cv.waitKey(0)
