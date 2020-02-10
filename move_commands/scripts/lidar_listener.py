#!/usr/bin/env python
import rospy
from move_commands.msg import LaserScan
def callback(data):
	rospy.loginfo(list(data.ranges)[179])
	data=list(data.ranges)
	if data[179]<1:
		rospy.loginfo('izquierda')
		#enviar giro a la izquierda
	else:
		rospy.loginfo('adelante')
		#enviar hacia delante

def listener():
	rospy.init_node('scan', anonymous=True)
	rospy.Subscriber("scan", LaserScan, callback)
	rospy.spin()
if __name__ == '__main__':
	listener()
