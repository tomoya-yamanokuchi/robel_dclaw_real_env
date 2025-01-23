import rospy
from .. import RobelDClawValveRealEnvironment


def run_tests():
    # ----
    env = RobelDClawValveRealEnvironment()
    # ----
    state = env.get_state()

    print("--------------------------------------------------")
    print("robot_position        = ", state.robot_position)
    print("object_position       = ", state.object_position)
    print("robot_velocity        = ", state.robot_velocity)
    print("object_velocity       = ", state.object_velocity)
    print("end_effector_position = ", state.end_effector_position)
    print("task_space_positioin  = ", state.task_space_positioin)
    print("----------------------------------------------------")


if __name__ == "__main__":
    run_tests()
