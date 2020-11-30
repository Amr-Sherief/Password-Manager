import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(

)

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Password Manager")

val = tk.StringVar()

value = val.get()

frame = tk.Frame(root)
frame.pack(side='top')

options = ["Add Password", "Show Passwords", "Generate Password"]


def check():
    if val.get() == options[0]:
        e_label = tk.Label(frame, text="Email")
        e_label.grid(row=3, column=0, sticky='W')
        email = tk.Entry(frame)
        email.grid(row=3, column=1)
        p_label = tk.Label(frame, text="Password")
        p_label.grid(row=4, column=0, sticky='W')
        password = tk.Entry(frame)
        password.grid(row=4, column=1)
        submit = tk.Button(frame, text="Submit", fg="red")
        submit.grid(row=5, column=0, columnspan=2)


menu = tk.OptionMenu(frame, val, *options)
menu.grid(row=0, column=0, columnspan=2)

circle = tk.PhotoImage(file="gimp-button.png")
commit = tk.Button(frame, image=circle, width=25, height=25, command=check)
commit.grid(row=1, column=0, columnspan=2)

root.mainloop()
