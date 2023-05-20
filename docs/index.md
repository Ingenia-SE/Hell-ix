<img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/logo_background.png?raw=true" alt="Hell-ix-Logo" width="210">

# Hell-ix Project

This GitHub repository is home to the **Autonomous Drone Racing Challenge 2022-2023**, a project in progress by Hell-ix and Droning teams. In particular, this repository includes the work done by Hell-ix team. The aim of the project is to organize an Autonomous Drone Racing (ADR) competition between two drones (each one managed by one team). The objetive for each team is to win the competition by performing the best as possible.

## What is ADR Challenge 2022-2023?
The ADR Challenge is a competition that will be held as a result of the INGENIA-SE 2022-2023. The competition will face two teams: **Hell-ix** and Droning. The competition will consist of **three main tests**: a straight-line speed race through four gates, a race through four gates forming a semicircle, and a freestyle test. 

## Features
The project has three main modules aimed at achieving autonomous operation of the drone.


### Race Trajectory Planner
The first main module consist on a program which generates a .csv file that contains the 3D coordinates of the best possible flight path for the drone to navigate through a series of designated gates. By defining specific center points for the drone to pass through and providing additional parameters such as gate orientations, the program calculates the most efficient trajectory. Furthermore, the trajectory can be optimized based on the drone's power-to-weight ratio, which determines how sharply it can maneuver around corners. This optimization is achieved by adjusting the "tension" at each gate. The program also provides a visual representation where the obstacles, arranged in the order the drone will encounter them, are displayed alongside the optimized flight path. Users have complete flexibility to configure the obstacles, including the ability to modify their number, positions, orientations, and sizes.

The program is formed by three different files:
- The main program, **trajectory_planner.m**, is responsible for generating the optimal trajectory and creating a .csv file. It utilizes various algorithms and functions to determine the best flight path for the drone to navigate through the gates.
- One of the essential functions used in the program is **hobbysplines.m**. Originally developed by Will Robertson and the University of Adelaide, this function has been slightly modified for this particular application. It leverages Hobby's algorithm, which takes into account curvature and tension, to select control points for drawing 3D Bezier curves. By employing this method, smooth and visually pleasing trajectories can be achieved.
- Another useful function is **plotGate.m**. This function serves the purpose of visualizing gates on a plot based on their positions and orientations. It enables the program to display the gates in a clear and understandable manner, allowing users to see the arrangement of gates along with the optimized trajectory.

Overall, the combination of the main program, **trajectory_planner.m**, the modified **hobbysplines.m** function, and the **plotGate.m** function provides a comprehensive solution for generating optimal trajectories, drawing smooth 3D Bezier curves, and visualizing the gates, resulting in an effective and user-friendly program for drone navigation.

<details>
  <summary><b>Images<b></summary>
  <p align="center">
    <img src="https://github.com/Ingenia-SE/Hell-ix/raw/main/img/trajectory_planner.png" alt="Trajectory Planner">
  </p>
  <p align="center">Four gates trayectory planner </p>
</details>
<br>



### Computer Vision

### Drone Racing Competition Simulation Environment
  
  
## Installation


## Setup Guide


## Simulation Guide


## User Guide


## Maintenance and Operations Manual
