import tkinter as tk
from Instruction import *
from key_controller import KeyController

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

class ButtonCommand:
	ic = 0
	cmd_L = []

	@classmethod
	def run_motor(self):
		can_L[ButtonCommand.ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="blue")
		ButtonCommand.ic += 1
		ButtonCommand.cmd_L.append()


	@classmethod
	def run_head(self):
		can_L[ButtonCommand.ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="green")
		ButtonCommand.ic += 1

	@classmethod
	def run_body(self):
		can_L[ButtonCommand.ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="red")
		ButtonCommand.ic += 1

	@classmethod
	def run_wait(self):
		can_L[ButtonCommand.ic].create_rectangle(.2*instruction_width, .2*instruction_height, .8*instruction_width, .8*instruction_height, fill="white")
		ButtonCommand.ic += 1


win = tk.Tk()
win.title("GUI Control")
win.geometry("1080x720")

# Make a frame to control width/height
win_frame = tk.Frame(master=win)
win_frame.pack()

ins_button_frame = tk.Frame(master=win)
ins_button_frame.pack()

# blank = tk.Canvas(win_frame, height=30, width=1080)
# blank.pack()

ins_holder_frame = tk.Frame(master=win)
ins_holder_frame.pack()

play_pause_frame = tk.Frame(master=win)
play_pause_frame.pack()

motor = tk.Button(ins_button_frame, button_options, text="Motor Instruction", command=ButtonCommand.run_motor)
motor.pack(side="left")

head = tk.Button(ins_button_frame, button_options, text="Head Instruction", command=ButtonCommand.run_head)
head.pack(side="left")

body = tk.Button(ins_button_frame, button_options, text="Body Instruction", command=ButtonCommand.run_body)
body.pack(side="left")

pause = tk.Button(ins_button_frame, button_options, text="Pause", command=ButtonCommand.run_wait)
pause.pack(side="left")

for i in range(8):
	instruction = tk.Canvas(ins_holder_frame, instruction_options)
	instruction.pack(side="left")
	can_L.append(instruction)


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

# # Make a canvas
# can = tk.Canvas(win_frame, width=1080, height=720, bd=2, bg="green")
# can.pack()
#
# can.create_line(0, 0, 1080, 520, fill="blue")
# can.create_rectangle(1080*.1, 520*.1, 1080 * .8, 520 * .8, outline="red")

# Instantiate keyboard controller
kc = KeyController()

win.mainloop()
