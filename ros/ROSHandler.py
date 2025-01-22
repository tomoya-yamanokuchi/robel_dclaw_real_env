
import sys
import numpy as np
import rospy
# import pathlib
import angle_interface as ai

# from ros_scripts.publisher import Publisher
# from ros_scripts.subscriber import Subscriber


from .publish import Publisher
from .subscribe import SubscriberManager


class ROSHandler:
    def __init__(self,
            node_name               : str   = "dclaw_node",
            publisher_sleep_time_sec: float = 1.0,
        ):
        self.node_name = node_name
        rospy.init_node(self.node_name, anonymous=True) # initialize "ros node"

        self.publisher  = Publisher(sleep_time_sec=publisher_sleep_time_sec)
        self.subscriber = SubscriberManager()

        while self.subscriber.all_initialized:
            rospy.sleep(0.1)

        # rospy.spin()
        import ipdb; ipdb.set_trace()

        self.__wait_ros_connection_establishment()
        self.print_initialized_message()


    def __wait_ros_connection_establishment(self):

        # 管理オブジェクトを作成
        manager = InitializationStateManager(total_subscribers=5)

        # 5つのサブスクライバーを作成して登録
        subscribers = [
            InitializationStateSubscriber(i, manager) for i in range(5)
        ]

        rospy.sleep(0.25)
        while self.subscriber.get_connection_flag_True_num() == self.__Subscriber.subscribe_sum:
            rospy.sleep(0.5)


    def print_initialized_message(self):
        rospy.loginfo("ROS connection is established!")


    def reset_env(self, sleep_time_sec=1):
        ctrl_init_positions  = ai.degree2resolution([0,0,0,  0,0,0,  0,0,0])
        claw_Position_P_Gain = np.array([200, 200, 200])
        init_command         = np.hstack([ctrl_init_positions, claw_Position_P_Gain])
        self.publish_initialize_ctrl(init_command)
        rospy.sleep(sleep_time_sec)




if __name__ == '__main__':

    from joint_space_target_example import JointSpaceTargetExample
    target_example = JointSpaceTargetExample()
    ros_handler = ROSHandler(node_name=None)

    print(ros_handler.node_name)


    for i in range(3):
        print(ros_handler.get_joint_positions())
        rospy.sleep(0.01)

    ros_handler.reset_env()


    # ros_handler.publish_joint_ctrl(ctrl=target_example.target1)
    # rospy.sleep(2)

    # ros_handler.publish_joint_ctrl(ctrl=target_example.target2)
    # rospy.sleep(2)

    # ros_handler.publish_joint_ctrl(ctrl=target_example.target3)
    # rospy.sleep(2)

    # ros_handler.publish_joint_ctrl(ctrl=target_example.target4)
    # rospy.sleep(2)

    # ros_handler.publish_joint_ctrl(ctrl=target_example.target5)
    # rospy.sleep(2)
