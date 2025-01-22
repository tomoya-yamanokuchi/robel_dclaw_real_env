import rospy
import numpy as np
from std_msgs.msg import Int32MultiArray


class JointCtrlPublisher:
    def __init__(self,
            sleep_time_sec: float = 1.0,
            queue_size    : int   = 10,
        ):
        # ------
        self.TOPIC_NAME : str = "/dclaw/joint_ctrl/command"
        self.sleep_time_sec   = sleep_time_sec
        self.queue_size       = queue_size
        # -------
        self._msg = Int32MultiArray()
        self._pub = rospy.Publisher(
            name       = self.TOPIC_NAME,
            data_class = Int32MultiArray,
            queue_size = queue_size,
        )
        # -------
        self._num_joint_ctrl = 9

    def publish(self, joint_ctrl_resolution: np.ndarray):
        assert joint_ctrl_resolution.shape == (self._num_joint_ctrl,)
        # ---
        self._msg.data = tuple(joint_ctrl_resolution)
        self._pub.publish(self._msg)
        rospy.sleep(self.sleep_time_sec)
