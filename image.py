import cv2
import numpy

def convert(frame):
    cv2.imwrite("image.png", frame)