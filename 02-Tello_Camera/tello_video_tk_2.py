import tkinter as tk
from djitellopy import tello
from threading import Thread
import imutils
from PIL import Image, ImageTk
import time
import cv2

#display camera feed window with tkinter. this is taken from scribbles.net showing video with tkinter.
class Window():
    def __init__(self, window, cap):
        self.window = window
        self.cap = cap
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.interval = 20

        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0)

        self.update_image()

    def update_image(self):
        self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # convert image format
        self.image = Image.fromarray(self.image) #to PIL format
        self.image = ImageTk.PhotoImage(self.image) #to ImageTk format

        self.canvas.create_image(0,0,anchor=tk.NW, image=self.image) #update image

        self.window.after(self.interval, self.update_image)

    def videoRecorder(self, frame_read):
        height, width, _ = frame_read.frame.shape
        video = cv2.VideoWriter('vid.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

        while True:
            video.write(frame_read.frame)
            time.sleep(1/30)

if __name__ == "__main__":
    root = tk.Tk()

    drone = tello.Tello()
    drone.connect()
    print(drone.get_battery())

    drone.streamoff()
    drone.streamon()


    cam = drone.get_frame_read().frame

    #time.sleep(5)
    
    #height, width, _ = cam.frame.shape

    #video = cv2.VideoWriter('vid.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
    #while True:
    #        video.write(frame_read.frame)
    #        time.sleep(1/30)

    #cam = cv2.resize(cam, (640, 480))


    time.sleep(3)
    cam = cv2.VideoCapture('udp://@0.0.0.0:11111') #tello video address

    #time.sleep(3)

    #win = Window(root) 

    #win.videoRecorder(cam)
    Window(root, cam)
    root.mainloop()