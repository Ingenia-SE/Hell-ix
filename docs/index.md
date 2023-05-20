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
  <summary>Images</summary>
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/trajectory_planner.png">
   
  </p>
  <p align="center">Trayectory planner</p>
</details>


### Computer Vision

### Drone Racing Competition Simulation Environment
  
  
## Installation


## Setup Guide

### Hardware setup

Once the Crazyflie 2.1 box is in hands on the team, it is important to be aware of what this package is formed by. It contains various components that are essential for its assembly. Ensure that you have all the following items before proceeding with the setup.

The box contains the following components:
  
- 1 x Crazyflie 2.X control board with all components mounted
- 5 x CW propellers
- 5 x CCW propellers
- 6 x Motor mounts
- 1 x LiPo battery
- 5 x Coreless DC motors
- 2 x Short expansion connector pins (1×10, 2mm spacing, 8 mm long)
- 2 x Long expansion connector pins (1×10, 2mm spacing, 14 mm long)
- 1 x Battery holder expansion board
- 1 x USB cable (only with the Crazyflie 2.1)

#### Power-on self-test

The Crazyflie 2.1 undergoes extensive testing during production, but it's recommended to run tests before assembling it to ensure nothing went wrong during shipping or storage. To do this, power on the Crazyflie 2.1 using a USB source (computer or charger) and check the test results. During the test, it's important to hold the Crazyflie 2.1 steady and keep it away from strong magnetic sources.

To perform the power-on self-test, connect the Crazyflie 2.1 to a USB power source. The test result is indicated by the LEDs M1 and M4. If the M4 LED blinks green five times rapidly, it means the test has passed.
In case the self-test fails, the M1 LED will blink red five times rapidly, followed by a pause and repetition. In such a situation, it is recommended to seek help by visiting the support discussions provided by the manufacturer.

<b>Note:The Crazyflie 2.1 has four LEDs labeled M1, M2, M3, and M4, which correspond to each of the four motors. These LEDs provide visual feedback on the status and operation of the respective motors during flight or testing. They help users monitor the individual motor status and detect any potential issues or abnormalities.</b>

<details>
  <summary>Crazyflie Leds Images</summary>
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/CrazyflieLeds.jpeg" style="width: 700px; height: 400px;">
   
  </p>
  <p align="center">Crazyflie LEDs</p>
 
</details>

#### Assembling

The assembly process of the Crazyflie 2.1 can typically be completed in under 10 minutes. However, it is crucial to take into account a few important considerations. Thus, it is imperative to correctly follow the provided instructions:

- **Wire Twisting**: Begin by twisting the wires of the four motors. This technique serves to minimize electronic noise and enhance the fit of the wires within the motor mount "hooks". 

- **Motor Mounting**: Push the four motors firmly into the motor mounts. Some force may be required for insertion. If encountering difficulty, try placing the motor can towards the edge of a table and apply pressure on the mount. However, exercise caution to avoid pressing on the motor axis, as it could potentially damage the motor. Ensure that the motor is fully inserted until it reaches the stop within the mount.

- **Twisted Wire Attachment**: Connect the twisted wire into the two small "hooks" positioned beneath the motor mount.

- **Motor Mount Insertion**: Proceed to insert the motor mounts onto the wings of the Crazyflie 2.1. These mounts are press-fit and may necessitate a gentle application of force. Ensure that they are fully inserted until they reach the stop. The specific placement of each motor is not critical. Once inserted, connect the motor connectors to the corresponding ports on the Crazyflie 2.1.

- **Propeller Attachment**: Now, it is time to attach the propellers. Note that two types of propellers are provided: clock-wise (CW) and counter-clockwise (CCW). Each type is packaged separately in the box. Carefully examine the shape of the tips and verify the correct rotation direction. Typically, CW propellers are labeled with an "A" or "A1" marking, while CCW propellers bear a "B" or "B1" marking. Additionally, ensure that the propellers are correctly oriented, with the convex side facing upwards.

<details>
  <summary>Propeller Images</summary>
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/RotorBlades%26Motors.jpeg" style="width: 300px; height: 200px;">
   
  </p>
  <p align="center">Two types of motors and propellers, the transparent ones are larger and are paired with more powerful motors.</p>
  
  
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/RotorBlade.jpeg" style="width: 300px; height: 200px;">
   
  </p>
  <p align="center">Standard propeller view</p>
</details>

- **Rubber Pad Attachment**: Affix the rubber pad to the Crazyflie 2.1 between the expansion headers.

- **Header Attachment**: Inside the box, you will find long and short headers. Select the two short headers and insert them into the expansion connector.

- **Battery Attachment**: Position the battery between the headers inserted into the expansion connector. Proceed to insert the battery holder board onto the headers, taking care with the sharp pins during insertion. The friction provided by the connections should securely hold the battery in place. Tighten it until it remains firmly fixed.

- **Battery Connection**: Connect the battery to finalize the assembly process. It is advisable to bend the battery wires and position them underneath the PCB to ensure they are out of the way.

<details>
  <summary>Battery Images</summary>
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/Battery.jpeg" style="width: 300px; height: 200px;">
   
  </p>
  <p align="center">Battery view</p>
  
  
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/BatteryHolderDeck.jpeg" style="width: 300px; height: 200px;">
   
  </p>
  <p align="center">Battery oblicual view</p>
</details>

- **Power-On**: The assembly is now complete, and it is time to power on the device. Note that the power button is a push button, not a sliding button. During the power-on self-test, observe the sequential spinning of all propellers. Verify that each propeller spins correctly. If any propellers fail to spin, check the motor connections for proper engagement.

By meticulously following these instructions, you have successfully completed the assembly process of the device. It is essential to ensure that all components are securely connected, and the power-on self-test confirms the appropriate functioning of the propellers.

<details>
  <summary>Assembled Crazyflie Images</summary>
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/AssembledCrazyflie_TopView.jpeg" style="width: 300px; height: 200px;">
   
  </p>
  <p align="center">Top view</p>
  
  
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/AssembledCrazyflie_BottomView.jpeg" style="width: 300px; height: 200px;">
   
  </p>
  <p align="center">Bottom view</p>
</details>

### Software setup

## Simulation Guide



## User Guide


## Maintenance and Operations Manual
