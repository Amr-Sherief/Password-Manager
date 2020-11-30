import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Password Manager")

val = tk.StringVar()

options = ["Add Password", "Retrieve Password", "Generate Password"]
menu = tk.OptionMenu(root, val, *options)
menu.pack()
root.mainloop()
