import maestro
import time

#c0 = maestro.Controller() # leave init blank to accept default

# Enumerate channels
BODY            = 0
FORWARD_BACK    = 1
LEFT_RIGHT      = 2
HEAD_TURN       = 3
HEAD_TILT       = 4

# Enumerate positions
MIN    = 3000
MID    = 6000
MAX    = 9000

# Enumerate movement steps
DRIVE_STEP = 850
TURN_STEP  = 1000

button_delay = 0.2	# set delay for after keypresses

#  Available controller functions
# setRange(chan, min, max)  set min and max values
# setTarget(chan, target)   set the given channel to change to the given target value
# setSpeed(chan, speed)     set the speed to be used by setTarget
# setAccel(chan, accel)     set the acceleration to be used by setTarget
# getPosition(chan)         get the given channels current position
# isMoving(chan)            returns true if channel has reached its target position
# getMovingState()          returns true if all channels have reached their targets
# runScriptSub(subNumber) runs subroutine
# stopScript() kills the current Maestro script

class KeyController():

	def __init__(self):
		pass
		# # reset the body position because it needs to happen for some reason?
		# c0.setTarget(BODY, MID)
		#
		# # Setting restrictions for all servos
		# c0.setRange(HEAD_TILT, MIN, MAX)
		# c0.setRange(HEAD_TURN, MIN, MAX)
		# c0.setRange(BODY, MIN, MAX)
		# c0.setRange(FORWARD_BACK, MIN, MAX)
		# c0.setRange(LEFT_RIGHT, MIN, MAX)
		#
		# # Setting speeds for all servos
		# c0.setSpeed(HEAD_TILT, 60)
		# c0.setSpeed(HEAD_TURN, 60)
		# c0.setSpeed(LEFT_RIGHT, 60)
		# c0.setSpeed(FORWARD_BACK, 60)
		# c0.setSpeed(BODY, 60)
		#
		# # Setting accelerations for all servos
		# c0.setAccel(HEAD_TILT, 30)
		# c0.setAccel(HEAD_TURN, 30)
		# c0.setAccel(BODY, 30)
		# c0.setAccel(FORWARD_BACK, 30)
		# c0.setAccel(LEFT_RIGHT, 30)

	def forward(self, event):
		self.move(FORWARD_BACK, -DRIVE_STEP)
		time.sleep(button_delay)

	def backward(self, event):
		self.move(FORWARD_BACK, DRIVE_STEP)
		time.sleep(button_delay)

	def left(self, event):
		self.move(LEFT_RIGHT, -DRIVE_STEP)
		time.sleep(button_delay)

	def right(self, event):
		self.move(LEFT_RIGHT, DRIVE_STEP)
		time.sleep(button_delay)

	def body_left(self, event):
		self.move(BODY, TURN_STEP)
		time.sleep(button_delay)

	def body_right(self, event):
		self.move(BODY, -TURN_STEP)
		time.sleep(button_delay)

	def head_left(self, event):
		self.move(HEAD_TURN, TURN_STEP)
		time.sleep(button_delay)

	def head_right(self, event):
		self.move(HEAD_TURN, -TURN_STEP)
		time.sleep(button_delay)

	def head_up(self, event):
		self.move(HEAD_TILT, TURN_STEP)
		time.sleep(button_delay)

	def head_down(self, event):
		self.move(HEAD_TILT, -TURN_STEP)
		time.sleep(button_delay)

	# generic function for moving any servo by any amount
	def move(self, channel, delta):
		# currentState = c0.getPosition(channel)
		# c0.setTarget(channel, currentState + delta)
		print("CHANGE CHANNEL <" + str(channel) + "> BY <" + str(delta) + ">")

	def recenter(self, event):
		c0.setTarget(FORWARD_BACK, MID)
		c0.setTarget(LEFT_RIGHT, MID)
		c0.setTarget(BODY, MID)
		c0.setTarget(HEAD_TILT, MID)
		c0.setTarget(HEAD_TURN, MID)

	def stop(self,event):
		c0.setTarget(FORWARD_BACK, MID)
		c0.setTarget(LEFT_RIGHT, MID)
