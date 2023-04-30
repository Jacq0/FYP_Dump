from djitellopy import Tello
from tkinter import  *
from PIL import ImageTk, Image
import cv2

#init values fot tkinter
w, h = 800, 600

win = null
lmain = null

def __init__():
    win = Tk()
    win.geometry("800x600")
    win.title("Tello Video Feed")

    frame = Frame(win)
    frame.grid(row=1, column=0)

    lmain = Label(win)
    lmain.grid()

tello = Tello()

tello.connect()

print(tello.get_battery())

tello.streamon()

cap = cv2.VideoCapture(tello.get_udp_video_address())
    
def video_stream():
    #frame_read = tello.get_frame_read().frame
    _, frame = cap.read()
    #img = cv2.resize(frame_read, w,h)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    #img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(cv2image)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)


video_stream()
win.mainloop()

#def showCameraFeed():
#    imgtk = ImageTk.fromarray()