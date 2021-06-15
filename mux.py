
from hcsr04 import HCSR04
import time
import machine
import socket
import Pin

host ="10.8.1.195"#host
port =49280
Gled=Pin(14,Pin.OUT)
Rled=Pin(15,Pin.OUT)
sensor = HCSR04(trigger_pin=12, echo_pin=13)

while True:
  distance = sensor.distance_cm()
  if distance <= 30:
    Gled.value(1)
    Rled.value(0)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.sendall("set MIXER:Current/InCh/Fader/On 0 0 1\n".encode())
    s.sendall("set MIXER:Current/InCh/Fader/Level 0 0 -1000\n".encode())
    s.recv(1500)
    s.close ()
    print("Sent")
    time.sleep(5)
    else:
      print("OUT DISTANCE:", distance, 'cm')
      Gled.value(0)
      Rled.value(1)

