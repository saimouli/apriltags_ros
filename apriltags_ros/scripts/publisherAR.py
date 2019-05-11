#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
from _AprilTagDetectionArray import AprilTagDetectionArray 

class ARClass:
	def __init__(self):
		self.pubPose = rospy.Publisher('arPose',Pose,queue_size=1)
		self.mySub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray, self.callbackclassImage, queue_size=1)

	def callbackclassImage(self, data):		
		for i in data.detections:
			poseData = Pose()
			poseData = i.pose.pose
			newZ = float(i.id)
			poseData.position.z = newZ
			self.pubPose.publish(poseData)



if __name__ == '__main__':
    rospy.init_node('imageARSubscriber', anonymous=True)
    myClass = ARClass()
    rospy.spin()
