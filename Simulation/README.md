# Hell - IX Simulation

These folders contain all the files necessary for the execution of the different tests that make up the drone competition.

## Installation
It is necessary to have the WEBOTS simulation program installed. If you do not have this program installed, it can be obtained through the following link: [Webots](https://cyberbotics.com/)


## Usage
Once you have the program, you have to open the following folder where both test simulations are located: ```.\webots\webots\worlds```.
When you have loaded the world, the next step is to run the simulation to see the results of each of the tests.


## Parts of the simulation
To realize the controller that manages the crazyflie in the simulation, the following process has been carried out: 

1. Search for specific documentation to know the libraries that should be added to the project to be able to perform a simple flight.

2. Once this first flight was successfully completed, the process of simulating a trajectory was started. To do this, first of all a function called ``PID_CF`` was implemented, where through the target position, the function regulates the power to be supplied to each of the drone motors. This function is a PID controller where each of the constants of the controller had to be adjusted.

3. Once the controller was working correctly, the next step was to read a csv file detailing each and every one of the points where the drone had to reach to perform the trajectory of each of the tests. To do this, the .csv file was read with the ``csv`` library of pyhton, where all these data are stored in a system matrix. Each of the rows determines a point that the drone must be able to reach, so a loop was implemented that did not change the reference position until it had not reached that position taking into account an assumable error.

4. Once the drone was able to follow trajectories, the design of the test scenarios began. To do this, each of the obstacles was first designed in 3D using CAD tools. Once designed, the obstacles were placed in the positions agreed with the opposing team. 




## License
Hell - Ix (Universidad Politécnica de Madrid)
