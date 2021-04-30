import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/0003.jpeg")
cv.imshow('Weirdo', img)

b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Red', r)
cv.imshow('Green', g)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)
