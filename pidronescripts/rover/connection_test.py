##########DEPENDENCIES#############

from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
# Import required modules from dronekit library

import time
# Import time module for adding delays

import socket
# Import socket module for network communication

# import exceptions
# Commented out the import of exceptions module as it is not used in the code

import math
# Import math module for mathematical operations

import argparse
# Import argparse module for parsing command-line arguments

#########FUNCTIONS#################

def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect', help='Connection string for the vehicle')
    args = parser.parse_args()
    connection_string = args.connect
    # Parse the connection string from command-line arguments
    
    vehicle = connect(connection_string, wait_ready=True, baud=57600)
    # Connect to the vehicle using the provided connection string and baud rate
    # wait_ready=True ensures that the script waits until the vehicle is ready
    
    return vehicle
    # Return the connected vehicle object

def arm():
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable.")
        time.sleep(1)
    # Wait until the vehicle becomes armable
    
    print("Vehicle is now armable")
    
    vehicle.mode = VehicleMode("GUIDED")
    while vehicle.mode != 'GUIDED':
        print("Waiting for drone to enter GUIDED flight mode")
        time.sleep(1)
    # Set the vehicle mode to GUIDED and wait until it is in GUIDED mode
    
    print("Vehicle now in GUIDED MODE. Have fun!!")
    
    vehicle.armed = True
    while not vehicle.armed:
        print("Waiting for vehicle to become armed.")
        time.sleep(1)
    # Arm the vehicle and wait until it is armed
    
    print("Vehicle is now armed.")
    return None

##########MAIN EXECUTABLE###########

vehicle = connectMyCopter()
# Connect to the vehicle using the connectMyCopter function

vehicle.wait_ready('autopilot_version')
# Wait until the autopilot version is available

print('Autopilot version: %s' % vehicle.version)
# Print the autopilot version

arm()
# Arm the vehicle using the arm function
