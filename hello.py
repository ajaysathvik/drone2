from dronekit import connect , VehicleMode , LocationGlobalRelative , LocationGlobal , Command 
import time
from pymavlink import mavutil
import dronekit as dronekit
baud_rate = 57600
vehicle = connect('/dev/ttyACM0',baud=baud_rate,wait_ready=True)
vehicle.armed = True
