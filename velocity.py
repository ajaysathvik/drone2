import dronekit_sitl
from dronekit import connect , VehicleMode , LocationGlobalRelative , LocationGlobal , Command
from dronekit.mavlink import MAVConnection 
import matplotlib.pyplot as plt
import folium
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from progress.bar import IncrementalBar
import time
from pymavlink import mavutil
import threading
import cv2
vehicle = connect('tcp:127.0.0.1:5762')

while True:
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
    time.sleep(1)