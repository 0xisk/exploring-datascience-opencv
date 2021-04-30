import cv2 as cv
import numpy as np

img = cv.imread("./Resources/Photos/0003.jpeg")

cv.imshow('Weirdo', img)

# Translation
def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rot_point=None):
    (height, width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width//2, height//2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rot_mat, dimensions)

# + ---> Counter clock wise rotation
# - ---> Clock wise rotation
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_clockwise = rotate(img, -45)
cv.imshow('Rotated', rotated_clockwise)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Flipping

# 0 ---> Flip vertically
# 1 ---> Flip horizontally
# -1 --> Both
vertical_flip = cv.flip(img, 0)
cv.imshow("Flip", vertical_flip)

horizontal_flip = cv.flip(img, 1)
cv.imshow("Horizontal", horizontal_flip)

cv.waitKey(0)

