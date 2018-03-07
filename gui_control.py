import tkinter as tk
from Instruction import *
#from key_controller import KeyController
import threading
import sys

# Set up constants for button dimensions

button_height 	= 2
button_width  	= 17
button_padx	  	= 5
button_pady		= 5

can_L = []

instruction_height 	= 90
instruction_width 	= 90

play_pause_width	= 100
play_pause_height	= 75

button_options 		= {"width":button_width, "height":button_height, "padx":button_padx, "pady":button_pady}
instruction_options = {"width":instruction_width, "height":instruction_height, "bg":"black"}
play_pause_options 	= {"width":play_pause_width, "height":play_pause_height}
scale_options		= {"width":20, "length":200, "orient":"horizontal"}

# Servo positions
MIN, MIN_WAIT 	= 0,0
MAX, MAX_WAIT	= 3000, 5


# Enumerate settings
FORWARD, LEFT, UP 		=  1,1,1
BACKWARD,RIGHT, DOWN	= -1,-1,-1
NO_MOVE					=  0

# instruction variables
ic 		= 0
cmd_L 	= []
th_L 	= []


# Base settings dictionaries
motor_D = {"type":"motor", "forward_back":NO_MOVE, "left_right":NO_MOVE, "forward_back_target":MIN, "left_right_target":MIN, "delay":NO_MOVE}

head_D = {"type":"head", "up_down":NO_MOVE, "left_right":NO_MOVE, "up_down_target":MIN, "left_right_target":MIN}

body_D = {"type":"body", "left_right":NO_MOVE, "left_right_target":MIN}

wait_D = {"type":"wait", "delay":MIN_WAIT}

thread_kill = False
anican = 0


def wrap(i):
	if i > 3:
		return 0
	else:
		return i

def animate_rect(color, can):
	global thread_kill
	i = 0
	x = 0
	y = 0
	inc = 2
	flags = ["right", "down", "left", "up"]
	while not thread_kill:
		can.create_rectangle(0, 0, instruction_width, instruction_height, fill="black")
		## determine how to change rectangle location
		#print(flags[i])
		if flags[i] == "right":
			if x < instruction_width - 50:
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
			if y < instruction_height - 50:
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

def stop_thread():
	global thread_kill
	thread_kill = True

def start_thread():
	global thread_kill
	thread_kill = False


def motor_settings_popup(settings_D):

	popup = tk.Toplevel(width=300, height=400)
	popup.title("Motor Settings")
	forward_back = tk.Scale(popup, scale_options, label="Backward or Forward?", from_=-1, to=1)
	forward_back_target = tk.Scale(popup, scale_options, label="Speed", from_=0, to=3000)
	left_right = tk.Scale(popup, scale_options, label="Left or Right?", from_=-1, to=1)
	left_right_target = tk.Scale(popup, scale_options, label="Speed", from_=0, to=3000)
	delay = tk.Scale(popup, scale_options, label="Time", from_=0, to=10)
	forward_back.pack()
	forward_back_target.pack()
	left_right.pack()
	left_right_target.pack()
	delay.pack()


	button = tk.Button(popup, text="Save Settings", command=lambda popup=popup, settings_D=settings_D, forward_back=forward_back, forward_back_target=forward_back_target, left_right=left_right, left_right_target=left_right_target, delay=delay: set_motor_settings(popup, settings_D, forward_back, forward_back_target, left_right, left_right_target, delay))
	button.pack()

def set_motor_settings(popup, settings_D, forward_back, forward_back_target, left_right, left_right_target, delay):
	settings_D["forward_back"] = int(forward_back.get())
	settings_D["forward_back_target"] = int(forward_back_target.get())
	settings_D["left_right"] = int(left_right.get())
	settings_D["left_right_target"] = int(left_right_target.get())
	settings_D["delay"] = int(delay.get())
	popup.destroy()


