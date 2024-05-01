##########DEPENDENCIES#############
import time
import os
import platform
import sys
import socket
import exceptions
import math
import argparse
from dronekit import connect, VehicleMode,LocationGlobalRelative,APIException
#####

vehicle = connect('/dev/tty/AMA0', baud =57600, wait_ready = True)
print(str(vehicle.system_status.state))
#### Functions
def arm():
	while vehicle.is_armable!=True:
		print("Waiting for vehicle to become armable.")
		time.sleep(1)
	print("Vehicle is now armable")

	vehicle.mode = VehicleMode("GUIDED")

	while vehicle.mode!='GUIDED':
		print("Waiting for drone to enter GUIDED flight mode")
		time.sleep(1)
	print("Vehicle now in GUIDED MODE. Have fun!!")

	vehicle.armed = True
	while vehicle.armed==False:
		print("Waiting for vehicle to become armed.")
		time.sleep(1)
	print("Vehicle is now armed.")

	return None
