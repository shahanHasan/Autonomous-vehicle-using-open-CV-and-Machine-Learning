from tkinter import *
import driveFunctions.py
from driveFunctions import Drive
import numpy as np
import cv2 as cv
# constructor of tkinter
# it is a blank window
root = Tk()
root.geometry('680x600')
root.title("Data Collector")
root.configure(background="#383a39")

drive = Drive()

def forward(event):
    drive.Forward()

def backward(event):
    drive.Backward()

def stop(event):
    drive.Stop()

def driveleft(event):
    drive.MoveLightLeft()

def driveright(event):
    drive.MoveLightRight()

def driveleftspin(event):
    drive.SpinLeft()

def driverightspin(event):
    drive.SpinRight()

def drivehardleft(event):
    drive.MoveHardLeft()

def drivehardright(event):
    drive.MoveHardRight()

def vdo():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        return frame

topframe = Frame(root)
topframe.pack(fill='both',expand='1')
bottomframe = Frame(root)
bottomframe.pack(fill='both',expand='1')


photo = PhotoImage(file=vdo())
label = Label(root, image = photo)
label.pack()

forward = Button(topframe , text="forward", fg="red")
forward.bind("<Button-1>",forward)
forward.pack(side=TOP)

backward = Button(topframe , text="backward", fg="blue")
backward.bind("<Button-1>",backward)
backward.pack(side=BOTTOM)

stop = Button(topframe , text="stop", fg="red")
stop.bind("<Button-1>",stop)
stop.pack(side=BOTTOM)

lefts = Button(topframe , text="driveleft", fg="blue")
lefts.bind("<Button-1>",driveleft)
lefts.pack(side=LEFT)

rights = Button(topframe , text="driveright", fg="red")
rights.bind("<Button-1>",driveright)
rights.pack(side=RIGHT)

spinl = Button(topframe , text="driveleftspin", fg="blue")
spinl.bind("<Button-1>",driveleftspin)
spinl.pack(side=LEFT)

spinr = Button(bottomframe , text="driverightspin", fg="red")
spinr.bind("<Button-1>",driverightspin)
spinr.pack(side=RIGHT)

hardl = Button(bottomframe , text="drivehardleft", fg="blue")
hardl.bind("<Button-1>",drivehardleft)
hardl.pack(side=LEFT)

hardr = Button(bottomframe , text="drivehardright", fg="red")
hardr.bind("<Button-1>",drivehardright)
hardr.pack(side=RIGHT)

root.mainloop()
