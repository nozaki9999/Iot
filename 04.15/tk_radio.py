import tkinter as tk

root =tk.Tk()

def func1():
    label.config(text = "ボタン1")
def func2():
    label.config(text = "ボタン1")
label = tk.Label()
label.pack()


sel = tk.IntVar()

sel.set(1)

rb1 = tk.Radiobutton(root,text = "ボタン1",variable = sel,value = 1,command = func1)
rb1.pack()

rb2 = tk.Radiobutton(root,text = "ボタン2",variable = sel,value = 2,command = func2)
rb2.pack()
root.mainloop()