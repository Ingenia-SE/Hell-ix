import cmath
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

        #C�digo despegue y establizaci�n

        for y in range(50):
            cf.commander.send_hover_setpoint(0, 0, 0, y*5 / 100)
            time.sleep(0.05)

        for _ in range(20):
            cf.commander.send_hover_setpoint(0, 0, 0, 2.5)
            time.sleep(0.1)


            #Realizaci�n de la estrella

        for giro0 in range (20):
            cf.commander.send_position_setpoint(0, 0, 2.5, giro0 * 18)
            time.sleep(0.05)

        for n1 in range (20):
            x = 0
            y = 0 + (cmath.cos(-54) - 0) * n1/10
            z = 1.5 + 1 + (cmath.sin(-54) - 1) * n1/10
            cf.commander.send_position_setpoint(x, y, z, 0)
            time.sleep(0.02)

        for giro0 in range (20):
            cf.commander.send_position_setpoint(x, y, z, giro0 * 18)
            time.sleep(0.05)

        for n2 in range (20):
            x = 0
            y = cmath.cos(-54) + (cmath.cos(162) - cmath.cos(-54)) * n2/10
            z = 1.5 + cmath.sin(-54) + (cmath.sin(162) - cmath.sin(-54)) * n2/10
            cf.commander.send_position_setpoint(x, y, z, 0)
            time.sleep(0.02)

        for giro0 in range (20):
            cf.commander.send_position_setpoint(x, y, z, giro0 * 18)
            time.sleep(0.05)
       
        for n3 in range (20):
            x = 0
            y = cmath.cos(162) + (cmath.cos(18) - cmath.cos(162)) * n3/10
            z = 1.5 + cmath.sin(162) + (cmath.sin(18) - cmath.sin(162)) * n3/10
            cf.commander.send_position_setpoint(x, y, z, 0)
            time.sleep(0.02)
      
        for giro0 in range (20):
            cf.commander.send_position_setpoint(x, y, z, giro0 * 18)
            time.sleep(0.05)
       
        for n4 in range (20):
            x = 0
            y = cmath.cos(18) + (cmath.cos(-126) - cmath.cos(18)) * n4/10
            z = 1.5 + cmath.sin(18) + (cmath.sin(-126) - cmath.sin(18)) * n4/10
            cf.commander.send_position_setpoint(x, y, z, 0)
            time.sleep(0.02)
       
        for giro0 in range (20):
            cf.commander.send_position_setpoint(x, y, z, giro0 * 18)
            time.sleep(0.05)
      
        for n5 in range (20):
            x = 0
            y = cmath.cos(-126) + (cmath.cos(90) - cmath.cos(-126)) * n5/10
            z = 1.5 + cmath.sin(-126) + (cmath.sin(90) - cmath.sin(-126)) * n5/10
            cf.commander.send_position_setpoint(x, y, z, 0)
            time.sleep(0.02)
      
        for giro0 in range (20):
            cf.commander.send_position_setpoint(x, y, z, giro0 * 18)
            time.sleep(0.05)


        #C�digo aterrizaje
        for y in range(50):
            cf.commander.send_hover_setpoint(0, 0, 0, (50 - y)*5 / 100)
            time.sleep(0.05)

        cf.commander.send_stop_setpoint()



# Hay que incluir esta parte en el resto del c�digo
