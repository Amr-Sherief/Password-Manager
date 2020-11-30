import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Password Manager")

val = tk.StringVar()


options = ["Add Password", "Show Passwords", "Generate Password"]


def check():
    if val == options[0]:
        print("why")


circle = tk.PhotoImage(file="gimp-button.png")

menu = tk.OptionMenu(root, val, *options, command=check())
menu.pack()

commit = tk.Button(root, image=circle, width=25, height=25, command=check())
commit.pack()

print(val)

root.mainloop()
