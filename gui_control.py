import tkinter as tk
from Instruction import *
from key_controller import KeyController
import threading

button_height 	= 2
button_width  	= 17
button_padx	  	= 5
button_pady		= 5

can_L = []

instruction_height 	= 100
instruction_width 	= 100

play_pause_width	= 100
play_pause_height	= 75

button_options 		= {"width":button_width, "height":button_height, "padx":button_padx, "pady":button_pady}
instruction_options = {"width":instruction_width, "height":instruction_height, "bg":"black"}
play_pause_options 	= {"width":play_pause_width, "height":play_pause_height}

# Servo positions
MIN, MIN_WAIT 	= 0,0
MAX, MAX_WAIT	= 3000, 5


# Enumerate settings
FORWARD, LEFT, UP 		=  1,1,1
BACKWARD,RIGHT, DOWN	= -1,-1,-1
NO_MOVE					=  0

ic = 0
cmd_L = []


# Base settings dictionaries
motor_D = {"type":"motor", "forward_back":NO_MOVE, "left_right":NO_MOVE, "forward_back_target":MIN, "left_right_target":MIN}

head_D = {"type":"head", "up_down":NO_MOVE, "left_right":NO_MOVE, "up_down_target":MIN, "left_right_target":MIN}

body_D = {"type":"body", "left_right":NO_MOVE, "left_right_target":MIN}

wait_D = {"type":"wait", "delay":MIN_WAIT}

def wrap(i):
	if i > 3:
		return 0
	else:
		return i

def animate_rect(color, can):
	i = 0
	x = 0
	y = 0
	inc = 2
	flags = ["right", "down", "left", "up"]
	while True:
		can.create_rectangle(0, 0, instruction_width, instruction_height, fill="black")
		## determine how to change rectangle location
		#print(flags[i])
		if flags[i] == "right":
			if x < 50:
				x += inc
			else:
				i += 1
			i = wrap(i)
		elif flags[i] == "left":
			if x > 0:
				x -= inc
			else:
				i += 1
			i = wrap(i)
		elif flags[i] == "down":
			if y < 50:
				y += inc
			else:
				i += 1
			i = wrap(i)
		elif flags[i] == "up":
			if y > 0:
				y -= inc
			else:
				i += 1
			i = wrap(i)

		else:
			i = 0
			x = 0
			y = 0

		can.create_rectangle(x, y, x+50, y+50, fill=color)

		time.sleep(.1)

def motor_settings_popup(settings_D):
	print(str(settings_D))
	settings_D["left_right"] += 1

	popup = tk.Toplevel()
	popup.title("Motor Settings")
	popup.geometry("200x400")

def head_settings_popup(settings_D):
	print(str(settings_D))
	settings_D["left_right"] += 1

def body_settings_popup(settings_D):
	print(str(settings_D))
	settings_D["left_right"] += 1

def wait_settings_popup(settings_D):
	print(str(settings_D))
	settings_D["delay"] += 1

def run_motor():
	global ic, cmd_L
	# can_L[ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="blue")
	th = threading.Thread(target=lambda color="blue", can=can_L[ic]: animate_rect(color, can))
	th.start()


	cmd_L.append({"type":"motor", "forward_back":NO_MOVE, "left_right":NO_MOVE, "forward_back_target":MIN, "left_right_target":MIN})

	can_L[ic].bind('<Button-1>', lambda event, settings_D=cmd_L[ic]: motor_settings_popup(settings_D))

	ic += 1

def run_head():
	global ic, cmd_L
	# can_L[ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="green")
	th = threading.Thread(target=lambda color="green", can=can_L[ic]: animate_rect(color, can))
	th.start()

	cmd_L.append({"type":"head", "up_down":NO_MOVE, "left_right":NO_MOVE, "up_down_target":MIN, "left_right_target":MIN})

	can_L[ic].bind('<Button-1>', lambda event, settings_D=cmd_L[ic]: head_settings_popup(settings_D))

	ic += 1

def run_body():
	global ic, cmd_L
	# can_L[ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="red")
	th = threading.Thread(target=lambda color="red", can=can_L[ic]: animate_rect(color, can))
	th.start()

	cmd_L.append({"type":"body", "left_right":NO_MOVE, "left_right_target":MIN})

	can_L[ic].bind('<Button-1>', lambda event, settings_D=cmd_L[ic]: body_settings_popup(settings_D))

	ic += 1

def run_wait():
	global ic, cmd_L
	# can_L[ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="white")
	th = threading.Thread(target=lambda color="white", can=can_L[ic]: animate_rect(color, can))
	th.start()

	cmd_L.append({"type":"wait", "delay":MIN_WAIT})

	can_L[ic].bind('<Button-1>', lambda event, settings_D=cmd_L[ic]: wait_settings_popup(settings_D))

	ic += 1

### MAIN WINDOW ###
win = tk.Tk()
win.title("GUI Control")
win.geometry("1080x720")

### FRAMES ###
# Make a frame to control width/height
win_frame = tk.Frame(master=win)
win_frame.pack()

ins_button_frame = tk.Frame(master=win)
ins_button_frame.pack()

ins_holder_frame = tk.Frame(master=win)
ins_holder_frame.pack()

play_pause_frame = tk.Frame(master=win)
play_pause_frame.pack()

### INSTRUCTION BUTTONS ###
motor = tk.Button(ins_button_frame, button_options, text="Motor Instruction", command=run_motor)
motor.pack(side="left")

head = tk.Button(ins_button_frame, button_options, text="Head Instruction", command=run_head)
head.pack(side="left")

body = tk.Button(ins_button_frame, button_options, text="Body Instruction", command=run_body)
body.pack(side="left")

wait = tk.Button(ins_button_frame, button_options, text="Wait", command=run_wait)
wait.pack(side="left")

### INSTRUCTION SLOTS ###
for i in range(8):
	instruction = tk.Canvas(ins_holder_frame, instruction_options)
	instruction.pack(side="left")
	can_L.append(instruction)

### START/STOP BUTTONS ###
# Create image variables for buttons
play_img = tk.PhotoImage(file="images/play_button.png")
pause_img = tk.PhotoImage(file="images/pause_button.png")
quit_img = tk.PhotoImage(file="images/quit_button.png")

play_button = tk.Button(play_pause_frame, play_pause_options, image=play_img)
play_button.pack(side="left")

pause_button = tk.Button(play_pause_frame, play_pause_options, image=pause_img)
pause_button.pack(side="left")

quit_button = tk.Button(play_pause_frame, play_pause_options, image=quit_img, command=exit)
quit_button.pack(side="left")

### SETTINGS MENUS ###
# motor_settings = tk.Menu(win, tearoff=0)
# motor_settings.add("radiobutton", label="Slow")
# motor_settings.add("radiobutton", label="Medium")
# motor_settings.add("radiobutton", label="Fast")

# # Make a canvas
# can = tk.Canvas(win_frame, width=1080, height=720, bd=2, bg="green")
# can.pack()
#
# can.create_line(0, 0, 1080, 520, fill="blue")
# can.create_rectangle(1080*.1, 520*.1, 1080 * .8, 520 * .8, outline="red")

# Instantiate keyboard controller
kc = KeyController()

win.mainloop()
