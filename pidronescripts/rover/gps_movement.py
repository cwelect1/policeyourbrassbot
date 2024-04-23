##########DEPENDENCIES#############

from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
# Import necessary modules from the dronekit library

import time
# Import the time module for adding delays

import socket
# Import the socket module for network communication

# import exceptions
# Commented out the import of exceptions module as it is not used in the code

import math
# Import the math module for mathematical calculations

import argparse
# Import the argparse module for parsing command-line arguments

#########FUNCTIONS#################

def connectRoberto():
    # Function to connect to the vehicle (drone) using command-line arguments
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
    # Function to arm the vehicle and set it to GUIDED mode
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

def get_distance_meters(targetLocation, currentLocation):
    # Function to calculate the distance in meters between two locations
    dLat = targetLocation.lat - currentLocation.lat
    dLon = targetLocation.lon - currentLocation.lon
    return math.sqrt((dLon * dLon) + (dLat * dLat)) * 1.113195e5
    # Calculate the distance using the Haversine formula

def goto(targetLocation):
    # Function to make the vehicle go to a specified target location
    distanceToTargetLocation = get_distance_meters(targetLocation, vehicle.location.global_relative_frame)
    # Calculate the initial distance to the target location
    
    vehicle.simple_goto(targetLocation)
    # Command the vehicle to go to the target location
    
    while vehicle.mode.name == "GUIDED":
        currentDistance = get_distance_meters(targetLocation, vehicle.location.global_relative_frame)
        if currentDistance < distanceToTargetLocation * 0.05:
            print("Reached target waypoint.")
            time.sleep(2)
            break
        time.sleep(1)
    # Continuously monitor the distance to the target location
    # Break the loop when the vehicle reaches within 5% of the initial distance
    
    return None

##########MAIN EXECUTABLE###########

wp1 = LocationGlobalRelative(36.00550, -95.86124, 10)
wp2 = LocationGlobalRelative(36.00607, -95.86107, 10)
wp3 = LocationGlobalRelative(36.00604, -95.86037, 10)
# Define the waypoint locations

vehicle = connectRoberto()
# Connect to the vehicle using the connectRoberto function

vehicle.parameters['WP_SPEED'] = 2
# Set the vehicle's waypoint speed parameter to 2 m/s

arm()
# Arm the vehicle and set it to GUIDED mode

goto(wp1)
goto(wp2)
goto(wp3)
# Command the vehicle to go to each waypoint sequentially

vehicle.mode = VehicleMode("RTL")
while vehicle.mode != 'RTL':
    print("Waiting for drone to enter RTL flight mode")
    time.sleep(1)
# Set the vehicle mode to RTL (Return to Launch) and wait until it is in RTL mode

print("Vehicle now in RTL mode. Driving home.")
# Print a message indicating that the vehicle is returning to the launch location
