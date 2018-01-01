import numpy as np
import cv2
import sys
import imutils
import time
import os

def resize_img(img, size=600):
    r = float(size) / img.shape[1]
    dim = (size, int(img.shape[0] * r))
    rimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    return rimg

def frame_no(img_name):
    suffix = img_name.split('_')[1]
    return int(suffix.split('.')[0])

frames = sorted([frame for frame in os.listdir('weighted_images') if frame[-4:] == '.jpg'], key=frame_no)

for img_name in frames:
    img = cv2.imread('weighted_images/' + img_name, -1)
    rimg = resize_img(img, size=1000)

    # cv2.putText(frame, str(weight), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(rimg, str(frame_no(img_name)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('frame', rimg)

    time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
