import cv2
import numpy as np
import sys

def resize_img(img, size=600):
    r = float(size) / img.shape[1]
    dim = (size, int(img.shape[0] * r))
    rimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    return rimg

cascade = cv2.CascadeClassifier('ball_cascade.xml')

img = cv2.imread(sys.argv[1])
# rimg = resize_img(img, size=600)

# gray = cv2.cvtColor(rimg, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
balls = cascade.detectMultiScale(gray)
print(balls)

for (x, y, w, h) in balls:
    print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

rimg = resize_img(img, size=600)
cv2.imshow('img', rimg)

c = cv2.waitKey(0)
if c == chr(c & 255):
    cv2.destroyAllWindows()
