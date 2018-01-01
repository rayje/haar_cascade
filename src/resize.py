import numpy as np
import cv2
import os

for img_name in os.listdir('negative_images'):
    if img_name[-4:] != '.jpg':
        continue

    img = cv2.imread('negative_images/' + img_name)
    
    rimg = cv2.resize(img, (250, 250))
    cv2.imwrite('resized_negatives/' + img_name, rimg)
    print('created', 'resized_negatives/' + img_name)
