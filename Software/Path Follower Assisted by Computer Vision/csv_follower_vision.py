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

errorz = errorangulo = 0

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

def ojodron():
    ref = 0
    centrox = centroz = 324/2

    capture = cv2.VideoCapture(0)
    isTrue, imagen = capture.read()

    h,w,c = imagen.shape
    img_negra = 0 * np.ones(shape=(h, w), dtype=np.uint8)

    #imagen = cv2.imread("prueba-python/fotos/cono.jpg")
    gauss = cv2.GaussianBlur(imagen,(5,5),15)

    hsv = cv2.cvtColor(gauss,cv2.COLOR_RGB2HSV)

    # Define range of orange color in HSV
    lower_orange = np.array([95, 50, 50])
    upper_orange = np.array([115, 255, 255])

    # Define range of white color in HSV
    lower_white = np.array([0, 0, 180])
    upper_white = np.array([180, 50, 255])

    mask1 = cv2.inRange(hsv, lower_orange, upper_orange)
    mask2= cv2.inRange(hsv, lower_white, upper_white)

    contornos, hier = cv2.findContours(mask2, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img_negra,contornos,-1,(255,255,255),-1)

    puertas = img_negra & mask1

    cont, hier = cv2.findContours(puertas, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for i in cont:
        if cv2.contourArea(i) > ref:
            ref = cv2.contourArea(i)
            M = cv2.moments(i)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cz = int(M['m01']/M['m00'])

    if (len(cont) > 0) & (ref > 400):
        cv2.drawContours(imagen, cont, -1, (0, 255, 0), 2)
        cv2.circle(imagen, (cx, cz), 7, (0, 0, 255), -1)
        cv2.putText(imagen, "center", (cx - 20, cz - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        ref = 0
        centrox = cx
        centroz = cz    
        print("x:",centrox,"y:",centroz)
    else:
        centrox = 324/2
        centroz = 324/2

    # K1 =
    # K2 =
    # Area1m =

    # dist = np.sqrt(Area1m/ref)

    # errorz = K1 * dist * (324/2 - centroz)
    # errorangulo = np.arctan((324/2-centrox) * K2 / dist)

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
            x, y, z, yaw = float(row[0]), float(row[1]), float(row[2]), float(row[3])
            ojodron()
            cf.commander.send_position_setpoint(y, -x, z - errorz, yaw - errorangulo)
            time.sleep(0.02)
            x0, y0 = x, y

        for y in range(50):
            cf.commander.send_hover_setpoint(0, 0, 0, (50 - y) / 100)
            time.sleep(0.05)

        cf.commander.send_stop_setpoint()



