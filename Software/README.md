# Software
Here it is included the software implementation for the Hell-ix group participation in the INGENIA-SE ADR Challenge 2022-2023. The folder includes the code used for the different tests of the competition as well as simple tests that have been used in order to check the correct performance of the drone.

## Contents

### Freestyle Test

### Path Follower Assisted by Computer Vision

### Race Trajectory Planner
This program enables the  **generation of a .csv file** with the 3D coordinates of the  **optimal trajectory** that  the drone must follow in  order to pass through  a set of  given  gates. The  program enables  to  determine the optimal trajectory by defining the center points through which the drone should pass, as well as other parameters such as  the direction in which it should pass  each of the gates. The trajectory can also be  optimized as  a function of the  ratio power to  weight  of the drone,  that  will  define  how  sharp  these  trajectories corners  can be. This is done by modifying what's called the "tension" on each of the gates. The program plots a figure where the different obstacles can be seen in the order the drone will pass through them, together with the optimized trajectory. The disposition of the obstacles is **fully configurable**, enabling to change number of obstacles, their positions and orientations and size.

### Tests
In this folder the python scripts used to test the drone for performing simple tasks are included. Two tests have been included: one for simple take-off, maintaining the position and landing, and the second one to follow a straight line.

## Use of the Programs
Talk about how to run the programs using an IDE and what are the necessary installations to run the programs, Crazyradio PA, etc.
