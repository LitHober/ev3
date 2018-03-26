#!/usr/bin/env python3

from ev3dev.ev3 import *

#Sensores y motores
cl = ColorSensor('in3')
ir = InfraredSensor('in2') 
motorIzq = LargeMotor('outB')
motorDer = LargeMotor('outC')

#Modos
cl.mode = 'COL-COLOR'
ir.mode = 'IR-PROX'

#Variables
btn = Button()

motorIzq.run_forever(speed_sp=200)
motorDer.run_forever(speed_sp=200)

while not btn.any():

    if ir.value() < 20:
        motorIzq.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake")  
        motorDer.run_to_rel_pos(position_sp=-500, speed_sp=200, stop_action="brake") 


motorIzq.stop(stop_action='brake')
motorDer.stop(stop_action='brake')