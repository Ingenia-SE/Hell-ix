# Software
Here it is included the software implementation for the Hell-ix group participation in the INGENIA-SE ADR Challenge 2022-2023. The folder includes the code used for the different tests of the competition as well as simple tests that have been used in order to check the correct performance of the drone.

## Contents

### Freestyle Test
This folder shows the different programs that have been used to compete in the freestyle test. This test is based on making free flight trajectories with the drone and they are valued based on their originality and difficulty. In this case, they have been created two trajectories: one in the shape of a vertical five-pointed star and a spiral.

### Path Follower Assisted by Computer Vision
This folder shows the programs with which the drone has been able to follow a trajectory based on the data available in a ".csv" file. In this way, a series of setpoints are established through the different position parameters (x, y, z, angle) in which the drone must be located. It must go from point to point in a certain time that is passed to it as a parameter. In this way the speed is adjusted.

In addition, a vision algorithm has been added to one of the programs that allows it to correct the trajectory based on the analysis made of the images that the drone takes with its camera.

### Race Trajectory Planner
This program enables the  **generation of a .csv file** with the 3D coordinates of the  **optimal trajectory** that  the drone must follow in  order to pass through  a set of  given  gates. The  program enables  to  determine the optimal trajectory by defining the center points through which the drone should pass, as well as other parameters such as  the direction in which it should pass  each of the gates. The trajectory can also be  optimized as  a function of the  ratio power to  weight  of the drone,  that  will  define  how  sharp  these  trajectories corners  can be. This is done by modifying what's called the "tension" on each of the gates. The program plots a figure where the different obstacles can be seen in the order the drone will pass through them, together with the optimized trajectory. The disposition of the obstacles is **fully configurable**, enabling to change number of obstacles, their positions and orientations and size.

### Tests
In this folder the python scripts used to test the drone for performing simple tasks are included. Two tests have been included: one for simple take-off, maintaining the position and landing, and the second one to follow a straight line.

## Use of the Programs
In order to compile and use the code that has been designed in this project, you must use **Python**, since it is the programming language that has been used to develop all the test programs. If you don't have it installed, you can get it from the following link: https://www.python.org/downloads/
Once this tool is available, the next thing will be to have a code editor, in this case **Visual Studio Code** has been used. Which can be downloaded through the following link: https://code.visualstudio.com/download.

When installing Python, you can make use of a number of libraries such as **"math"**, **"time"**, **"logging"**, **"cmath"** or **"csv"**. However, the following additional libraries will need to be installed:
1. **cflib**: is the API written in Python used to communicate with Crazyflie. To install it, follow the steps described in the following link: https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/installation/install/.
2. **cv2 (OpenCV)**: contains the necessary functions to develop the vision algorithm. It can be downloaded through the following link: https://opencv.org/releases/.
3. **numpy**: used to perform numerical calculations. It can be installed by following the steps indicated in this link: https://numpy.org/install/.
