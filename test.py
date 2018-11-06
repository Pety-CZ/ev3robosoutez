import ev3dev.ev3 as ev3
from ev3dev.ev3 import TouchSensor
from ev3dev.ev3 import ColorSensor

COL_VALUE = 50
SPEED = 500
FW = 560
BACK = -140
TURN = 400
# map = [[],[],[]]


A = ev3.LargeMotor('outA')
B = ev3.LargeMotor('outB')
C = ev3.Motor('outC')


#~ us = UltrasonicSensor()
#~ us.mode='US-DIST-CM'		# Put the US sensor into distance mode.
cl = ColorSensor()
cl.mode='COL-REFLECT'
# bt = Button()
two = 2
COL_VALUE = 50
ts = TouchSensor()

def motor_wait():
	A.wait_while('running')
	B.wait_while('running')


def colision():
    if ts.value():
        if cl.value() <= COL_VALUE:
            crash()
            left()
        else:
            crash()
            right()
            fwd()
            if ts.value():
                crash()
                right()
                for x in range(two):
                    fwd()
                if ts.value():
                    if cl.value() <= COL_VALUE:
                        crash()
                        left()
                    else:
                        crash()
                    for y in range(two):
                        right()
                        fwd()

def crash():
	A.run_to_rel_pos(position_sp=BACK, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=BACK, speed_sp=SPEED, stop_action="brake")
	motor_wait()

def fwd():
	A.run_to_rel_pos(position_sp=FW, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=FW, speed_sp=SPEED, stop_action="brake")
	motor_wait()

def back():
	A.run_to_rel_pos(position_sp=-FW, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=-FW, speed_sp=SPEED, stop_action="brake")
	motor_wait()

def right():
	A.run_to_rel_pos(position_sp=TURN, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=-TURN, speed_sp=SPEED, stop_action="brake")
	motor_wait()

def left():
	A.run_to_rel_pos(position_sp=TURN, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=-TURN, speed_sp=SPEED, stop_action="brake")
	motor_wait()


while True:
    fwd()
    colision()
