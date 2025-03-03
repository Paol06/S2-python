import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
x1 = 0

canva = tk.Canvas(root, width=600, height=400)
canva.grid(rowspan=1,columnspan=1)

button1 = tk.Button(canva, name='ok', width = 20, pady=10)
button1.grid(row=0, column=0)



button3 = tk.Button(canva, name='calculer',width=20,pady=10)
button3.grid(row=1, column=1)
label1 = tk.Label()








root.mainloop()