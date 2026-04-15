import tkinter as tk

root = tk.Tk()
label = tk.Label(root,text="サンプル")

def func():
  root.destroy()  

button = tk.Button(root,text="終了",command=func)
label.pack()
button.pack()


root.mainloop()
