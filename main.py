import tkinter as tk
import mysql.connector
import random

mydb = mysql.connector.connect(

)

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Password Manager")

val = tk.StringVar()

value = val.get()

frame = tk.Frame(root)
frame.pack(side='top')

options = ["Add Login", "Show Logins", "Generate Password"]


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
    if val.get() == options[1]:
        return 0
    if val.get() == options[2]:
        s_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                      'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        c_alphabet = ['A', 'B', 'C', 'd', 'E', 'F', 'G', 'H',
                      'I', 'J', 'K', 'l', 'm', 'n', 'O', 'P', 'Q',
                      'r', 's', 't', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
                   '+', '=', '/', '\\', '?', '<', '>', '{', '}', '[', ']',
                   '_', ';', ',', '.', '"', "'"]
        choices = [s_alphabet, c_alphabet, numbers, symbols]

        main_probability = random.choice(choices)

        branched_probability = random.choice(main_probability)


menu = tk.OptionMenu(frame, val, *options)
menu.grid(row=0, column=0, columnspan=2)

circle = tk.PhotoImage(file="gimp-button.png")
commit = tk.Button(frame, image=circle, width=25, height=25, command=check)
commit.grid(row=1, column=0, columnspan=2)

root.mainloop()

# todo make the password generated made of 16 characters
