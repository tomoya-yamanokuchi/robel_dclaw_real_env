import rospy
import numpy as np
from std_msgs.msg import Int32MultiArray
from ...utils import ParameterObject


class JointCtrlPublisher:
    def __init__(self, params: ParameterObject):
        # ------
        self.TOPIC_NAME : str = "/dclaw/joint_ctrl/command"
        self.sleep_time_sec   = params.sleep_time_sec
        self.queue_size       = params.queue_size
        # -------
        self._msg = Int32MultiArray()
        self._pub = rospy.Publisher(
            name       = self.TOPIC_NAME,
            data_class = Int32MultiArray,
            queue_size = self.queue_size,
        )
        # -------
        self._num_joint_ctrl = 9

    def publish(self, joint_ctrl_resolution: np.ndarray):
        assert joint_ctrl_resolution.shape == (self._num_joint_ctrl,)
        # ---
        self._msg.data = tuple(joint_ctrl_resolution)
        self._pub.publish(self._msg)
        rospy.sleep(self.sleep_time_sec)
