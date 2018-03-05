import tkinter as tk

win = tk.Tk()
#win.geometry("790x450")
win.title("Ash Running")

anim = [tk.PhotoImage(file="images/ash_running.gif", format='gif -index %i' %(i)) for i in range(2)]

def update(ind):
	frame = anim[ind]
	ind += 1
	can.config(image=frame)
	if ind == 2:
		ind = 0
	can.after(500, update, ind)

can = tk.Label()
can.pack()

win.after(0, update, 0)

win.mainloop()
