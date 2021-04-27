import cv2 as cv 

# img = cv.imread('./Resources/Photos/cat_large.jpg')
# cv.imshow('Cat', img)


def rescale_frame(frame, scale=0.75):
    # frame.shape[1] = frame width
    width = int(frame.shape[1] * scale)
    # frame.shape[0] = frame height
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading Videos
# You can use int 0 for referencing to webcam
capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

# Reading a video using a while loop to read the video frame by frame
while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame, scale=.2)

    # To show the video frame by frame
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # To stop the video from running infinitely, if the letter 'd' is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

cv.destroyAllWindows()

