import cv2 as cv

# Reading Videos
# You can use int 0 for referencing to webcam
capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

# Reading a video using a while loop to read the video frame by frame
while True:
    isTrue, frame = capture.read()

    # To show the video frame by frame
    cv.imshow('Video', frame)

    # To stop the video from running infinitely, if the letter 'd' is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

cv.destroyAllWindows()
