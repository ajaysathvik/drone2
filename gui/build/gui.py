from tkinter import *

root = Tk()

text_label = Label(root, text="Counting...")
text_label.pack()

count = 0
def update_counter():
    global count
    count += 1
    text_label.config(text=f"Count: {count}")
    root.after(1000, update_counter)  # Call after 1 second

update_counter()

root.mainloop()