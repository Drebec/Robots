from maestro import Controller
import time

# c0 = Controller()

BODY            = 0
FORWARD_BACK    = 1
LEFT_RIGHT      = 2
HEAD_TURN       = 3
HEAD_TILT       = 4

class Motor:
    def __init__(self, forward_back=0, left_right=0, delay=0, forward_back_target=0, left_right_target=0):
        self.delay = delay
        self.forward_back_target = forward_back_target
        self.left_right_target = left_right_target

    # def get_forward_back_target(self):
    #     return self.forward_back_target
    #
    # def get_left_right_target(self):
    #     return self.left_right_target
    #
    # def set_forward_back_target(self, forward_back_target):
    #     self.forward_back_target = forward_back_target
    #
    # def set_left_right_target(self, left_right_target):
    #     self.left_right_target = left_right_target

    def execute(self):
        #c0.setTarget(FORWARD_BACK, 6000 + (self.forward_back * self.forward_back_target))
        #c0.setTarget(LEFT_RIGHT, 6000 + (self.left_right * self.left_right_target))
        print("Executing Motor Movement")
        #time.sleep(delay)

class Body:
    def __init__(self, left_right=0, left_right_target=0):
        self.left_right = left_right
        self.left_right_target = left_right_target

    # def get_target(self):
    #     return self.target
    #
    # def set_target(self, target):
    #     self.target = target
    #
    def execute(self):
        # c0.setTarget(BODY, 6000 + (self.left_right * self.left_right_target))
        print("Executing Body Movement")

class Head:
    def __init__(self, up_down=0, left_right=0, up_down_target=0, left_right_target=0):
        self.up_down_target = up_down_target
        self.left_right_target = left_right_target

    # def get_up_down_target(self):
    #     return self.up_down_target
    #
    # def get_left_right_target(self):
    #     return self.left_right_target
    #
    # def set_up_down_target(self, up_down_target):
    #     self.up_down_target = up_down_target
    #
    # def set_left_right_target(self, left_right_target):
    #     self.left_right_target = left_right_target

    def execute(self):
        # c0.setTarget(HEAD_TURN, 6000 + (self.left_right * self.left_right_target))
        # c0.setTarget(HEAD_TILT, 6000 + (self.up_down * self.up_down_target))
        print("Executing Head Movement" + str(self.up_down_target))


class Wait:
    def __init__(self, delay=0):
        self.delay = delay

    # def get_delay(self):
    #     return self.delay
    #
    # def set_delay(self, time):
    #     self.delay = delay

    def execute(self):
        # time.sleep(delay)
        print("Executing Wait" + str(self.delay))
