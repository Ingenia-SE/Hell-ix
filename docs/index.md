<img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/logo_background.png?raw=true" alt="Hell-ix Logo" width="210">

# Hell-ix Project

This GitHub repository is home to the **Autonomous Drone Racing Challenge 2022-2023**, a project in progress by Hell-ix and Droning teams. In particular, this repository includes the work done by Hell-ix team. The aim of the project is to organize an Autonomous Drone Racing (ADR) competition between two drones (each one managed by one team). The objetive for each team is to win the competition by performing the best as possible.

## What is ADR Challenge 2022-2023?
The ADR Challenge is a competition that will be held as a result of the INGENIA-SE 2022-2023. The competition will face two teams: **Hell-ix** and Droning. The competition will consist of **three main tests**: a straight-line speed race through four gates, a race through four gates forming a semicircle, and a freestyle test. 

## Features
The project has three main modules aimed at achieving autonomous operation of the drone.


### Race Trajectory Planner
The first main module consist on a program which generates a .csv file that contains the 3D coordinates of the best possible flight path for the drone to navigate through a series of designated gates. By defining specific center points for the drone to pass through and providing additional parameters such as gate orientations, the program calculates the most efficient trajectory. Furthermore, the trajectory can be optimized based on the drone's power-to-weight ratio, which determines how sharply it can maneuver around corners. This optimization is achieved by adjusting the "tension" at each gate. The program also provides a visual representation where the obstacles, arranged in the order the drone will encounter them, are displayed alongside the optimized flight path. Users have complete flexibility to configure the obstacles, including the ability to modify their number, positions, orientations, and sizes.

The program consists of three files. The main program, ```trajectory_planner.m```, generates an optimal trajectory and creates a .csv file. It utilizes various algorithms and functions, including the modified ```hobbysplines.m``` function, which employs Hobby's algorithm to select control points for smooth 3D Bezier curves. Additionally, it utilizes the ```plotGate.m``` function which visualizes the gates' positions and orientations, providing a clear representation of the gate arrangement along with the optimized trajectory.Overall, the combination of the main program, trajectory_planner.m, the modified hobbysplines.m function, and the plotGate.m function provides a comprehensive solution for generating optimal trajectories, drawing smooth 3D Bezier curves, and visualizing the gates, resulting in an effective and user-friendly program for drone navigation.

<details>
  <summary>Images</summary>
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/trajectory_planner.png?raw=true">
   
  </p>
  <p align="center">Trayectory planner</p>
</details>


### Computer Vision

The second main module consists of correcting the altitude and direction of the drone based on the obstacles it encounters along its path. To achieve this, the drone uses the camera it carries to recognize doors, aligning itself both in height and direction towards the center of the door. The operation of this algorithm relies on the use of another algorithm that reads the path to follow from an external file.

With the first script ```csv_follower.py```, the drone passes through a series of gates in a certain amount of time.
To do this, a series of setpoints defined in a csv file are read, which describes the trajectory that the drone must follow in order to pass through all the obstacles.
In addition to this, script ```csv_follower_vision.py``` has been programmed with an additional function that reads the images provided by the drone's AI-deck camera, analyzes them and determines the centre of the gates.
Once the position of the centre of the door to be crossed is known, it is necessary to correct the position of the drone in such a way that it manages to centre the centre of the door in the image, in order to be sure that the drone is going to cross it.

It is necessary to modify two parameters, the yaw and the height. To do this, two constants "K" are defined that will be multiplied by the errors detected in the parameters to be modified, in order to be able to add these values to those that have been read from the csv. In this way, it is possible to vary the value of these parameters sufficiently to correct these small trajectory errors and pass through the obstacles successfully.
In this way, the drone is able to correct any errors in the original trajectory by means of the vision algorithm.

<details>
  <summary>Gate recognition Example</summary>
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/vision_algorithm.gif" width="640">
   
  </p>
  <p align="center">Example of door recognition.</p>
  

</details>


### Drone Racing Competition Simulation Environment