def head_settings_popup(settings_D):
	popup = tk.Toplevel(width=300, height=400)
	popup.title("Head Settings")
	up_down = tk.Scale(popup, scale_options, label="Up or Down?", from_=-1, to=1)
	up_down_target = tk.Scale(popup, scale_options, label="Target", from_=0, to=3000)
	left_right = tk.Scale(popup, scale_options, label="Left or Right?", from_=-1, to=1)
	left_right_target = tk.Scale(popup, scale_options, label="Target", from_=0, to=3000)
	up_down.pack()
	up_down_target.pack()
	left_right.pack()
	left_right_target.pack()


	button = tk.Button(popup, text="Save Settings", command=lambda popup=popup, settings_D=settings_D, up_down=up_down, up_down_target=up_down_target, left_right=left_right, left_right_target=left_right_target: set_head_settings(popup, settings_D, up_down, up_down_target, left_right, left_right_target))
	button.pack()

def set_head_settings(popup, settings_D, up_down, up_down_target, left_right, left_right_target):
	settings_D["up_down"] = int(up_down.get())
	settings_D["up_down_target"] = int(up_down_target.get())
	settings_D["left_right"] = int(left_right.get())
	settings_D["left_right_target"] = int(left_right_target.get())
	popup.destroy()

def body_settings_popup(settings_D):
	popup = tk.Toplevel(width=300, height=400)
	popup.title("Body Settings")
	left_right = tk.Scale(popup, scale_options, label="Left or Right?", from_=-1, to=1)
	left_right_target = tk.Scale(popup, scale_options, label="Target", from_=0, to=3000)
	left_right.pack()
	left_right_target.pack()

	button = tk.Button(popup, text="Save Settings", command=lambda popup=popup, settings_D=settings_D, left_right=left_right, left_right_target=left_right_target: set_body_settings(popup, settings_D, left_right, left_right_target))
	button.pack()

def set_body_settings(popup, settings_D, left_right, left_right_target):
	settings_D["left_right"] = int(left_right.get())
	settings_D["left_right_target"] = int(left_right_target.get())
	popup.destroy()

def wait_settings_popup(settings_D):
	popup = tk.Toplevel(width=300, height=400)
	popup.title("Wait Settings")
	delay = tk.Scale(popup, scale_options, label="Time", from_=0, to=10)
	delay.pack()

	button = tk.Button(popup, text="Save Settings", command=lambda popup=popup, settings_D=settings_D, delay=delay: set_wait_settings(popup, settings_D, delay))
	button.pack()

def set_wait_settings(popup, settings_D, delay):
	settings_D["delay"] = int(delay.get())
	popup.destroy()

def run_motor():
	global ic, cmd_L, th_L, motor_img
	can_L[ic].create_image(instruction_width/2,instruction_height/2, image=motor_img)

	#can_L[ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="blue")
	# th = threading.Thread(target=lambda color="blue", can=can_L[ic]: animate_rect(color, can))
	# th_L.append(th)
	#th.start()


	cmd_L.append({"type":"motor", "forward_back":NO_MOVE, "left_right":NO_MOVE, "forward_back_target":MIN, "left_right_target":MIN})

	can_L[ic].bind('<Button-1>', lambda event, settings_D=cmd_L[ic]: motor_settings_popup(settings_D))

	ic += 1

def run_head():
	global ic, cmd_L, th_L, head_img
	can_L[ic].create_image(instruction_width/2,instruction_height/2, image=head_img)

	# can_L[ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="green")
	# th = threading.Thread(target=lambda color="green", can=can_L[ic]: animate_rect(color, can))
	# th_L.append(th)
	#th.start()

	cmd_L.append({"type":"head", "up_down":NO_MOVE, "left_right":NO_MOVE, "up_down_target":MIN, "left_right_target":MIN})

	can_L[ic].bind('<Button-1>', lambda event, settings_D=cmd_L[ic]: head_settings_popup(settings_D))

	ic += 1

def run_body():
	global ic, cmd_L, th_L, bod_img
	can_L[ic].create_image(instruction_width/2,instruction_height/2, image=bod_img)

	# can_L[ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="red")
	# th = threading.Thread(target=lambda color="red", can=can_L[ic]: animate_rect(color, can))
	# th_L.append(th)
	# th.start()

	cmd_L.append({"type":"body", "left_right":NO_MOVE, "left_right_target":MIN})

	can_L[ic].bind('<Button-1>', lambda event, settings_D=cmd_L[ic]: body_settings_popup(settings_D))

	ic += 1

