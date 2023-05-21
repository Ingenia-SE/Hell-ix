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
            cf.commander.send_hover_setpoint(0, 0, 0, y / 100)
            time.sleep(0.05)

        for _ in range(20):
            cf.commander.send_hover_setpoint(0, 0, 0, 0.5)
            time.sleep(0.1)

        #C�digo de la trayectoria de la espiral
        for n in range(5):                         #N�mero de vueltas de la espiral
            for angle in range(90):      #Angulo cada 4 grados
               x = (angle-45) * 4 / 360             #Avance 1m por 360 grados
               y = 0 + cmath.cos((angle-45)*4) * 0.5    #Circulo de 1m de diametro
               z = 1.5 + cmath.sin((angle-45)*4) * 0.5  #Altura entre 1 y 2 metros
               time.sleep(0.02)

        #C�digo aterrizaje
        for y in range(50):
            cf.commander.send_hover_setpoint(0, 0, 0, (50 - y)*3 / 100)
            time.sleep(0.05)

        cf.commander.send_stop_setpoint()




