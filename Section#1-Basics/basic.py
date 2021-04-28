import cv2 as cv

img = cv.imread("./Resources/Photos/0003.jpeg")
cv.imshow('0003.jpeg', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray Image', gray)

# Converting to Blur image
blurImg = cv.blur(img, (50, 50))
cv.imshow('blurred image', blurImg)

# Converting to Gaussian Blur
gaussianBlur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', gaussianBlur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

cv.waitKey(0)
