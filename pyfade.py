import socket
import time
import math

start_value = -37000
end_value = 1
time_interval = 5
time_step = 0.01

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("your_server_ip", your_port_number))

start_time = time.time()

while start_value <= end_value:
    time_elapsed = time.time() - start_time
    current_value = start_value + (end_value - start_value) * (1 - math.exp(-time_elapsed / time_interval))
    
    command = f"set MIXER:Current/InCh/Fader/On 0 0 {current_value}\n"
    s.sendall(command.encode())
    
    time.sleep(time_step)

s.close()