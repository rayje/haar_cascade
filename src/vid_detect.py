import cv2
import numpy as np
import sys

def resize_img(img, size=600):
    r = float(size) / img.shape[1]
    dim = (size, int(img.shape[0] * r))
    rimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    return rimg

cascade = cv2.CascadeClassifier('ball_cascade.xml')
cap = cv2.VideoCapture(sys.argv[1])

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ball_detect.avi',fourcc, 20.0, (1920,1080))

weights = []
y_values = []
min_x = 630
max_x = 1260
min_y = 236
max_y = 800

def in_bounds(x, y, w, h):
    return x > min_x and x+w < max_x and y > min_y and y+h < max_y

frame_no = 1
while(True):
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # balls = cascade.detectMultiScale(gray, 20, 4)
    balls, rejectLevels, levelWeights = cascade.detectMultiScale3(
        gray, 
        # scaleFactor=1.1, 
        minNeighbors=5,
        minSize=(50,50), 
        # flags=cv2.CASCADE_SCALE_IMAGE, 
        outputRejectLevels=True)

    if len(balls) > 0:
        collect = False
        print(frame_no, len(balls))
        for i in range(len(balls)):
            (x, y, w, h) = balls[i]
            weight = levelWeights[i][0]

            if in_bounds(x, y, w, h):
                # collect = True

                if weight >= 3.34:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, str(weight), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                    cv2.putText(frame, str(weight), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            # else:
            #     # if weight > 1.27543717:
            #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            #     cv2.putText(frame, str(weight), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # if collect:
            # cv2.imwrite('weighted_images/image' + str(frame_no) + '.jpg', frame)

        # if collect:
            # weights += lw
            # print(balls)
            # print('rejectLevels:', rejectLevels, 'levelWeights:', levelWeights)

    
    # Draw a box on the frame. This is used to track a center boundary.
    cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (255, 0, 0), 2)

    # Resize and rotate the image
    # rimg = resize_img(frame)
    # rimg = imutils.rotate(rimg, -90)

    # Show the image
    # cv2.imshow('img', rimg)

    # Write the frame to a new video file
    out.write(frame)

    frame_no += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# if len(weights) > 0:
#     print('weights avg:', sum(weights)/len(weights))
#     print('min weight:', min(weights), 'max weight:', max(weights))
# print(weights)
# print(min(y_values), max(y_values))
out.release()
cv2.destroyAllWindows()
