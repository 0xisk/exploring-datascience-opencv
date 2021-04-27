import cv2 as cv 


def rescale_frame(frame, scale=0.75):
    """ This Rescaling function is working for
    Images, Videos, and Live Video

    :param frame:
    :param scale:
    :return:
    """

    # frame.shape[1] = frame width
    width = int(frame.shape[1] * scale)
    # frame.shape[0] = frame height
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_resolution(width, height):
    """ This function used for Live Videos, like reading from
    external camera, or web cam.

    :param width:
    :param height:
    """
    capture.set(3, width)
    capture.set(4, height)


# Rescaling Images
img = cv.imread('./Resources/Photos/cat.jpg')
resized_image = rescale_frame(img)

cv.imshow('Cat', img)
cv.imshow('Cat Resized', resized_image)

cv.waitKey(0)

# Rescaling Videos
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

