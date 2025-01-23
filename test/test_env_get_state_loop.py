import rospy
from .. import RobelDClawValveRealEnvironment


def run_tests():
    # ----
    env = RobelDClawValveRealEnvironment()
    # ----
    rate = rospy.Rate(hz=60)  # 10Hzでループ
    while not rospy.is_shutdown():
        try:
            state = env.get_state()
            print(f"robot_position = {state.robot_position}")
        except Exception:
            rospy.logwarn("An exception occurred during state retrieval.")
        rate.sleep()


if __name__ == "__main__":
    run_tests()