The third main module consists of performing simulations in the open-source software Webots. This program allows creating simulation environments by importing 3D models, which facilitates their visualization. Additionally, it allows using different programming languages to carry out the simulation. All the information related to the program can be found on the [Cyberbotics website](https://cyberbotics.com/).

In this module, the main codes that govern the behavior of the drone are collected in the folder /webots/controllers, where both C and Python codes can be found. These codes (**pid_controller** and **pid_controller_position**) simulate the behavior of the drone using PID, where the first one is responsible for controlling the velocity of the drone, and the second one controls the position. The remaining files are primarily used to create the 3D space in the simulation program.

<details>
  <summary>Simulations</summary>
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/test_1_simulation.gif"width="640">
   
  </p>
  <p align="center">Test 1 - Four-obstacles straight line</p>
  
   <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/test_2_simulation.gif"width="640">
   
  </p>
  <p align="center">Test 2 - Four-obstacles semicircle</p>
</details>
  
## Installation
**Requirements:** [Python 3.8](https://www.python.org/downloads/release/python-3816/) or later. Code editor software (like [Visual Studio](https://code.visualstudio.com/download)). Matlab (or Octave) for creating the trajectory to be followed by the drone.

Next, all the software requirements needed for using this project's files and their installation are explained.

<details>
  <summary> Python libraries needed </summary>
  
- **cflib**: is the API written in Python used to communicate with Crazyflie. To install it, follow the steps described in the following [link](https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/installation/install/).
- **cv2 (OpenCV)**: contains the necessary functions to develop the vision algorithm. It can be downloaded through the following [link](https://opencv.org/releases/).
- **numpy**: used to perform numerical calculations. It can be installed by following the steps indicated in this [link](https://numpy.org/install/).
  
</details>
<details>
  <summary> CFClient installation </summary>
  
- **Install the CFClient**: Begin by installing the [CFClient software](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/userguides/userguide_client/) from the source code on your computer. This software serves as the interface for controlling the Crazyflie. If you don't have it installed, press the link and follow the guide steps.

- **Connect the Crazyradio**: Plug in the Crazyradio 2.0 or Crazyradio PA into a USB port on your computer. This radio module facilitates communication between the CFClient and the Crazyflie.
</details>
<details>
  <summary> Crazyradio 2.0 firmware update </summary>
  
- The first thing to do is to assemble the hardware, which contains the Antenna and the Crazyradio 2.0 USB dongle. 
  
- Continue setting the antenna on to the connector on the USB dongle.
  
- To flash new firmware to the Crazyradio 2.0 , it must first be set to the bootloader mode.
  
- Press and hold the button.
  
- Insert the USB dongle into a USB port while holding the button.
  
- Verify that the LED is pulsating with a red light, this indicates that the Crazyradio 2.0  is in bootloader mode.
  
- When in bootloader mode, the Crazyradio 2.0  will appear as a USB drive in your operating system. Firmware is installed by copying a .uf2 firmware file to the drive.
  
- Open a file browser and find the drive named Crazyradio2.
  
- Go to the release page on github. Download the file named ```crazyradio2-CRPA-emulation-[version].uf2``` by clicking on it.
  
- In your file browser, drag and drop the downloaded file to the Crazyradio2 drive.
  
- The installation takes less than a second and when done, the Crazyradio 2.0  will restart running the new firmware. Since it is no longer in bootloader mode, the USB drive will no longer be available.

When the Crayradio PA emulation firmware starts up, the LED will light up briefly in white. If you missed it when flashing, unplug and re-plug the Crazyradio 2.0  to restart it.The Crazyradio 2.0 will be nowready to use and it will behave like a Crazyradio PA, which means it will be compatible with all the products in the Crazyflie ecosystem.

<b>Note</b>: Depending on which operating system you use, you will have to install drivers or do some configuration to communicate with the Crazyradio 2.0. 
 </details>
  <details>
    <summary>Drivers installation</summary>
To install the necessary drivers for the Bitcraze device, follow these steps:

- Download Zadig: Visit the website http://zadig.akeo.ie/ and download the Zadig software.

- Connect the Bitcraze device to your PC: Plug in the Bitcraze device, and Windows will display an installation window. Note that on Windows 8 and 10, the window may close automatically without any action. On Windows 7, you need to close the "install failed" window.

- Launch Zadig: Open the Zadig software. You should see a list of devices available.

- Select the Device and Driver: Locate your Bitcraze device in the list and select it. Choose "libusb" as the driver option.

- Install the Driver: Click the "Install" button to begin the driver installation process.

- Wait for Installation: The installation process will run, and it should complete successfully. The duration of the installation can vary, ranging from quick to a few minutes.

By following these steps, you can download Zadig, connect the Bitcraze device, and install the required drivers for proper functionality.
  </details>

<details>
  <summary> Simulation Software </summary>

  It is necessary to have the Webots simulation program installed in order to run the simulation files. This software can be obtained through the following [link](https://cyberbotics.com/#download).
  
</details>



## Setup Guide

### Hardware setup

Once the Crazyflie 2.1 box is in the team's hands, it is important to be aware of what this package is formed by. It contains various components that are essential for its assembly. Ensure that you have all the following items before proceeding with the setup.
<details>
    <summary>Components</summary>
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
</details>

#### Power-on self-test

The Crazyflie 2.1 undergoes extensive testing during production, but it's recommended to run tests before assembling it to ensure nothing went wrong during shipping or storage. To do this, power on the Crazyflie 2.1 using a USB source (computer or charger) and check the test results. During the test, it's important to hold the Crazyflie 2.1 steady and keep it away from strong magnetic sources.

To perform the power-on self-test, connect the Crazyflie 2.1 to a USB power source. The test result is indicated by the LEDs M1 and M4. If the M4 LED blinks green five times rapidly, it means the test has passed.
In case the self-test fails, the M1 LED will blink red five times rapidly, followed by a pause and repetition. In such a situation, it is recommended to seek help by visiting the support discussions provided by the manufacturer.

<details>
    <summary>Crazyflie Leds</summary>
  
The Crazyflie 2.1 has four LEDs, each serving a specific purpose:

- **M1: The front right LED (1)**

  - Power on and all is good: Blinks red twice every second.
  - Power on, but sensors are not yet calibrated: Blinks red with a 2-second interval. Calibrate the sensors by placing the Crazyflie 2.X on a level surface and keeping it still.
  - Battery low: Fully lit in red. Indicates that it's time to land and recharge the battery.
  - Self-test fail: Repeatedly blinks five short red pulses with a longer pause between groups.
- **M2 and M3: Blue LEDs (2 and 3) at the back**

  - Power on and all is good: Fully lit.
  - Power on, but sensors are not yet calibrated: Fully lit.
  - Charging: M3 (back left LED) blinks, while M2 (right back LED) is lit.
  - Boot loader mode: Blink approximately once every second.
- **M4: The front left LED (4)**

  -Radio connected: Flickers in red and/or green.
  
These LED indicators provide valuable information about the status of the Crazyflie 2.1 drone, including power, sensor calibration, battery level, charging, boot loader mode, radio connection, and self-test results.


<details>
  <summary>Crazyflie Leds Images</summary>
  <p align="center"> 
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/CrazyflieLeds.jpeg" style="width: 700px; height: 400px;">
   
  </p>
  <p align="center">Crazyflie LEDs</p>
 
</details>
</details>

#### Assembling

The assembly process of the Crazyflie 2.1 can typically be completed in under 10 minutes. However, it is crucial to take into account a few important considerations. The following dropdown includes the steps to be followed for a proper assembly of the drone.

<details>
  <summary>Assembly Instructions</summary>

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

- **Battery Connection**: Connect the battery to finalize the assembly process. It is advisable to bend the battery wires and position them underneath the PCB to ensure they are out of the way. <b>Note</b>: To recharge the battery of the Crazyflie 2.1, simply connect a micro USB cable. Ensure that the Crazyflie is turned on. During the charging process, the back left blue LED will blink. Once the LED remains fully illuminated, it indicates that the battery is fully charged.

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
</details>  

### Software setup
To control the flight of the Crazyflie, you have the option to use either a mobile device or a computer. Using a mobile device provides a quick setup, although it may require more piloting skills. On the other hand, if you prefer more options and greater control, you can utilize a computer along with a Crazyradio 2.0 or Crazyradio PA and a gamepad.

However, in the case of the team, it has been chosen a different approach. Instead of using a gamepad,  the movement of the Crazyflie is controlled by programming and executing trajectories within the Python IDE using the CFClient.

The CFClient is a software tool that serves as a graphical interface for interacting with the Crazyflie. It allows to monitor and control various aspects of the drone's flight parameters, sensor data, and behavior. Additionally, you can establish a connection between the CFClient and the Crazyflie by utilizing the Crazyradio 2.0 or Crazyradio PA for wireless communication. Check the Installation section to get information about how to install it.

Once you have everything installed and working correctly, you can connect your computer with the drone:
- **Launch the CFClient**: Open the CFClient software on your computer. This will provide you with access to various control and configuration options for the Crazyflie.

- **Establish Radio Connection**: Within the CFClient, locate the option to establish a radio connection. This process establishes a wireless link between the CFClient and the Crazyflie through the Crazyradio.

- **Select Crazyflie Device**: After establishing the radio connection, the CFClient will display a list of available Crazyflie devices. Choose the desired Crazyflie from the list to establish a connection with that specific device.

- **Configure Settings**: Once connected, you can configure various settings within the CFClient to customize the behavior and performance of the Crazyflie. These settings may include flight parameters, control mappings, and sensor calibration.

- **Monitor and Control**: With the CFClient and Crazyradio successfully connected to the Crazyflie, you can monitor real-time telemetry data, such as flight status, battery levels, and signal quality. Use the CFClient interface to control the Crazyflie's movement and perform maneuvers according to your requirements.

- **Firmware Updates**: It is crucial to keep the Crazyflie's firmware up to date to access the latest features and improvements. The CFClient provides options to update the firmware, ensuring compatibility and optimal performance.

By following these technical and formal steps, users can effectively utilize the CFClient and the Crazyradio 2.0 or Crazyradio PA to control and manage the Crazyflie's flight operations.

## Simulation Guide

After completing the installation of Webots as described in the installation section, it is time to load the world and run the simulation.
To do this, it is necessary to enter the folder ```\Simulation\webots\webots\worlds``` and load one of the two available experiments: Straight Line Test (```Prueba Linea Recta.wbt```) and Curve Test (```Prueba Curva.wbt```).
Once one of the experiments is loaded, the next step is to run the simulation to observe the results of the test.

## User Guide


To be able to use the drone's guidance codes, it is first necessary to connect it to the computer. To do this, after installing the drivers mentioned in the installation section, follow the following steps:

- **Launch the CFClient**: Open the CFClient software on your computer. This will provide you with access to various control and configuration options for the Crazyflie.

- **Establish Radio Connection**: Within the CFClient, locate the option to establish a radio connection. This process establishes a wireless link between the CFClient and the Crazyflie through the Crazyradio.

- **Select Crazyflie Device**: After establishing the radio connection, the CFClient will display a list of available Crazyflie devices. Choose the desired Crazyflie from the list to establish a connection with that specific device.

- **Configure Settings**: Once connected, you can configure various settings within the CFClient to customize the behavior and performance of the Crazyflie. These settings may include flight parameters, control mappings, and sensor calibration.

After connecting the drone to the computer, it is time to send it the programmed Python code to initiate its flight.


Firstly, it will be necessary to create the trajectory to be followed by the drone. To do this, open the file ```trajectory_planner.m``` to obtain the CSV file with the trajectory.

Then, using a programming program such as Visual Studio, execute the code ```csv_follower.py``` to send the trajectory to the drone.
Once the program execution is completed, terminate the created terminal to avoid issues in subsequent executions.

## Maintenance and Operations Manual

Next, we provide a series of tips and recommendations to follow when handling and repairing the drone and associated programs:


<details>
  <summary>Replacement of drone parts</summary>
   
  When replacing batteries, make sure that the drone is turned off and not connected to the computer to avoid potential personal injury or damage to the device. This caution is mentioned because if the drone enters installation mode, sometimes no LED lights are visible, which can give false information about its power status.

During the installation of propellers, it is necessary to exercise caution. Applying excessive force can damage the rotor, while installing with insufficient pressure may cause the propeller to detach during the initial flights.

It is recommended to replace the included rotor in the drone with a more powerful one to better align the programmed timing with the desired outcome. The following image shows the two types of rotors:
  
  
  <p align="center">
    
  <img src="https://github.com/Ingenia-SE/Hell-ix/blob/main/img/RotorBlades%26Motors.jpeg" width="640">
   
  </p>
  
  <p align="center">Left: Stock rotors. Right: More powerful rotors.</p>
    
 
</details>

<details>
  <summary>Advices</summary>
  
  When powering on the drone, it is recommended to quickly place it on a flat surface (such as the ground or a table) until you hear a short sequence of beeps during which the propellers will briefly spin. It is not recommended to hold it in your hand during this process to avoid improper calibration.

When executing the programming code, it is advisable to close any other terminals to avoid potential interference with other terminals or driver usage.  
  
 </details>

<details>
  <summary>Errors</summary>
  
  
Finally, three common errors that may arise when using this repository are mentioned:

- When using the Matlab code to create the trajectory in .csv format, an error may occur due to the default decimal separator, which can be either "," or ".". If errors occur when running the code to read the trajectory in Python, check the decimal separator in the csv file.

- If the drone is hit during flight and does not turn back on, it is likely that the battery has been displaced. To fix this, disconnect the battery cable and reconnect it. If it still does not turn on, replace the battery as it may have run out of power.

- If, when executing the flight code, the drone does not execute the code correctly or errors occur during execution, close the terminal using the "Kill terminal" or similar option (depending on the software used). Once this is done, run the code again.


  
  </details>
