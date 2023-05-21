# Tests
In this folder the python scripts used to test the drone for performing simple tasks are included. Two tests have been included: one for simple take-off, maintaining the position and landing, and the second one to follow a straight line.

## Description of the Tests
### 1. Take-off and Landing Test
This test is contained in script ```up_and_down.py```. In this test the drone must climb 1.5 metres above the ground, hold the position for 2 seconds and land. To do this, a series of "for" loops have been used that establish setpoints at which the drone must stay for a certain time.

### 2. Move Forward Test
This test is contained in script ```move_forward.py```. In this test the drone must rise 1.5 metres above the ground, hold the position for 2 seconds and move in a straight line in the direction of the x-axis for 1.5 metres. It must then land. For this, a series of "for" loops have been used where a series of setpoints are defined in which the drone must stay for a certain amount of time.
