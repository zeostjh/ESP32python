
from simpleOSC import initOSCClient, sendOSCMsg, closeOSC
from hcsr04 import HCSR04
from machine import Pin, PWM
import time
import sleep
import machine
import socket
import Pin
initOSCClient()
host ="10.8.1.95"#host
port =49280
Rled=PWM(Pin(4), 5000)
Gled=PWM(Pin(5), 5000)
Bled=PWM(Pin(15), 5000)
Oled=PWM(Pin(2), 5000)
sensor = HCSR04(trigger_pin=12, echo_pin=13)
esp32_001 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
esp32_001.connect((host,port))https://github.com/zeostjh/ESP32python/blob/main/mux.py
while True:
  distance = sensor.distance_cm()
  if distance <= 20:
    sendOSCMsg("/3333333", [444])
    esp32_001.sendall("set MIXER:Current/InCh/Fader/On 0 0 0\n".encode())
    esp32_001.sendall("set MIXER:Current/InCh/Fader/Level 0 0 500\n".encode())
    esp32_001.recv(1500)
    esp32_001.close ()
    print("Sent")
    time.sleep(0.5)
    for R_dutyCycle in range(0, 1024):
      Rled.duty(R_dutyCycle)
      print(R_dutyCycle)
    elif distance <= 40:
      sendOSCMsg("/2222222", [444])
      esp32_001.sendall("set MIXER:Current/InCh/Fader/On 0 0 0\n".encode())
      esp32_001.sendall("set MIXER:Current/InCh/Fader/Level 0 0 0\n".encode())
      esp32_001.recv(1500)
      esp32_001.close ()
      print("Sent")
      time.sleep(0.5)
      for G_dutyCycle in range(0, 1024):
        Rled.duty(G_dutyCycle)
        print(G_dutyCycle)
      elif distance <= 60:
        sendOSCMsg("/1111111", [444])
        esp32_001.sendall("set MIXER:Current/InCh/Fader/On 0 0 0\n".encode())
        esp32_001.sendall("set MIXER:Current/InCh/Fader/Level 0 0 -2000\n".encode())
        esp32_001.recv(1500)
        esp32_001.close ()
        print("Sent")
        time.sleep(0.5)
        for B_dutyCycle in range(0, 1024):
          Rled.duty(B_dutyCycle)
          print(B_dutyCycle)
        time.sleep(0.5)
 closeOSC()     

      
      
      
#from simpleOSC import initOSCClient, initOSCServer, setOSCHandler, sendOSCMsg, closeOSC, \
#createOSCBundle, sendOSCBundle, startOSCServer
#initOSCClient()
#while True:
#    sendOSCMsg("/test", [444])

                                                             # create and send a bundle
            # bundle = createOSCBundle("/test/bndlprt1")
            # bundle.append(666)                             # 1st message appent to bundle
            # bundle.append("the number of the beast")       # 2nd message appent to bundle
            # sendOSCBundle(bundle)                          # !! it sends by default to localhost ip "127.0.0.1" and port 9000
            # closeOSC() # finally close the connection before exiting or program.
            
            # if __name__ == '__main__': myTest()
 
#for R_dutyCycle in range(0, 1024):
#for G_dutyCycle in range(0, 1024):
#for B_dutyCycle in range(0, 1024):
#for O_dutyCycle in range(0, 1024): 
#Rled.duty(R_dutyCycle)
#Gled.duty(G_dutyCycle)
#Bled.duty(B_dutyCycle)
#Oled.duty(O_dutyCycle)
#print(R_dutyCycle)
#print(G_dutyCycle)
#print(B_dutyCycle)
#print(O_dutyCycle)
  
