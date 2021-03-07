from tkinter import *

# Window Set
window = Tk()
window.title("Test")
window.geometry("800x600")
window.resizable(0, 0)

# Gif, Png File Loc Set
backgroundpng = PhotoImage(file = "./HWSV/BG.png")
wolfgif = PhotoImage(file = "./HWSV/wolf.gif")
sheepgif = PhotoImage(file = "./HWSV/sheep.gif")
vegetablegif = PhotoImage(file = "./HWSV/vegetable.gif")
ballpng = PhotoImage(file = "./HWSV/B.png")

# BG Set
background = Canvas(window, width = 800, height = 600)
background.create_image(400, 300, image = backgroundpng)
background.pack()
ball = Canvas(window, width = 128, height = 128)
ball.create_image(66, 66, image = ballpng)
ball.place(x = 300, y = 100)

# Button Set
wolf = Button(window, image = wolfgif, width = 128, height = 128).place(x = 65, y = 50)
sheep = Button(window, image = sheepgif, width = 128, height = 128).place(x = 65, y = 230)
vegetable = Button(window, image = vegetablegif, width = 128, height = 128).place(x = 65, y = 415)

window.mainloop()