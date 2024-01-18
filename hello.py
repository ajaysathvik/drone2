from dronekit import connect , VehicleMode , LocationGlobalRelative , LocationGlobal , Command
baud_rate = 57600
vehicle = connect('/dev/ttyACM0',baud=baud_rate,wait_ready=True)

print("Battery level:", vehicle.battery.level)