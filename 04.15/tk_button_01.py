import tkinter as tk

root = tk.Tk()

def func():
    print("Pushed")

button = tk.Button(root,text="PUSH!!",command=func)
button.pack()

root.mainloop()
