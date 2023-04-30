from djitellopy import tello
import cv2
import queue
import threading
import time

q=queue.Queue()

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()

time.sleep(20)

def Receive():
    cap = cv2.VideoCapture("udp://@0.0.0.0:11111")
    #ret, frame = cap.read()
    
    #q.put(frame)
    while True:
        frame = drone.get_frame_read().frame
        q.put(frame)

def Display():
    while True:
        if q.empty() != True:
            frame = q.get()
            cv2.imshow("frame", frame)

if __name__ == '__main__':
    p1 = threading.Thread(target=Receive)
    p2 = threading.Thread(target=Display)
    p1.start()
    p2.start() 

#while True:
#    img = drone.get_frame_read().frame
#    #img = cv2.resize(img, (640, 480))
#    cv2.imshow("Image", img)
#    cv2.waitKey(0)
    

