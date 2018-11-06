#!/usr/bin/env python3

from vardef import *
from drive import *

map_gen()
led_ready()

while not bt.any():
	pass
led_start()
#~ Start of drive
start_configuration()
left()
while not bt.on_enter():

	drive()

	check_for_end()

start_configuration()
right()
while not bt.on_enter():

	drive()

	check_for_end()


# #~ End of program


led_end()
