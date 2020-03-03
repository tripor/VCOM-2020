import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    cv.imshow('cam', frame)
    if cv.waitKey(1) == ord('q'):
        saved_frame=frame
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
cv.imshow('frame',saved_frame)
cv.waitKey(0)



cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('cam', frame)
    cv.imshow('gray_cam',frame_gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    cv.imshow('cam', frame)
    frame_strange = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    frame_strange[frame_strange < 128] = 0
    frame_strange[frame_strange >= 128] = 255
    cv.imshow('strange_cam',frame_strange)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()