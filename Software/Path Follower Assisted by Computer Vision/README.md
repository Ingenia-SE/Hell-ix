# Path Follower Assisted by Computer Vision

## Description of the Program
In the first test (**csv_follower.py**), the drone must pass through a series of gates in a certain amount of time.
To do this, a series of setpoints defined in a csv file are read, which describes the trajectory that the drone must follow in order to pass through all the obstacles.
In addition, in the second test (**csv_follower_vision.py**) a function has been defined that must read the images provided by the drone's AI Deck camera, analyse them and determine the centre of the gates.
In this way, the drone is able to correct any errors in the original trajectory by means of the vision algorithm.

## Vision algorithm
After receiving the images from the camera, they are processed in this way:
1. A Gaussian blur is performed to homogenise the image.
2. The colour format is changed from RGB to HSV.
3. Masks are created from the parts of the image that fall within a defined colour range. In this case, the white and orange areas will be identified, as the obstacles are of this colour.
4. By superimposing both masks, the contours of the doors to be crossed are obtained.
5. The next step is to detect the centre of the nearest contour by means of a function that returns the centre of the contour it receives as a parameter.

## Position Correction
Once the position of the centre of the door to be crossed is known, it is necessary to correct the position of the drone in such a way that it manages to centre the centre of the door in the image, in order to be sure that the drone is going to cross it.

It is necessary to modify two parameters, the yaw and the height. To do this, two constants are defined that will be multiplied by the errors detected in the parameters to be modified, in order to be able to add these values to those that have been read from the csv. In this way, it is possible to vary the value of these parameters sufficiently to correct these small trajectory errors and pass through the obstacles successfully.
