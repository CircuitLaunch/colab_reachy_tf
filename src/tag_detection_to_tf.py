#!/usr/bin/env python3
import sys
import tf
from apriltag_ros.msg import AprilTagDetectionArray
import rospy

def tf_handle(msgs):

    for msg in msgs.detections:
        msg.pose.header.frame_id = "april_tag" + str(msg.id[0])
        rospy.loginfo(msg)
        
        br = tf.TransformBroadcaster()
        br.sendTransform((msg.pose.pose.pose.position.x,
                          msg.pose.pose.pose.position.y,
                          msg.pose.pose.pose.position.z),
                         (msg.pose.pose.pose.orientation.x,
                          msg.pose.pose.pose.orientation.y,
                          msg.pose.pose.pose.orientation.z,
                          msg.pose.pose.pose.orientation.w),
                          rospy.Time.now(),
                          msg.pose.header.frame_id,
                          "camera")
    
if __name__ == "__main__":  
    try:
        rospy.init_node('tf_listener')
        rospy.Subscriber('/tag_detections',AprilTagDetectionArray,tf_handle)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
