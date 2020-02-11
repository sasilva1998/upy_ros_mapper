#!/usr/bin/env python
import rospy
import socket
from move_commands.msg import LaserScan
import time
def callback(data):
	rospy.loginfo(list(data.ranges)[179])
	data=list(data.ranges)
	if data[179]<1:
		rospy.loginfo('izquierda')
		sock.sendall('1')
	else:
		rospy.loginfo('adelante')
		sock.sendall('0')
	time.sleep(1.5)
def listener():
	global sock 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('192.168.43.86', 88)
	sock.connect(server_address)
	rospy.init_node('scan', anonymous=True)
	rospy.Subscriber("scan", LaserScan, callback,queue_size=1)
	rospy.spin()

if __name__ == '__main__':
	listener()
