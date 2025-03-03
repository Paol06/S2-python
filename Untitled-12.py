from tkinter import *

root = Tk()
root.geometry("1280x720")
root.config(bg = "blue")

x0 = 640
y0 = 360
dx = 5
dy = 5

image = PhotoImage(file="minecraft.png")
canva = Canvas(root, width=1280, height=720, bg="blue")
canva.pack(expand = True)
creation = canva.create_image(640, 360, image = image)




def mvt():
    global x0, y0, dx, dy

    x0 = x0 + dx
    y0 = y0 + dy
    canva.coords(creation, x0, y0)

    if x0 >= 1280 or x0 <= 0:
        dx = -dx
    if y0 >= 720 or y0 <= 0:
        dy = -dy
    canva.after(50, mvt)
    return

mvt()

root.mainloop()