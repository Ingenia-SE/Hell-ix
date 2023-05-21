# -*- coding: utf-8 -*-
#
#  ...........       ____  _ __
#  |  ,-^-,  |      / __ )(_) /_______________ _____  ___
#  | (  O  ) |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  | / ,..´  |    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#     +.......   /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  MIT Licence
#
#  Copyright (C) 2023 Bitcraze AB
#

"""
file: pid_controller.py

A simple PID controller for the Crazyflie
ported from pid_controller.c in the c-based controller of the Crazyflie
in Webots
"""

import numpy as np


class pid_position_fixed_height_controller():
    def __init__(self):
        self.past_x_error = 0.0
        self.past_y_error = 0.0
        self.past_yaw_error = 0.0
        self.past_vx_error = 0.0
        self.past_vy_error = 0.0
        self.past_alt_error = 0.0
        self.past_pitch_error = 0.0
        self.past_roll_error = 0.0
        self.x_integrator = 0.0
        self.y_integrator = 0.0
        self.yaw_integrator = 0.0
        self.altitude_integrator = 0.0
        self.last_time = 0.0

    def pid(self, dt, desired_x, desired_y, desired_yaw, desired_altitude, actual_roll, actual_pitch, actual_yaw, actual_yaw_rate,
            actual_altitude, actual_x, actual_y, actual_vx, actual_vy):
        # Velocity PID control (converted from Crazyflie c code)
        gains = {"kp_att_y": 0.8, "kd_att_y": 0.1, "kp_att_rp": 0.5, "kd_att_rp": 0.1,
                 "kp_vel_xy": 2, "kd_vel_xy": 0.5, "kp_z": 10, "ki_z": 5, "kd_z": 5,
                 "kp_pos": 4, "kd_pos": 0.8, "ki_pos": 0.8}

        # Position PID control
        x_error = desired_x - actual_x
        x_deriv = (x_error - self.past_x_error) / dt
        y_error = desired_y - actual_y
        y_deriv = (y_error - self.past_y_error) / dt
        yaw_error = desired_yaw - actual_yaw
        yaw_deriv = (yaw_error - self.past_yaw_error) / dt
        self.x_integrator += x_error * dt
        self.y_integrator += y_error * dt
        self.yaw_integrator += yaw_error * dt
        desired_vx_local = gains["kp_pos"] * np.clip(x_error, -1, 1) + gains["kd_pos"] * x_deriv + gains["ki_pos"] * np.clip(self.x_integrator, -2, 2)
        desired_vy_local = gains["kp_pos"] * np.clip(y_error, -1, 1) + gains["kd_pos"] * y_deriv + gains["ki_pos"] * np.clip(self.y_integrator, -2, 2)
        desired_vx = desired_vx_local*np.cos(actual_yaw) + desired_vy_local*np.sin(actual_yaw)
        desired_vy = -desired_vx_local*np.sin(actual_yaw) + desired_vy_local*np.cos(actual_yaw)
        desired_yaw_rate = gains["kp_pos"] * np.clip(yaw_error, -1, 1) + gains["kd_pos"] * yaw_deriv + gains["ki_pos"] * np.clip(self.yaw_integrator, -0.1, 0.1)
        self.past_x_error = x_error
        self.past_y_error = y_error
        self.past_yaw_error = yaw_error

        # Velocity PID control
        vx_error = desired_vx - actual_vx
        vx_deriv = (vx_error - self.past_vx_error) / dt
        vy_error = desired_vy - actual_vy
        vy_deriv = (vy_error - self.past_vy_error) / dt
        desired_pitch = gains["kp_vel_xy"] * np.clip(vx_error, -1, 1) + gains["kd_vel_xy"] * vx_deriv
        desired_roll = -gains["kp_vel_xy"] * np.clip(vy_error, -1, 1) - gains["kd_vel_xy"] * vy_deriv
        self.past_vx_error = vx_error
        self.past_vy_error = vy_error

        # Altitude PID control
        alt_error = desired_altitude - actual_altitude
        alt_deriv = (alt_error - self.past_alt_error) / dt
        self.altitude_integrator += alt_error * dt
        alt_command = gains["kp_z"] * alt_error + gains["kd_z"] * alt_deriv + \
            gains["ki_z"] * np.clip(self.altitude_integrator, -2, 2) + 48
        self.past_alt_error = alt_error

        # Attitude PID control
        pitch_error = desired_pitch - actual_pitch
        pitch_deriv = (pitch_error - self.past_pitch_error) / dt
        roll_error = desired_roll - actual_roll
        roll_deriv = (roll_error - self.past_roll_error) / dt
        yaw_rate_error = desired_yaw_rate - actual_yaw_rate
        roll_command = gains["kp_att_rp"] * np.clip(roll_error, -1, 1) + gains["kd_att_rp"] * roll_deriv
        pitch_command = -gains["kp_att_rp"] * np.clip(pitch_error, -1, 1) - gains["kd_att_rp"] * pitch_deriv
        yaw_command = gains["kp_att_y"] * np.clip(yaw_rate_error, -1, 1) 
        self.past_pitch_error = pitch_error
        self.past_roll_error = roll_error

        # Motor mixing
        m1 = alt_command - roll_command + pitch_command + yaw_command
        m2 = alt_command - roll_command - pitch_command - yaw_command
        m3 = alt_command + roll_command - pitch_command + yaw_command
        m4 = alt_command + roll_command + pitch_command - yaw_command

        # Limit the motor command
        m1 = np.clip(m1, 0, 600)
        m2 = np.clip(m2, 0, 600)
        m3 = np.clip(m3, 0, 600)
        m4 = np.clip(m4, 0, 600)


        return [m1, m2, m3, m4]