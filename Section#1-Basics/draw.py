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

# 2. Draw a Rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('Rectangle Blank', blank)

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Filled Rectangle Blank', blank)

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=-1)
cv.imshow('Filled Rectangle Blank', blank)

cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('Filled Rectangle Blank with black.shape dimensions', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv.imshow('Circle Blank', blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255, 255, 0), thickness=-1)
cv.imshow('Thick Circle Blank', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line Blank', blank)

cv.waitKey(0)