def run_wait():
	global ic, cmd_L, th_L, wait_img
	can_L[ic].create_image(instruction_width/2,instruction_height/2, image=wait_img)

	# can_L[ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="white")
	# th = threading.Thread(target=lambda color="white", can=can_L[ic]: animate_rect(color, can))
	# th_L.append(th)
	#th.start()

	cmd_L.append({"type":"wait", "delay":MIN_WAIT})

	can_L[ic].bind('<Button-1>', lambda event, settings_D=cmd_L[ic]: wait_settings_popup(settings_D))

	ic += 1

def delete_all():
	global cmd_L, can_L, th_L, ic
	# clear all lists
	cmd_L = []
	th_L  = []
	ic    = 0

	for i in range(8):
		can_L[i].destroy()

	can_L = []

	for i in range(8):
		instruction = tk.Canvas(ins_holder_frame, instruction_options)
		instruction.pack(side="left")
		can_L.append(instruction)

def delete_index(index):
	global can_L, cmd_L, th_L, ic
	can_L.delete(index)

def program_helper():
	global anican, prog_thread, thread_kill, bg_img
	# run animation
	# run program

	animation_win = tk.Toplevel()
	animation_win.overrideredirect(1)
	animation_win.title("Animation")
	animation_win.geometry("790x450")

	# bg_can = tk.Canvas(animation_win)
	# bg_can.create_image(0, 0, image=bg_img)

	anican = tk.Label(animation_win)
	anican.pack()

	prog_thread = threading.Thread(target=run_program)
	prog_thread.start()

	thread_kill = False
	update(0, animation_win)

def update(ind, window):
	global anican, anim
	frame = anim[ind]
	ind += 1
	anican.config(image=frame)
	if ind == 2:
		ind = 0
	if not thread_kill:
		anican.after(100, update, ind, window)
	else:
		window.destroy()

def run_program():
	global thread_kill
	thread_kill = False
	for i in cmd_L:
		print(str(i))

		command_type = list(i.values())[0]
		temp = dict(i)
		temp.pop("type")
		command_args = temp
		print(command_type)
		if i["type"] == "motor":
			inst = Motor(**command_args)
		elif i["type"] == "body":
			inst = Body(**command_args)
		elif i["type"] == "head":
			inst = Head(**command_args)
		elif i["type"] == "wait":
			inst = Wait(**command_args)

		#start_thread()
		#print(str(th_L[cmd_L.index(i)]))
		#th_L[cmd_L.index(i)].start()
		#th = threading.Thread(target=lambda color="blue", can=can_L[cmd_L.index(i)]: animate_rect(color, can))
		#th.start()
		inst.execute()
		#stop_thread()
	print("finished exectution")
	thread_kill = True
	return 0

### MAIN WINDOW ###
win = tk.Tk()
win.title("GUI Control")
win.geometry("790x450")

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
play_img 	= tk.PhotoImage(file="images/play_button.png")
clear_img 	= tk.PhotoImage(file="images/clear_button.png")
quit_img 	= tk.PhotoImage(file="images/quit_button.png")

motor_img 	= tk.PhotoImage(file="images/Motor.png")
head_img	= tk.PhotoImage(file="images/Head.png")
bod_img		= tk.PhotoImage(file="images/Bod.png")
wait_img	= tk.PhotoImage(file="images/Wait.png")

play_button = tk.Button(play_pause_frame, play_pause_options, image=play_img, command=program_helper)
play_button.pack(side="left")

pause_button = tk.Button(play_pause_frame, play_pause_options, image=clear_img, command=delete_all)
pause_button.pack(side="left")

quit_button = tk.Button(play_pause_frame, play_pause_options, image=quit_img, command=exit)
quit_button.pack(side="left")

anim = [tk.PhotoImage(file="images/ash_running.gif", format='gif -index %i' %(i)) for i in range(2)]
anim[0] = anim[0].zoom(2)
anim[1] = anim[1].zoom(2)
bg_img = tk.PhotoImage(file="images/pallet-town-rby.png")

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
#kc = KeyController()

win.mainloop()
