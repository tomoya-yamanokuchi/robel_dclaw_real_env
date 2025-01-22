import rospy
import numpy as np
from std_msgs.msg import Int32MultiArray


class InitializeCommandPublisher:
    def __init__(self,
            sleep_time_sec: float = 1.0,
            queue_size    : int   = 10,
        ):
        # ------
        self.TOPIC_NAME : str = "/dclaw/initialize_ctrl/command"
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
        self._num_ctrl            = 9
        self._num_current_limit   = 9
        self._num_position_p_gain = 9
        self._num_init_command    = (self._num_ctrl + self._num_current_limit + self._num_position_p_gain)


    def publish(self, initialize_command: np.ndarray):
        assert initialize_command.shape == (self._num_init_command,)
        # ---
        self._msg.data = tuple(initialize_command)
        self._pub.publish(self._msg)
        rospy.sleep(self.sleep_time_sec)


