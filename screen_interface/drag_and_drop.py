import tkinter as tk

class Block:
    def __init__(self, xpos, ypos, width, height, canvas, color="#FFFF00"):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        self.canvas = canvas

    def show(self):
        self.canvas.create_rectangle(self.xpos, self.ypos, self.xpos + self.width, self.ypos + self.height, fill=self.color)
        self.canvas.pack()

    def adjust(self, xpos, ypos, width, height):
        self.xpos += xpos
        self.ypos += ypos
        self.width += width
        self.height += height


window = tk.Tk()
canvas = tk.Canvas(window, bg="#333333", height="550", width="1000")
canvas.pack()

blocks = []
for i in range(5):
    blocks.append(Block(30, (100*i)+30, 75, 75, canvas))

for i in range(len(blocks)):
    blocks[i].show()
block = Block(500, 500, 100, 100, canvas)
# block.show()
# block.adjust(100, 100, -50, -50)
# block.show()

window.mainloop()
