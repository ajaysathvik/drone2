import sys
from cx_Freeze import setup, Executable

# Include all necessary packages
build_exe_options = {"packages": [ "dronekit", "matplotlib.pyplot", "numpy",
                                  "mpl_toolkits.mplot3d", "progress.bar", "time", "pymavlink", "cv2", "eel",
                                  "os", "sys","bottle_websocket"]}

# Include additional modules or data files if needed (e.g., include_files=["data_file.txt"])

# Define the executable
setup(
    name="My Drone App",
    version="1.0",
    description="An app for controlling a drone and visualizing data",
    options={"build_exe": build_exe_options},
    executables=[Executable("drone.py")]
)

