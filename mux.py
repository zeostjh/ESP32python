
from hcsr04 import HCSR04
import time
import machine
import socket

host ="10.8.1.195"#host
port =49280

sensor = HCSR04(trigger_pin=16, echo_pin=0)

while True:
  distance = sensor.distance_cm()
  if distance <= 30:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.sendall("set MIXER:Current/InCh/Fader/On 0 0 0\n".encode())
    s.sendall("set MIXER:Current/InCh/Fader/Level 3 0 0\n".encode())
    s.recv(1500)
    s.close ()
    else:
      print(
      


   print("sent")


    
