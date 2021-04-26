import cv2 as cv

# Reading Videos
capture = cv.VideoCapture('./Resources/Videos/dog.mp4') # You can use int 0 for refrencing to webcam

# Reading a video using a while loop to read the video frame by frame
while True:
    isTrue, frame = capture.read()

    # To show the video frame by frame
    cv.imshow('Video', frame)

    # To stop the video from running infinitly, if the letter 'd' is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()

cv.destroyAllWindows()
