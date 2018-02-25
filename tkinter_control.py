import tkinter as tk
from key_controller import KeyController

# Create main window
win = tk.Tk()
win.title("GUI Controller")

# Instantiate keyboard controller
kc = KeyController()

### BIND BUTTONS ###
## MOVEMENT ##
win.bind("w", kc.forward)
win.bind("a", kc.left)
win.bind("s", kc.backward)
win.bind("d", kc.right)

## HEAD ##
win.bind("i", kc.head_up)
win.bind("j", kc.head_left)
win.bind("k", kc.head_down)
win.bind("l", kc.head_right)

## BODY ##
win.bind("q", kc.body_left)
win.bind("e", kc.body_right)

## STOPPING ##
win.bind(";", kc.recenter)
win.bind("<space>", kc.stop)

## QUIT ##
win.bind("p", exit)

# Begin the mainloop
win.mainloop()
