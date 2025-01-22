import rospy
import angle_interface as ai
from .publish import Publisher
from .subscribe import SubscriberManager
from .utils import ParameterObject


class ROSHandler:
    def __init__(self, params: ParameterObject):
        self.node_name  = params.node_name
        rospy.init_node(self.node_name, anonymous=True)
        self.publisher  = Publisher(params)
        self.subscriber = SubscriberManager(params)
        while not self.subscriber.all_initialized:
            rospy.sleep(0.1)

    def wait_initialization(self):
        while not self.subscriber.initialization_state.is_initialize_finished:
            rospy.sleep(0.1)
        rospy.loginfo("initialization is finsed!!")
