from dronekit import connect , VehicleMode , LocationGlobalRelative , LocationGlobal , Command
import matplotlib.pyplot as plt
import time
import cv2
import eel
import logging

logging.basicConfig(filename='logile.log',format='%(asctime)s - %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

vehicle = connect('127.0.0.1:14550', wait_ready=True)

def arm():
    while vehicle.is_armable == False:
       print("Waiting")
       time.sleep(1)
    vehicle.armed = True

    while vehicle.armed == False:
        print("Waiting to become armed")

    print("vehicle is now armed")

def video():
    cap = cv2.VideoCapture(0) 
    if not cap.isOpened():
        print("Error opening video capture")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if frame is captured successfully
        if not ret:
            print("Error capturing frame")
            break

        # Process the frame (e.g., display, perform computer vision tasks)
        # ...
        cv2.imshow('Video Feed', frame)

        # Wait for key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

@eel.expose
def version_major():
    return vehicle.version.major

@eel.expose
def version_minor():
    return vehicle.version.minor

def check_version_2():
    if vehicle.version.is_stable:
        print ("upgrade the drone version to 3 or higher")

@eel.expose
def check_battery():
    battery = vehicle.battery.level
    return battery

@eel.expose
def check_altitude():
    altitude = vehicle.location.global_relative_frame.alt
    return altitude

@eel.expose
def check_roll():
    roll = vehicle.attitude.roll
    return roll
     

def check_pitch():
    pitch = vehicle.attitude.pitch
    
    
def check_velocity():

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
    print (vehicle.airspeed)

def check_groundspeed():
    print (vehicle.groundspeed)

@eel.expose
def check_mode():
    vehicle_mode = vehicle.mode.name
    return vehicle_mode
            
def check_is_armable():
    return vehicle.is_armable

@eel.expose
def check_armed():
    return vehicle.armed

@eel.expose
def check_temperature():
    temperature = vehicle.battery.level
    return temperature

@eel.expose
def check_status():
    return vehicle.system_status.state   

def check_parameters():
    print (vehicle.parameters['THR_MIN'])

def check_gps():
    print (vehicle.gps_0)

def check_last_heartbeat():
    print (vehicle.last_heartbeat)

def check_home_location():
    print (vehicle.home_location)

@eel.expose
def mission_check():
    cmds = vehicle.commands
    return cmds.count

@eel.expose
def compass_calibration():
    return vehicle.capabilities.compass_calibration

@eel.expose
def set_mode(mode):
    vehicle.mode = VehicleMode(mode)
    
@eel.expose
def set_status(status):
    vehicle.system_status.state = status  
     
@eel.expose
def set_mission(lat,lon,alt):
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
    return vehicle.location.global_relative_frame.lat

@eel.expose
def check_location_lon():
    return vehicle.location.global_relative_frame.lon

@eel.expose
def check_location_alt():
    return vehicle.location.global_relative_frame.alt

@eel.expose
def make_guided():
    vehicle.mode = VehicleMode("GUIDED")
    
@eel.expose
def compass():
    return vehicle.heading
    
@eel.expose
def make_arm():
    vehicle.armed = True

@eel.expose
def ground_speed():
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
eel.init("web")
eel.start('index.html', size=(2400,1080))
