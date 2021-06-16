
from hcsr04 import HCSR04
import time
import machine
import socket
import Pin

host ="10.8.1.95"#host
port =49280
rled=Pin(4,Pin.OUT)
gled=Pin(5,Pin.OUT)
bled=Pin(15,Pin.OUT)
sensor = HCSR04(trigger_pin=12, echo_pin=13)
esp32_001 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
esp32_001.connect((host,port))
while True:
  distance = sensor.distance_cm()
  if distance <= 30:
    rled.value(0)
    gled.value(1)
    bled.value(0)
    esp32_001.sendall("set MIXER:Current/InCh/Fader/On 0 0 1\n".encode())
    esp32_001.sendall("set MIXER:Current/InCh/Fader/Level 0 0 -1000\n".encode())
    esp32_001.recv(1500)
    esp32_001.close ()
    print("Sent")
    time.sleep(0.5)
    else:
      print("OUT DISTANCE:", distance, 'cm')
      rled.value(1)
      gled.value(0)
      bled.value(0)

