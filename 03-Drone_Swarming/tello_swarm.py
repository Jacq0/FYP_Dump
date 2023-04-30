from djitellopy import TelloSwarm
from time import sleep

ips = ["192.168.1.63", "192.168.1.64"]

swarm = TelloSwarm.fromIps(ips)

swarm.connect()

drones = []

for drone in swarm:
    drones.append(drone)

    drone.takeoff()

    sleep(1)

    drone.land()

drones[0].takeoff
drones[1].takeoff

sleep(2)

drones[0].land
drones[1].land