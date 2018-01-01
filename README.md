# Haar Cascades

This repo contains code for experiments used while learning about [Haar Cascades](https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html) in OpenCV.

The goal of this was to be able to track a ball within a video using OpenCV.

### Steps
The steps taken for this were:
1. Capture images of the ball to be tracked, using images converted from video.
2. Preprocess the images to contain just the ball using OpenCV's HoughCircles class, and crop the images to the detected circles.
3. Convert the cropped images to a vector file for training.
4. Use `opencv_traincascade` to train and generate a cascade.xml that can be used during detection.
5. Detect images in video frames using the trained model.

#### Code

**Positive Images**: Images that contain the object to be detected.
**Negative Images**: Images that do not contain the object to be detected.

##### Convert video to images
The data sets used for these experiments were captured by converting frames from a video to images.

The `vid_to_img.py` script takes care of this by using OpenCV's VideoCapture class and resizing the images so that they can be processed at a later stage.

This script was used to collect both positive and negative images.

##### Circle Detect
To detect the ball in the training images, the `circle_detect.py` script will use HoughCircles. The script assumes that the largest circle in the image is the ball, and crops the image so that it contains only the ball.

##### Create Samples
Once the images are cropped for training, we now need to create a vector file that can be used by the `opencv_traincascade` script.

Before running the `create_samples.sh` script, we need to create a `positives.txt` and a `bg.txt` file that can be used to when generating the samples vector file.

```bash
# Assuming cropped files exist in ./cropped_images directory
cd ./cropped_images
find . -iname "*.jpg" > positives.txt
```

```bash
# Assuming negative images exist in negative_images directory
cd negative_images
find . -iname "*.jpg" > negatives.txt
```

Once these files are created, the script `create_samples.sh` can be run.

The result should be a vector file will be created `samples.vec`.

##### Training
To train the cascade, run the `train.sh` script. If all the previous steps were followed, the `samples.vec` file should have been created.

**Note**: The `train.sh` script assumes a `data` directory exists. If it does not, create it before running the script.

##### Evaluation
To test the cascade, the `vid_detect.py` script can be used to test if the cascade can detect the object within a video frame.

The video used for the original testing had a ball in the center of each frame. So, the script draws a box to create a visual reference of the center of the frame. All boxes detected by the cascade are evaluated to determine if the fall within the center boundary. With this, the code can be modified to do one of the following:
* Draw the detected box if the box falls within the center boundary
* Ignore the detected boxes that fall outside the center boundary
* Use the levelWeight value to draw green boxes for higher levelWeights, and yellow boxes for lower weights.
