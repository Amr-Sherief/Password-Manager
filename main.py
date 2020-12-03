import tkinter as tk
import mysql.connector
import random

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='19371937A',
    database='password'

)

cursor = mydb.cursor()

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Password Manager")

val = tk.StringVar()

value = val.get()

frame = tk.Frame(root)
frame.pack(side='top')

options = ["Add Login", "Show Logins", "Generate Password"]


def sequel():
    global done

    e_label.destroy()
    email.destroy()
    p_label.destroy()
    password.destroy()
    submit.destroy()

    insert_code = 'INSERT INTO passwords (email, pass) VALUES ("{}", "{")'
    insert_code = insert_code.format(email.get(), password.get())
    cursor.execute(insert_code)

    done = tk.Label(frame, text="Done!", fg='red')
    done.grid(row=6, column=0, columnspan=2)


def check():
    global e_label
    global email
    global p_label
    global password
    global submit
    global last_password_entry

    try:
        e_label.destroy()
    except:
        print("======================================================================================")

    try:
        email.destroy()
    except:
        print("======================================================================================")
    try:
        p_label.destroy()
    except:
        print("======================================================================================")

    try:
        password.destroy()
    except:
        print("======================================================================================")

    try:
        submit.destroy()
    except:
        print('======================================================================================')

    try:
        last_password_entry.destroy()
    except:
        print("======================================================================================")

    try:
        done.destroy()
    except:
        print("======================================================================================")

    if val.get() == options[0]:

        e_label = tk.Label(frame, text="Email")
        email = tk.Entry(frame)
        p_label = tk.Label(frame, text="Password")
        password = tk.Entry(frame)
        submit = tk.Button(frame, text="Submit", fg="red", command=sequel)

        e_label.grid(row=3, column=0, sticky='W')
        email.grid(row=3, column=1)
        p_label.grid(row=4, column=0, sticky='W')
        password.grid(row=4, column=1)
        submit.grid(row=5, column=0, columnspan=2)

    if val.get() == options[1]:

        return

    if val.get() == options[2]:


        s_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                      'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        c_alphabet = ['A', 'B', 'C', 'd', 'E', 'F', 'G', 'H',
                      'I', 'J', 'K', 'l', 'm', 'n', 'O', 'P', 'Q',
                      'r', 's', 't', 'U', 'V', 'W', 'X', 'Y', 'Z']

        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-',
                   '+', '=', '?']

        choices = [s_alphabet, c_alphabet, numbers, symbols]
        last_password = ''

        s_alphabet_num = 0
        c_alphabet_num = 0
        numbers_num = 0
        symbols_num = 0

        while True:
            for i in range(16):

                if i == 0:

                    main_probability = random.choice(choices)

                    branched_probability = random.choice(main_probability)
                    last_password += str(branched_probability)

                    if branched_probability in s_alphabet:
                        s_alphabet_num += 1
                    if branched_probability in c_alphabet:
                        c_alphabet_num += 1
                    if branched_probability in numbers:
                        numbers_num += 1
                    if branched_probability in symbols:
                        symbols_num += 1
                        break

                min_list = [s_alphabet_num, c_alphabet_num, numbers_num, symbols_num]
                min_num = min(min_list)
                if s_alphabet_num == min_num:
                    branched_probability = random.choice(s_alphabet)
                elif c_alphabet_num == min_num:
                    branched_probability = random.choice(c_alphabet)
                elif numbers_num == min_num:
                    branched_probability = random.choice(numbers)
                elif symbols_num == min_num:
                    branched_probability = random.choice(symbols)

                if str(branched_probability) in s_alphabet:
                    s_alphabet_num += 1
                elif str(branched_probability) in c_alphabet:
                    c_alphabet_num += 1
                elif branched_probability in numbers:
                    numbers_num += 1
                elif str(branched_probability) in symbols:
                    symbols_num += 1
                last_password += str(branched_probability)

            else:
                last_password_entry = tk.Label(frame, text=last_password)
                last_password_entry.grid(row=3, column=0)
                return


menu = tk.OptionMenu(frame, val, *options)
menu.grid(row=0, column=0, columnspan=2)

circle = tk.PhotoImage(file="gimp-button.png")
commit = tk.Button(frame, image=circle, width=25, height=25, command=check)
commit.grid(row=1, column=0, columnspan=2)

root.mainloop()

mydb.commit()
