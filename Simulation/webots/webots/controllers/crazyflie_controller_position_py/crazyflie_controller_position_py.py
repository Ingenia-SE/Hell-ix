#  ...........       ____  _ __
#  |  ,-^-,  |      / __ )(_) /_______________ _____  ___
#  | (  O  ) |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  | / ,..´  |    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#     +.......   /_____/_/\__/\___/_/   \__,_/ /___/\___/

# MIT License

# Copyright (c) 2022 Bitcraze

# @file crazyflie_controllers_py.py
# Controls the crazyflie motors in webots in Python

"""crazyflie_controller_py controller."""


from controller import Robot
from controller import Motor
from controller import InertialUnit
from controller import GPS
from controller import Gyro
from controller import Keyboard
from controller import Camera
from controller import DistanceSensor

from math import cos, sin
import csv
import time
import numpy as np
import sys
sys.path.append('../../../controllers/python_based')
from pid_controller_position import pid_position_fixed_height_controller


csv_file_path = "C:/Users/PCWIN10/Desktop/webots/webots/controllers/crazyflie_controller_position_py/Semicirculo3M.csv"
#csv_reader = csv.reader(open(csv_file_path, 'r'))
#row=next(csv_reader)
matriz_datos=[]
#row = row[0].split(";")
#forward_diff_desired, sideways_diff_desired, height_diff_desired, yaw_diff_desired = float(row[2]), float(row[3]), float(row[4]), float(row[5])
      
with open(csv_file_path,'r') as archivo_csv:
    lector=csv.reader(archivo_csv,delimiter=';')
    for fila in lector:
        matriz_datos.append(fila)
                    
x_ini = float(matriz_datos[0][0])
y_ini = float(matriz_datos[0][1])
z_ini = float(matriz_datos[0][2])  
angle_ini = float(matriz_datos[0][3])
n_filas=len(matriz_datos) 
print(n_filas)
print(y_ini)
print(z_ini)
print(angle_ini)


#x_ini, y_ini, z_ini, angle_ini = float(row[2]), float(row[3]), float(row[4]), float(row[5])
if __name__ == '__main__':

    robot = Robot()
    timestep = int(robot.getBasicTimeStep())

    ## Initialize motors
    m1_motor = robot.getDevice("m1_motor");
    m1_motor.setPosition(float('inf'))
    m1_motor.setVelocity(-1)
    m2_motor = robot.getDevice("m2_motor");
    m2_motor.setPosition(float('inf'))
    m2_motor.setVelocity(1)
    m3_motor = robot.getDevice("m3_motor");
    m3_motor.setPosition(float('inf'))
    m3_motor.setVelocity(-1)
    m4_motor = robot.getDevice("m4_motor");
    m4_motor.setPosition(float('inf'))
    m4_motor.setVelocity(1)

    ## Initialize Sensors
    imu = robot.getDevice("inertial_unit")
    imu.enable(timestep)
    gps = robot.getDevice("gps")
    gps.enable(timestep)
    gyro = robot.getDevice("gyro")
    gyro.enable(timestep)
    camera = robot.getDevice("camera")
    camera.enable(timestep)
    range_front = robot.getDevice("range_front")
    range_front.enable(timestep)
    range_left = robot.getDevice("range_left")
    range_left.enable(timestep)
    range_back = robot.getDevice("range_back")
    range_back.enable(timestep)
    range_right = robot.getDevice("range_right")
    range_right.enable(timestep)

    ## Get keyboard
    keyboard = Keyboard()
    keyboard.enable(timestep)

    ## Initialize variables

    past_x_global = 0
    past_y_global = 0
    past_time = robot.getTime()

    # Crazyflie position PID controller
    PID_CF = pid_position_fixed_height_controller()
    PID_update_last_time = robot.getTime()
    sensor_read_last_time = robot.getTime()

    print("\n");

    print("====== Controls =======\n\n");

    print(" The Crazyflie can be controlled from your keyboard!\n");
    print(" All controllable movement is in body coordinates\n");
    print("- Use the up, back, right and left button to move in the horizontal plane\n");
    print("- Use Q and E to rotate around yaw ");
    print("- Use W and S to go up and down\n ")
    error_pos=0.08
    error_altura=0.04
    # Main loop:
    turns_counter = 0
    yaw_estimate = 0.0
    desired_state = [x_ini, y_ini,z_ini, angle_ini]  # x, y, z, yaw, set to above the initial drone pos in the apartment
    i=0
    while robot.step(timestep) != -1:
        #print((matriz_datos[i]))
        dt = robot.getTime() - past_time
        actual_state = {}
        ## Get sensor data
        roll = imu.getRollPitchYaw()[0]
        pitch = imu.getRollPitchYaw()[1]
        yaw = imu.getRollPitchYaw()[2]
        yaw_rate = gyro.getValues()[2]
        altitude = gps.getValues()[2]
        x_global = gps.getValues()[0]
        v_x_global = (x_global - past_x_global)/dt
        y_global = gps.getValues()[1]
        v_y_global = (y_global - past_y_global)/dt
        
        if error_pos>abs(x_global-desired_state[0]) and error_pos>abs(y_global-desired_state[1]) and error_altura>abs(altitude-desired_state[2]):
            print(desired_state)
            i=i+1
           
        ## Get body fixed velocities
        cosyaw = cos(yaw)
        sinyaw = sin(yaw)
        v_x = v_x_global * cosyaw + v_y_global * sinyaw
        v_y = - v_x_global * sinyaw + v_y_global * cosyaw

        ## Initialize values
        forward_diff_desired = 0
        sideways_diff_desired = 0
        yaw_diff_desired = 0
        height_diff_desired = 0

        cameraData = camera.getImage()
                
        yaw_estimate += yaw_rate * dt
        
        if i<n_filas:
            desired_state[0]=float(matriz_datos[i][0])
            desired_state[1]=float(matriz_datos[i][1])
            desired_state[2]=float(matriz_datos[i][2])
            desired_state[3]=float(matriz_datos[i][3])
        
        if desired_state[3] < (np.pi*0.9) and yaw_estimate < (np.pi*0.9) and desired_state[3] > (-np.pi*0.9) and  yaw_estimate > (-np.pi*0.9):
            yaw_estimate = yaw
        
        ## Example how to get sensor data
        ## range_front_value = range_front.getValue();
        # print(desired_state, yaw, yaw_estimate, yaw - yaw_estimate)


        ## PID position controller with fixed height
        motor_power = PID_CF.pid(dt, desired_state[0], desired_state[1],
                                desired_state[3], desired_state[2],
                                roll, pitch, yaw_estimate, yaw_rate,
                                altitude, x_global, y_global, v_x, v_y)
                               
        
        m1_motor.setVelocity(-motor_power[0])
        m2_motor.setVelocity(motor_power[1])
        m3_motor.setVelocity(-motor_power[2])
        m4_motor.setVelocity(motor_power[3])

        past_time = robot.getTime()
        past_x_global = x_global
        past_y_global = y_global
       





