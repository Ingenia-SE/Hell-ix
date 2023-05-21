import cv2
import numpy as np

ref = 0
centrox = centroz = 0

imagen = cv2.imread("ingenia/puerta8.jpg")

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

cv2.imshow("gauss",gauss)
cv2.imshow("1",mask1)
cv2.imshow("2",mask2)
cv2.imshow("negra",img_negra)
cv2.imshow("puertas1",puertas)

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

# cv2.imshow("imgnegra",img_negra)
cv2.imshow("puertas",imagen)
# cv2.imshow("mask1",mask1)

# ########## corrección de posición ##########
# K1 =
# K2 =
# Area1m =

# dist = np.sqrt(Area1m/ref)

# errorz = K1 * dist * (324/2 - centroz)
# errorangulo = np.arctan((324/2-centrox) * K2 / dist)



cv2.waitKey(0)