import rospy
import numpy as np
from std_msgs.msg import Int32
from ...utils import ParameterObject


class ValveCtrlPublisher:
    def __init__(self, params: ParameterObject):
        # ------
        self.TOPIC_NAME : str = "/dclaw/valv_ctrl/command"
        self.sleep_time_sec   = params.sleep_time_sec
        self.queue_size       = params.queue_size
        # -------
        self._msg = Int32()
        self._pub = rospy.Publisher(
            name       = self.TOPIC_NAME,
            data_class = Int32,
            queue_size = self.queue_size,
        )
        # -----
        self._num_valve_ctrl = 1

    def publish(self, valve_ctrl_resolution: np.ndarray):
        assert valve_ctrl_resolution.shape == (self._num_valve_ctrl,)
        # ---
        self._msg.data = tuple(valve_ctrl_resolution)
        self._pub.publish(self._msg)
        rospy.sleep(self.sleep_time_sec)
