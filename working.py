import machine
import hcsr04
import time
import network
from umqtt.simple import MQTTClient


ultrasonic = hcsr04.HCSR04(trigger_pin=12, echo_pin=13, echo_timeout_us=500000)
localled = machine.Pin(2, machine.Pin.OUT)#revese
r = machine.Pin(15, machine.Pin.OUT)
g = machine.Pin(4, machine.Pin.OUT)
b = machine.Pin(5, machine.Pin.OUT)

SERVER = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client", SERVER)
CHANNEL_ID = "1418567"
WRITE_API_KEY = "HBMQ14EA93E4VWR5"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY
UPDATE_TIME_INTERVAL = 5000
last_update = time.ticks_ms()

t = 1
h = 2

while True:
    time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '|', distance/2.54, 'inch')
    payload = "field1={}" .format(str(distance))
    client.connect()
    client.publish(topic, payload)
    client.disconnect()
    last_update = time.ticks_ms()
    if distance <= 10:
        localled.on()
        r.off()
        g.on()
        b.on()
        time.sleep(0.1)
    elif distance <= 20:
        localled.off()
        r.on()
        g.on()
        b.on()
        time.sleep(0.1)
    elif distance <= 25:
        localled.on()
        r.on()
        g.off()
        b.on()
        time.sleep(0.02)
        localled.off()
        r.on()
        g.on()
        b.on()
        time.sleep(0.02)
    elif distance <= 30:
        localled.on()
        r.on()
        g.off()
        b.on()
        time.sleep(0.03)
        localled.off()
        r.on()
        g.on()
        b.on()
        time.sleep(0.03)
    elif distance <= 40:
        localled.off()
        r.on()
        g.on()
        b.off()
        
        time.sleep(0.1)
    elif distance > 41:
        localled.off()
        r.on()
        g.on()
        b.on()
        time.sleep(0.1)
        
    
    
    

