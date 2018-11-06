from vardef import *


def drive():
    while not ts.value():
        fwdF()
        if cl.value < COL_VALUE:
            check_left()
            break
    col()

# def AI():
#     if map[][][] == map[X][Y][True]:
#         goThere()

        ## TODO: DO some AI for antonomous driving from list


def check_left():
    if cl.value() < COL_VALUE:
        left()
        fwd()
        right()
        right()
        fwd()
        left()

# def check_direction():
# 	if(DIRECTION = -3):
# 		DIRECTION = 1
# 		X = X + 1
# 	elif(DIRECTION = 2):
# 		DIRECTION = -2
# 		Y = Y - 1
# 	elif(DIRECTION = 0):
# 		Y = Y + 1
# 	elif(DIRECTION = -1):
# 		X = X - 1

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

def fwd():
	DIRECTION = 0
	A.run_to_rel_pos(position_sp=FW, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=FW, speed_sp=SPEED, stop_action="brake")
	motor_wait()
    check_drive()

def back():
	DIRECTION = -2
	A.run_to_rel_pos(position_sp=-FW, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=-FW, speed_sp=SPEED, stop_action="brake")
	motor_wait()
    check_drive()

def right():
	DIRECTION = DIRECTION + 1
	A.run_to_rel_pos(position_sp=TURN, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=-TURN, speed_sp=SPEED, stop_action="brake")
	motor_wait()
    check_drive()

def left():
	DIRECTION = DIRECTION - 1
	A.run_to_rel_pos(position_sp=TURN, speed_sp=SPEED, stop_action="brake")
	B.run_to_rel_pos(position_sp=-TURN, speed_sp=SPEED, stop_action="brake")
	motor_wait()
    check_drive()


def check_drive():
	mapping()
	check_direction()
