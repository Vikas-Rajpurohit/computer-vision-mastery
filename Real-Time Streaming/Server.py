# First quit the Client.py then Server.py 

import cv2
import socket
import pickle
import os
import numpy as np

## Server Setup

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = '127.0.0.1'
port = 6666
s.bind((ip,port))

while True:
    x =s.recvfrom(1000000)
    clientip = x[1][0]
    data = x[0]
    
    data = pickle.loads(data)

    img = cv2.imdecode(data, cv2.IMREAD_COLOR)

    cv2.imshow('Image Server', img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cv2.destroyAllWindows()