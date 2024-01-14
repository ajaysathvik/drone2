# from tkinter import *
# from dronekit import connect , VehicleMode , LocationGlobalRelative , LocationGlobal
import eel
# vehicle = connect('tcp:127.0.0.1:5762')

eel.init('/home/unknown/Documents/drone-project/drone-project/web')
eel.start('index.html', size=(2400,1080))