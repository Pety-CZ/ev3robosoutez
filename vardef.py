from ev3dev.auto import *
import ev3dev.ev3 as ev3
from ev3dev.ev3 import TouchSensor
from ev3dev.ev3 import ColorSensor

COL_VALUE = 50
SPEED = 250
FW = 560
BACK = -140
TURN = 242
 map = []


A = ev3.LargeMotor('outA')
B = ev3.LargeMotor('outB')
C = ev3.Motor('outC')
ts = TouchSensor()
#~ us = UltrasonicSensor()
#~ us.mode='US-DIST-CM'		# Put the US sensor into distance mode.
cl = ColorSensor()
cl.mode='COL-REFLECT'
bt = Button()

#~ gy = GyroSensor()
#~ gy.mode='GYRO-ANG'			# Put the gyro sensor into ANGLE mode.

def led_ready():
	Leds.all_off()

def led_start():
	Leds.set_color(Leds.LEFT,  Leds.GREEN)
	Leds.set_color(Leds.RIGHT, Leds.GREEN)

def led_end():
	Leds.set_color(Leds.LEFT,  Leds.ORANGE)
	Leds.set_color(Leds.RIGHT, Leds.ORANGE)

def motor_wait():
	A.wait_while('running')
	B.wait_while('running')

def start_configuration():
	DIRECTION = 0
	X = 4
	Y = 3
	fwd()
	fwd()
	back()

def fwdF():
	DIRECTION = 0
	A.run_to_rel_pos(position_sp=FW, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=FW, speed_sp=SPEED, stop_action="brake")
	motor_wait()
	check_driveFull()

def backF():
	DIRECTION = -2
	A.run_to_rel_pos(position_sp=-FW, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=-FW, speed_sp=SPEED, stop_action="brake")
	motor_wait()
	check_driveFull()

def rightF():
	DIRECTION = DIRECTION + 1
	A.run_to_rel_pos(position_sp=TURN, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=-TURN, speed_sp=SPEED, stop_action="brake")
	motor_wait()
	check_driveFull()

def leftF():
	DIRECTION = DIRECTION - 1
	A.run_to_rel_pos(position_sp=TURN, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=-TURN, speed_sp=SPEED, stop_action="brake")
	motor_wait()
	check_driveFull()

def crash():
	A.run_to_rel_pos(position_sp=BACK, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=BACK, speed_sp=SPEED, stop_action="brake")
	motor_wait()

def check_driveFull():
	mapping()
	check_direction()
	colision()

# def map_gen():
# 	for i in X:
# 		for j in Y:
# 			map[][][] = map[I][J][False]
#
# 	# # TODO: WRITE DEFINITION OF STARTING BLCOK
#
# # 	map.append((3, 3, False))
# # 	map.append((4, 3, False))
# # 	map.append((5, 3, False))
# #
# def mapping():
# 	if(cl.value < COL_VALUE):
# 		if(DIRECTION = 0):
# 			if X is 0:
# 				map.append((X, Y, True))
# 			else:
# 				map.append((X - 1, Y, True))
# 		elif(DIRECTION = -2):
# 			if X is 8:
# 				map.append((X, Y, True))
# 			else:
# 				map.append((X + 1, Y, True))
# 		elif(DIRECTION = 1):
# 			if Y is 5:
# 				map.append((X, Y, True))
# 			else:
# 				map.append((X, Y + 1, True))
# 		elif(DIRECTION = -1):
# 			if Y is 5:
# 				map.append((X, Y, True))
# 			else:
# 				map.append((X, Y - 1, True))
#
# 	elif ts.value():
# 		if(DIRECTION = 0):
# 			if Y not 0:
# 				map.append((X, Y - 1, False))
# 		elif(DIRECTION = -2):
# 			if Y not 5:
# 				map.append((X, Y + 1, False))
# 		elif(DIRECTION = 1):
# 			if X not 8:
# 				map.append((X + 1, Y, False))
# 		elif(DIRECTION = -1):
# 			if X not 0:
# 				map.append((X - 1, Y, False))
# 	else:
# 		map.append((X, Y, True))

def check_for_end():
	if  bt.on_backspase():
		led_end()
		raise SystemExit
