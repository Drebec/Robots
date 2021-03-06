import Maestro
import sys, tty, os, time, termios

# Create controller instance
c0 = Maestro.Controller() # leave init blank to accept default

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

# sit in loop and scan for inputs

# Defining keyboard input method
def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

# generic function for moving any servo by any amount
def move(channel, delta):
	currentState = c0.getPosition(channel)
	c0.setTarget(channel, currentState + delta)

def recenter():
	c0.setTarget(FORWARD_BACK, 6000)
	c0.setTarget(LEFT_RIGHT, 6000)
	c0.setTarget(BODY, 6000)
	c0.setTarget(HEAD_TILT, 6000)
	c0.setTarget(HEAD_TURN, 6000)

def stop():
	c0.setTarget(FORWARD_BACK, 6000)
	c0.setTarget(LEFT_RIGHT, 6000)

c0.setTarget(BODY, MID)	# reset the body position because it needs to happen for some reason?

# Setting restrictions for all servos
c0.setRange(HEAD_TILT, MIN, MAX)
c0.setRange(HEAD_TURN, MIN, MAX)
c0.setRange(BODY, MIN, MAX)
c0.setRange(FORWARD_BACK, MIN, MAX)
c0.setRange(LEFT_RIGHT, MIN, MAX)

# Setting speeds for all servos
c0.setSpeed(HEAD_TILT, 60)
c0.setSpeed(HEAD_TURN, 60)
c0.setSpeed(LEFT_RIGHT, 60)
c0.setSpeed(FORWARD_BACK, 60)
c0.setSpeed(BODY, 60)

# Setting accelerations for all servos
c0.setAccel(HEAD_TILT, 30)
c0.setAccel(HEAD_TURN, 30)
c0.setAccel(BODY, 30)
c0.setAccel(FORWARD_BACK, 30)
c0.setAccel(LEFT_RIGHT, 30)

# main loop
while True:
	char = getch()	# get the keyboard input

	# terminal case
	if (char == "p"):
		recenter()
		exit(0)

	if (char == ";"):
		recenter()
	if (char == " "):
		stop()

	# big nasty switch to control robot movement based on key pressed
	if (char == "w"):
		move(FORWARD_BACK, -DRIVE_STEP)
		time.sleep(button_delay)
	if (char == "s"):
		move(FORWARD_BACK, DRIVE_STEP)
		time.sleep(button_delay)
	if (char == "a"):
		move(LEFT_RIGHT, DRIVE_STEP)
		time.sleep(button_delay)
	if (char == "d"):
		move(LEFT_RIGHT, -DRIVE_STEP)
		time.sleep(button_delay)
	if (char == "q"):
		move(BODY, TURN_STEP)
		time.sleep(button_delay)
	if (char == "e"):
		move(BODY, -TURN_STEP)
		time.sleep(button_delay)
	if (char == "i"):
		move(HEAD_TILT, TURN_STEP)
		time.sleep(button_delay)
	if (char == "k"):
		move(HEAD_TILT, -TURN_STEP)
		time.sleep(button_delay)
	if (char == "j"):
		move(HEAD_TURN, TURN_STEP)
		time.sleep(button_delay)
	if (char == "l"):
		move(HEAD_TURN, -TURN_STEP)
		time.sleep(button_delay)
