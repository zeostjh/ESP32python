import socket
import time

host ="10.8.1.195"#host
port =49280

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))

s.sendall("set MIXER:Current/InCh/Fader/On 0 0 0\n".encode())

s.sendall("set MIXER:Current/InCh/Fader/Level 3 0 0\n".encode())

s.sendall("set MIXER:Current/InCh/Fader/Level 4 0 500\n".encode())

s.sendall("set MIXER:Current/InCh/Fader/Level 5 0 -1000\n".encode())

print("sent")

s.recv(1500)

s.close ()
