import cv2
import time
import image
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    cv2.imshow("My video", frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()