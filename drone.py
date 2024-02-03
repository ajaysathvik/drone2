from dronekit import connect , VehicleMode , LocationGlobalRelative , LocationGlobal , Command
import matplotlib.pyplot as plt
import time
import cv2
import eel

baud_rate = 57600
# vehicle = connect('127.0.0.1:5762')
# vehicle = connect('0.0.0.0:14551',wait_ready=True , baud=baud_rate)

# drone_ip = "127.0.0.1"  # Replace with your drone's IP address
# drone_port = 14560


# # Connect to the drone using MAVLink over UDP
# vehicle = connect(f"udp:{drone_ip}:{drone_port}", wait_ready=True)

global vehicle 
# vehicle = connect("/dev/ttyUSB0", baud=baud_rate)

@eel.expose
def connect_vehicle():
    global vehicle
    vehicle = connect('/dev/ttyUSB0' ,baud = baud_rate)
    # vehicle = connect('127.0.0.1:14550', wait_ready=True, baud=baud_rate)
    
def arm():
    global vehicle
    while vehicle.is_armable == False:
       time.sleep(1)
    vehicle.armed = True

@eel.expose
def version_major():
    global vehicle
    return vehicle.version.major


@eel.expose
def version_minor():
    global vehicle
    return vehicle.version.minor

# def check_version_2():
#     global vehicle
#     if vehicle.version.is_stable:

@eel.expose
def check_battery():
    global vehicle
    vehicle.wait_ready('battery')
    battery = vehicle.battery.level
    return battery

@eel.expose
def check_altitude():
    global vehicle
    altitude = vehicle.location.global_relative_frame.alt
    return altitude

@eel.expose
def check_roll():
    global vehicle
    roll = vehicle.attitude.roll
    return roll
     
@eel.expose
def check_pitch():
    global  vehicle
    pitch = vehicle.attitude.pitch
    return pitch
    
    
def check_velocity():
    global vehicle
    northward_velocity = vehicle.velocity[0]
    eastward_velocity = vehicle.velocity[1]
    upward_velocity = vehicle.velocity[2]


    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot origin
    ax.plot([0], [0], [0], 'o', markersize=10, color='black')

    # Plot velocity components as lines
    ax.plot([0, eastward_velocity], [0, 0], [0, 0], color='red', linewidth=2)
    ax.plot([0, 0], [0, northward_velocity], [0, 0], color='green', linewidth=2)
    ax.plot([0, 0], [0, 0], [0, upward_velocity], color='blue', linewidth=2)

    # Add annotations for each velocity component
    ax.text(eastward_velocity, 0, 0, f'{eastward_velocity:.2f}', fontsize=12, color='red')
    ax.text(0, northward_velocity, 0, f'{northward_velocity:.2f}', fontsize=12, color='green')
    ax.text(0, 0, upward_velocity, f'{upward_velocity:.2f}', fontsize=12, color='blue')

    # Set labels and title
    ax.set_xlabel('Eastward Velocity')
    ax.set_ylabel('Northward Velocity')
    ax.set_zlabel('Upward Velocity')
    ax.set_title('Drone Velocity in 3D')

    # Show plot
    plt.savefig("velocity.png")

def check_airspeed():
    global vehicle
    print (vehicle.airspeed)

def check_groundspeed():
    global vehicle
    print (vehicle.groundspeed)

@eel.expose
def check_mode():
    global  vehicle
    vehicle_mode = vehicle.mode.name
    return vehicle_mode
            
def check_is_armable():
    global vehicle
    return vehicle.is_armable

@eel.expose
def check_armed():
    global vehicle
    return vehicle.armed

@eel.expose
def check_status():
    global vehicle
    return vehicle.system_status.state   

def check_parameters():
    global vehicle
    print (vehicle.parameters['THR_MIN'])

def check_gps():
    global vehicle
    print (vehicle.gps_0)

def check_last_heartbeat():
    global vehicle
    print (vehicle.last_heartbeat)

def check_home_location():
    global vehicle
    print (vehicle.home_location)

@eel.expose
def mission_check():
    global vehicle
    cmds = vehicle.commands
    return cmds.count

@eel.expose
def compass_calibration():
    global vehicle
    return vehicle.capabilities.compass_calibration

