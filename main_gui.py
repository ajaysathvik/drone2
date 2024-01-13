import eel
import drone
<<<<<<< HEAD

@eel.expose
def get_battery ():
    return  drone.check_battery()
=======
from time import sleep
>>>>>>> parent of e6a2bc0 (.)

eel.init('web')
eel.start('index.html', size=(2400,1080))

<<<<<<< HEAD
=======
root = Tk()
root.title("C Drone")

# root.resizable(False, False)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

canvas = Canvas(root, width=width, height=height,bg="#E3E8EB")
canvas.pack()

# create a rounded cornered rectangle
#rounded_rectangle(canvas, left , top, right, bottom, radius=25, fill="#D9D9D9")

rounded_rectangle(canvas, width*0.007, height*0.01, width*0.115, height*0.063, radius=50, fill="#FFFFFF") # top left
rounded_rectangle(canvas, width*0.007, height*0.077, width*0.115, height*0.5, radius=50, fill="#F3F7F9") # bottom left
rounded_rectangle(canvas, width*0.847, height*0.01, width*0.995, height*0.93, radius=50, fill="#F3F7F9") # rightmost
rounded_rectangle(canvas, width*0.122, height*0.01, width*0.4978, height*0.063, radius=50, fill="#FFFFFF") # top middle
rounded_rectangle(canvas, width*0.504 , height*0.01, width*0.84, height*0.063, radius=50, fill="#FFFFFF") # top right
rounded_rectangle(canvas, width*0.122, height*0.077, width*0.84, height*0.545, radius=50, fill="#D9D9D9") # middle 
rounded_rectangle(canvas, width*0.122, height*0.555, width*0.84, height*0.93, radius=50, fill="#D9D9D9") # bottom middle

canvas.create_text(
    175,
    55,
    anchor="nw",
    text="AerroGrow",
    fill="#000000",
    font=("Inter", 30 * -1)
)

batteryimg = Image.open("gui/build/assets/frame0/Battery.png").convert("RGBA")
battery1 = batteryimg.resize((424,280)).rotate(180)
battery3 = ImageTk.PhotoImage(battery1)
canvas.create_image(width*0.487, height*-0.024, anchor=NW, image=battery3)

temp_img = Image.open("gui/build/assets/frame0/temp.png").convert("RGBA")
temp_img1 = temp_img.resize((119 ,119))
temp_img2 = ImageTk.PhotoImage(temp_img1)
canvas.create_image(width*0.64, height*0.01, anchor=NW, image=temp_img2)

alt_img = Image.open("gui/build/assets/frame0/alt.png").convert("RGBA")
alt_img1 = alt_img.resize((119 ,119))
alt_img2 = ImageTk.PhotoImage(alt_img1)
canvas.create_image(width*0.75, height*0.01, anchor=NW, image=alt_img2)

droneimg = Image.open("gui/build/assets/frame0/camera-drone.png").convert("RGBA")
droneimg1 = droneimg.resize((128,128))
droneimg2 = ImageTk.PhotoImage(droneimg1)
canvas.create_image(width*0.135,height*0.009,anchor=NW,image=droneimg2)
canvas.create_image(width*0.25,height*0.009,anchor=NW,image=droneimg2)

def battery_check():
    battery_percentage = drone.check_battery()

    canvas.delete("battery_text")

    canvas.create_text(
        width * 0.576,   # x-coordinate
        height * 0.036,  # y-coordinate
        anchor="center",  # text alignment
        text=f"{battery_percentage}%",  # text
        fill="#000000",  # text color
        font=("Calibri", 17, "normal"),  # font and size
        tags="battery_text"  # add a tag to easily delete this text later
    )

    root.after(100, battery_check)

battery_check()

def temp_check():
    temp_percentage = drone.temp_check()

    canvas.delete("temp_text")

    canvas.create_text(
        width*0.676,  # x-coordinate
        height*0.036,  # y-coordinate
        anchor="center",  # text alignment
        text=f"{temp_percentage}",  # text
        fill="#000000",  # text color
        font=("Calibri", 17, "normal"),  # font and size
        tags="temp_text"  # add a tag to easily delete this text later
    )

    root.after(100, temp_check)

temp_check()

def alt_check():
    alt = drone.check_altitude()
    
    canvas.delete("alt_text")
    
    canvas.create_text(
        width*0.79,
        height*0.037,
        anchor="center",
        text=f"{alt}",
        fill="#000000",
        font=("Calibri", 17, "normal"),
        tags="alt_text"
    )
    
    root.after(100,alt_check)
    
alt_check()

canvas.create_text(
    width*0.192,
    height*0.026,
    anchor="center",
    fill="#919191",
    text="Arm Status",
    font=("Calibri", 10, "normal"),
    tags="arm_status_text"
)

def status_check():
    status= drone.check_armed()
    
    canvas.delete("status_text")
    
    print (status)
    
    if status == True:
        canvas.create_text(
        width*0.187,
        height*0.044,
        anchor="center",
        fill="#000000",
        text="Armed",
        font=("Calibri", 12, "normal"),
        tags="status_text"
    )
    else:
        canvas.create_text(
        width*0.192,
        height*0.044,
        anchor="center",
        fill="#000000",
        text="Disarmed",
        font=("Calibri", 12, "normal"),
        tags="status_text"
    )    

status_check()

canvas.create_text(
    width*0.297,
    height*0.026,
    anchor="center",
    fill="#919191",
    text="Mode",
    font=("Calibri", 10, "normal"),
    tags="arm_mode_text"
)

def mode_check():
    mode = drone.check_mode()
    
    canvas.delete("mode_text")
    
    canvas.create_text(
        width*0.304,
        height*0.044,
        anchor="center",
        fill="#000000",
        text=f"{mode}",
        font=("Calibri", 12, "normal"),
        tags="mode_text"
    )
    
    root.after(100,mode_check)

mode_check()
    
root.mainloop()
>>>>>>> parent of e6a2bc0 (.)
