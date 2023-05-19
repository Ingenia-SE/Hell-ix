# Race Trajectory Planner

## Description of the Program

This program enables the  **generation of a .csv file** with the 3D coordinates of the  **optimal trajectory** that  the drone must follow in  order to pass through  a set of  given  gates. The  program enables  to  determine the optimal trajectory by defining the center points through which the drone should pass, as well as other parameters such as  the direction in which it should pass  each of the gates. The trajectory can also be  optimized as  a function of the  ratio power to  weight  of the drone,  that  will  define  how  sharp  these  trajectories corners  can be. This is done by modifying what's called the "tension" on each of the gates. The program plots a figure where the different obstacles can be seen in the order the drone will pass through them, together with the optimized trajectory. The disposition of the obstacles is **fully configurable**, enabling to change number of obstacles, their positions and orientations and size.

## Program Files

1. **Main program trajectory_planner.m**: This is the main program which creates the .csv file with the optimal trajectory.
2. **Function hobbysplines.m**: This is a function developped by Will Robertson and the University of Adelaide that has been slightly modified. It employs Hobby's algorithm for choosing control points based on curvature and tension in order to draw 3D Bezier curves. 
3. **Function plotGate.m**: This is a function to plot a gate given its position and orientation.

<img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/trajectory_planner.png?raw=true" alt="Hell-ix-Logo" width="1000">
