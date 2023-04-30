from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.takeoff()
drone.send_rc_control(0, 60, 0, 0)
sleep(1)
drone.land()