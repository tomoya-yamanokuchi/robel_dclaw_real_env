import rospy
from .. import RobelDClawValveRealEnvironment
import cv2

def run_tests():
    # ----
    env = RobelDClawValveRealEnvironment()
    # ----
    rate = rospy.Rate(hz=60)  # 10Hzでループ
    while not rospy.is_shutdown():
        try:
            state = env.get_state()
            # print(f"robot_position = {state.robot_position}")

            img = env.get_image()
            print(f"image.shape = {img.shape}")
            # cv2.imshow('window', img)
            # cv2.waitKey(100)
            # cv.save
            # import ipdb; ipdb.set_trace()
            # cv2.imwrite('output.png', img)
            import ipdb; ipdb.set_trace()

        except Exception:
            rospy.logwarn("An exception occurred during state retrieval.")
        rate.sleep()


if __name__ == "__main__":
    run_tests()
