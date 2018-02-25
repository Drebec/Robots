import tkinter as tk
from key_controller import KeyController

button_height 	= 2
button_width  	= len("Motor Instruction")
button_padx	  	= 5
button_pady		= 5

instruction_height 	= 50
instruction_width 	= 50

button_options 		= {"width":button_width, "height":button_height, "padx":button_padx, "pady":button_pady}
instruction_options = {"width":instruction_width, "height":instruction_height}

win = tk.Tk()
win.title("GUI Control")
win.geometry("1080x720")

# Make a frame to control width/height
win_frame = tk.Frame(master=win)
win_frame.pack()

motor = tk.Button(win_frame, button_options, text="Motor Instruction")
motor.grid(column=2, row=0)

head = tk.Button(win_frame, button_options, text="Head Instruction")
head.grid(column=4, row=0)

body = tk.Button(win_frame, button_options, text="Body Instruction")
body.grid(column=6, row=0)

pause = tk.Button(win_frame, button_options, text="Pause")
pause.grid(column=8, row=0)

# # Make a canvas
# can = tk.Canvas(win_frame, width=1080, height=720, bd=2, bg="green")
# can.pack()
#
# can.create_line(0, 0, 1080, 520, fill="blue")
# can.create_rectangle(1080*.1, 520*.1, 1080 * .8, 520 * .8, outline="red")

# Instantiate keyboard controller
kc = KeyController()

win.mainloop()
