import usocket as socket
import network
import utime
from arlorobot import *

bot=ArloRobot()


wifi=network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('SoccerRobot','esp12345678')

utime.sleep(3)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',88))

sock.listen(10)
print('escuchando')
while True:
    connection, client_address = sock.accept()

    try:
        while True:
        
            data = connection.recv(4096)
            if data != b'':
                data=int(data.decode('utf-8'))
                print(data)
            
            if data==0:
                bot.move(10,10,30)
            elif data==1:
                bot.turn(10,30)
        
    finally:
        connection.close()