@eel.expose
def set_mode(mode):
    global vehicle
    vehicle.mode = VehicleMode(mode)
    
@eel.expose
def set_status(status):
    global vehicle
    vehicle.system_status.state = status  
     
@eel.expose
def set_mission(lat,lon,alt):
    global vehicle
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    vehicle.simple_takeoff(alt)
    while True:
        if vehicle.location.global_relative_frame.alt >= int(alt)-1:
            break
        time.sleep(1)
    vehicle.simple_goto(LocationGlobalRelative(lat, lon, alt))  

@eel.expose
def check_location_lat():
    global vehicle
    return vehicle.location.global_relative_frame.lat

@eel.expose
def check_location_lon():
    global vehicle
    return vehicle.location.global_relative_frame.lon

@eel.expose
def check_location_alt():
    global vehicle
    return vehicle.location.global_relative_frame.alt

@eel.expose
def make_guided():
    global vehicle
    vehicle.mode = VehicleMode("GUIDED")
    
@eel.expose
def compass():
    global vehicle
    return vehicle.heading
    
@eel.expose
def make_arm():
    global vehicle
    vehicle.armed = True

@eel.expose
def ground_speed():
    global vehicle
    return vehicle.groundspeed

# def get_path(path):
#     if getattr(sys, 'frozen', False):
#         print (os.path.join(sys.executable, os.path.relpath(os.path.join(sys.argv[0], path))))
#         return os.path.join(sys.executable, os.path.relpath(os.path.join(sys.argv[0], path)))
#     else:
#         print(os.path.join(os.path.dirname(__file__), path))
#         return os.path.join(os.path.dirname(__file__), path)
    
# def get_path(relative):
#     return os.path.join(
#         os.environ.get(
#             "_MEIPASS2",
#             os.path.abspath(".")
#         ),
#         relative
#     )   

# def get_path(relative_path):
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)
 
# def get_path(path: str) -> str:
#     if getattr(sys, 'frozen', False):
#         return os.path.join(sys.executable, os.path.relpath(os.path.join(sys.argv[0], path)))
#     else:
#         return os.path.abspath(path)
 
    
# eel.init(path=get_path("web")) 

# def print_info():
#     global vehicle
#     print(vehicle.battery)
#     print("Roll: %s Pitch %s Yaw %s" % (vehicle.attitude.roll, vehicle.attitude.pitch, vehicle.attitude.yaw))
#     print("Velocity: %s" % vehicle.velocity)
#     print("Airspeed: %s" % vehicle.airspeed)
#     print("Groundspeed: %s" % vehicle.groundspeed)
#     print("Mode: %s" % vehicle.mode.name)
#     print("Armed: %s" % vehicle.armed)
#     print("Status: %s" % vehicle.system_status.state)
#     print("Vehicle Heading: %s" % vehicle.heading)
#     print("Location: %s" % vehicle.location.global_relative_frame)
#     print("latitude: %s longitude: %s altitude: %s" % (vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon, vehicle.location.global_relative_frame.alt))

# @eel.expose
# def print_info():
#     global vehicle
#     print(vehicle.battery)
#     print("Roll: %s Pitch %s Yaw %s" % (vehicle.attitude.roll, vehicle.attitude.pitch, vehicle.attitude.yaw))
#     print("Velocity: %s" % vehicle.velocity)
#     print("Airspeed: %s" % vehicle.airspeed)
#     print("Groundspeed: %s" % vehicle.groundspeed)
#     print("Mode: %s" % vehicle.mode.name)
#     print("Armed: %s" % vehicle.armed)
#     print("Status: %s" % vehicle.system_status.state)
#     print("Vehicle Heading: %s" % vehicle.heading)
#     print("Location: %s" % vehicle.location.global_relative_frame)
#     print("latitude: %s longitude: %s altitude: %s" % (vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon, vehicle.location.global_relative_frame.alt))

@eel.expose
def calibrate_sensors():
    global vehicle
    vehicle.send_calibrate_accelerometer()
    vehicle.send_calibrate_gyro()
    vehicle.send_calibrate_barometer()
    vehicle.send_calibrate_vehicle_level()

    
eel.init("web")
eel.start('index.html', size=(2400,1080))
