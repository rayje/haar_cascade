import numpy as np
import cv2
import sys
import imutils

def resize_img(img, size=600):
    r = float(size) / img.shape[1]
    dim = (size, int(img.shape[0] * r))
    rimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    return rimg

cap = cv2.VideoCapture(sys.argv[1])
id = 1

while(True):
    ret, frame = cap.read()
    if not ret:
        break

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # gray = imutils.rotate(gray, -90)
    # rimg = imutils.rotate(frame, -90)
    rimg = resize_img(frame, 1000)

    # cv2.imshow('frame', rimg)
    # cv2.imwrite('ball_images/image' + str(id) + '.jpg', rimg)
    cv2.imwrite('test_images/image' + str(id) + '.jpg', rimg)
    # cv2.imwrite('negative_images/image' + str(id) + '.jpg', rimg)
    id += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(id)
cap.release()
cv2.destroyAllWindows()
