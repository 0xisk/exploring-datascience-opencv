import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt

img = cv.imread("./Resources/Photos/0003.jpeg")
cv.imshow('Weirdo', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_RGB2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('RGB', rgb)

# Reverse

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV ---> BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('HSV ---> LAB', lab_bgr)

cv.waitKey(0)
