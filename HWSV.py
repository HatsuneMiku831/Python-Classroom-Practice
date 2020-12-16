from tkinter import *

window = Tk()
window.title("Test")
window.geometry("800x600")
window.resizable(0, 0)

canvas = Canvas(window, width = 266, height = 600, bg = "forest green").place(x = 0, y = 0)
canvas1 = Canvas(window, width = 268, height = 600, bg = "deepskyblue2").place(x = 267, y = 0)
canvas2 = Canvas(window, width = 266, height = 600, bg = "forest green").place(x = 535, y = 0)

wolfgif = PhotoImage(file = "wolf.gif")

wolf = Button(window, image = wolfgif, width = 128, height = 128).pack(side = LEFT)

window.mainloop()