import tkinter as tk
import random as rd
color = 0

root = tk.Tk()
root.geometry('600x400')
root.config(bg='yellow')
canva = tk.Canvas(root, width=600, height=400,bg='black')
canva.grid(row=1,column=1,rowspan=3)


def couleur():
    global color
    co = tk.Entry(text=tk.StringVar())
    co.grid(row=0, column=1, sticky='e')
    color=tk.StringVar().get
    print(color)





def carre():
    x = rd.randint(50, 550)
    y = rd.randint(50, 350)
    w = rd.randint(10, 40)
    canva.create_rectangle(x-w,y-w,x+w,y+w,fill='red')






bouton1=tk.Button(root, text='cercle', width=10,pady=10, bg='red')
bouton1.grid(row=1, column=0)

bouton2=tk.Button(root, text='carré', width=10,pady=10, bg='blue',command=carre)
bouton2.grid(row=2, column=0)

bouton3=tk.Button(root, text='croix', width=10,pady=10, bg='green')
bouton3.grid(row=3, column=0)

bouton4=tk.Button(root, text='choisir une couleur', width=30,pady=10, bg='cyan',command=couleur)
bouton4.grid(row=0, column=1)













root.mainloop()