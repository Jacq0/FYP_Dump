import serial
import time 

#setup the port for the microbit
port = serial.Serial('COM11', 115200)
takeInput = True
routine2 = False

#numbering is handled on microbit transmitter
while takeInput == True:
    print("Enter Command for Tello (Formatted like DRONE-NUMBER|COMMAND, Replace number with A for all)")
    
    entered = input("> ") + '\r'

    port.write(bytes(entered, 'utf-8'))
    
    if entered == "exit\r":
        port.close()
        break

if takeInput == False and routine2 == False:
    time.sleep(2)
    port.write(b'A|command\r')
    time.sleep(2)
    port.write(b'A|takeoff\r')
    time.sleep(5)
    port.write(b'A|flip f\r')
    time.sleep(10)
    port.write(b'A|land\r')
    time.sleep(2)
    port.close()

if routine2:
    time.sleep(2)
    port.write(b'0|command\r')
    time.sleep(0.5)
    port.write(b'1|command\r')
    time.sleep(2)
    port.write(b'0|takeoff\r')
    time.sleep(0.5)
    port.write(b'1|takeoff\r')
    time.sleep(2)
    port.write(b'0|cw 90\r')
    time.sleep(0.5)
    port.write(b'1|cw 90\r')
    time.sleep(10)
    port.write(b'0|land\r')
    time.sleep(0.5)
    port.write(b'1|land\r')
    time.sleep(2)
    port.close()