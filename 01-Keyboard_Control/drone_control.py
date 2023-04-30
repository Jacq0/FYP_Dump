import keyboardIn as k
import djitellopy as tello

k.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())


def getKBIn():
    lr, fb, ud, yv = 0,0,0,0 #values for each of the directions
    speed = 50

    if k.getKey("w"): 
        fb = speed
    if k.getKey("s"): 
        fb = -speed

    if k.getKey("a"): 
        lr = -speed
    if k.getKey("d"): 
        lr = speed

    if k.getKey("q"): 
        yv = speed
    if k.getKey("e"): 
        yv = -speed

    if k.getKey("SPACE"):
        ud = speed
    if k.getKey("LCTRL"):
        ud = -speed

    return [lr, fb, ud, yv]

while True:
    if(k.getKey("t")):
        drone.takeoff()

    if(k.getKey("l")):
        drone.land()

    vals = getKBIn()
    drone.send_rc_control(vals[0],vals[1],vals[2],vals[3])