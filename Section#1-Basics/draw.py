import cv2 as cv
import numpy as np

# Working on a Blank Image
blank = np.zeros((500,500), dtype='uint8')
cv.imshow('Blank', blank)

cv.waitKey(0)
