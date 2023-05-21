import logging
import time
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper
import csv
import numpy as np
import cv2
import math

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')


# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf

        cf.param.set_value('kalman.resetEstimation', '1')
        time.sleep(0.1)
        cf.param.set_value('kalman.resetEstimation', '0')
        time.sleep(2)

        for y in range(50):
            cf.commander.send_hover_setpoint(0, 0, 0, y / 100)
            time.sleep(0.05)

        for _ in range(20):
            cf.commander.send_hover_setpoint(0, 0, 0, 0.5)
            time.sleep(0.1)

        csv_file_path = "C:/Users/Usuario/Desktop/VUELO CRAZYFLIE/trajectory.csv"
        csv_reader = csv.reader(open(csv_file_path, 'r'))
        for row in csv_reader:
            x, y, z = float(row[0]), float(row[1]), float(row[2])
            if row == 0:
                angle = 0
            else:
                angle = -np.arctan((y-y0)/(x-x0)) * 180 / math.pi
            cf.commander.send_position_setpoint(y, -x, z, angle)
            time.sleep(0.02)
            x0, y0 = x, y

        for y in range(50):
            cf.commander.send_hover_setpoint(0, 0, 0, (50 - y) / 100)
            time.sleep(0.05)

        cf.commander.send_stop_setpoint()


