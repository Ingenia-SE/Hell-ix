import logging
import time
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper
import csv

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
            cf.commander.send_hover_setpoint(0, 0, 0, y*3 / 100)
            time.sleep(0.05)

        for _ in range(20):
            cf.commander.send_hover_setpoint(0, 0, 0, 1.5)
            time.sleep(0.1)

        for _ in range(50):
            cf.commander.send_hover_setpoint(y*3/100, 0, 0, 1.5)
            time.sleep(0.1)

        for _ in range(20):
            cf.commander.send_hover_setpoint(1.5, 0, 0, 1.5)
            time.sleep(0.1)

        for y in range(50):
            cf.commander.send_hover_setpoint(1.5, 0, 0, (50 - y)*3 / 100)
            time.sleep(0.05)

        cf.commander.send_stop_setpoint()
