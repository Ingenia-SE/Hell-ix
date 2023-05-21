# Freestyle Test
In this section we will describe a series of programmes created to compete in the freestyle event. In this part of the competition, each team has the freedom to fly the drone in such a way that its trajectory draws figures in the air.

## Program Files
### 1. **freestyle_star.py**
In this program, a series of setpoints are defined through which the drone must pass.

These points describe a trajectory in the shape of a vertical five-pointed star. That is why the modified position parameters are the "y" and "z", since the drone will be located in the x = 0 plane at the moment.

In addition, the drone has been programmed in such a way that when it reaches a vertex it will make one turn about the z-axis. To do this, the value of the yaw is modified in a series of setpoints.


### 2. **freestyle_spiral.py**

By executing this programme, the drone draws a spiral in the air.

To draw this spiral, a superposition of movements is carried out. On the one hand, a circle with a diameter of one metre is made in the y, z plane while the value of x is varied linearly, so that it moves forward by one metre for each circle made.

All these points are transmitted to the drone in the form of setpoints through which it must pass in a given time.
