
from hcsr04 import HCSR04
import time
import machine

sensor = HCSR04(trigger_pin=16, echo_pin=0)

while True:
  distance = sensor.distance_cm()
  print('Distance:', distance, 'cm')
  if distance <= 30:
    
