import cv2 as cv

img = cv.imread("./Resources/Photos/0003.jpeg")
# cv.imshow('0003.jpeg', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# cv.imshow('Gray Image', gray)

# Converting to Blur image
blur_img = cv.blur(img, (50, 50))
# cv.imshow('blurred image', blur_img)

# Converting to Gaussian Blur
gaussian_blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', gaussian_blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)

# Reduce the amount of edges by passing a blur image
canny_blur = cv.Canny(gaussian_blur, 125, 175)
# cv.imshow('Canny Edges', canny_blur)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow("Eroded image", eroded)

# Resize
resized = cv.resize(img, (1000, 1000), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
