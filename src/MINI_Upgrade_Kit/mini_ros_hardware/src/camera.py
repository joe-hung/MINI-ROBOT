#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np
import time

class Camera:
    def __inti__(self):
        
        rospy.init_node('camera', anonymous=True)
        
        self.img_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=1)
        self.rate = rospy.Rate(10) # 10hz

        self.cap = cv2.VideoCapture(1)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
        
        self.bridge = CvBridge()

    def update(self):
        #start time 
        _, frame = self.cap.read()
        msg_img = self.bridge.cv2_to_imgmsg(frame, encoding="passthrough")
        self.img_pub(msg_img)

def ros_loop(node):
    try:
        while not rospy.is_shutdown():
            node.update()
            node.rate.sleep()
    except KeyboardInterrupt:
        pass
    except rospy.ROSInterruptException:
        pass
if __name__ == '__main__':
    ros_loop(Camera())