from time import sleep
from hc_sr04 import HC_SR04
from servo import Servo
import numpy as np
import matplotlib.pyplot as plt
import random
from operator import itemgetter 

sensor = HC_SR04()
servo = Servo()

mapa = []

for i in range(0, 180):
    servo.angle = i
    servo.set_angle()
    dst = sensor.get_distance()
    medida = {'angle': i*np.pi/180, 'distance': dst}
    mapa.append(medida)

theta = list(map(itemgetter('angle'), mapa))
theta = [x-np.pi/2 for x in theta]
distance = list(map(itemgetter('distance'), mapa))

ax = plt.subplot(111, projection='polar')
ax.plot(theta, distance)
ax.set_rmax(300)
ax.set_rlabel_position(0)
ax.grid(True)
ax.set_thetamin(-90)
ax.set_thetamax(90)

plt.show()