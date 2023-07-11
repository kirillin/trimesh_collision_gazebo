#!/usr/bin/env python3

import random
import sys

import rospy

from gazebo_msgs.srv import SpawnModel, SpawnModelRequest
from geometry_msgs.msg import Pose, Point, Quaternion


def main(args=None):
    rospy.init_node('test_trimesh')
    
    qty_trimeshes = 2
    if len(sys.argv) > 1:
        qty_trimeshes = int(sys.argv[1])

    model_sdf_path = rospy.get_param('model_sdf_path')

    rospy.wait_for_service('gazebo/spawn_sdf_model')
    spawn_srv = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
  
    i = 0
    while i < qty_trimeshes:
        spawn_srv(
            model_name='trimesh' + str(random.randint(100, 999)),
            model_xml=open(model_sdf_path, 'r').read(),
            robot_namespace='/',
            initial_pose=Pose(Point(0, 0, (i + 1) * 0.3), Quaternion(0, 0, 0, 1)),
            reference_frame='world'
        )
        i += 1


if __name__ == '__main__':
    main()
