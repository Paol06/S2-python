from tkinter import *

root = Tk()

canva = Canvas(root, width=1280, height=720, bg='blue')
canva.pack(fill='both', expand=True)

x0 = 610
y0 = 610
dx = 5
dy = 5

rect = canva.create_rectangle(x0,y0,x0+20,y0+20, fill='red', width=2)

def mvt():
    global x0, y0, dx, dy
    x0 = x0 + dx
    y0 = y0 + dy

    canva.coords(rect,x0,y0,x0+20,y0+20)

    if x0 >= 1280 or x0 <= 0:
        dx = -dx
    if y0 >= 720 or y0 <= 0:
        dy = -dy
    
    canva.after(50,mvt)

mvt()





root.mainloop()