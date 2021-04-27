import cv2 as cv 

img = cv.imread('./Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.75):
    # frame.shape[1] = frame width
    width = int(frame.shape[1] * scale)
    # frame.shape[0] = frame height
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


cv.waitKey(0)
