import socket
import time

host ="10.8.1.195"#host
port =49280

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))


# turn channel 1 off
s.sendall("set MIXER:Current/InCh/Fader/On 0 0 0\n".encode())

# turn channel 2 off
s.sendall("set MIXER:Current/InCh/Fader/On 1 0 0\n".encode())

# set channel 3 fader to 0
s.sendall("set MIXER:Current/InCh/Fader/Level 2 0 0\n".encode())

# set channel 4 fader to 0
s.sendall("set MIXER:Current/InCh/Fader/Level 3 0 0\n".encode())

# set channel 5 fader to +5
s.sendall("set MIXER:Current/InCh/Fader/Level 4 0 500\n".encode())

# set channel 6 fader to -10
s.sendall("set MIXER:Current/InCh/Fader/Level 5 0 -1000\n".encode())

print("sent")

s.recv(1500)

s.close ()
