import json
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def pw_list():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(letters) for _ in range(nr_symbols)]
    password_numbers = [random.choice(letters) for _ in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)

    password = "" .join(password_list)


    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def file_save():

    website = website_entry.get()
    emails = email_entry.get()
    passwords = password_entry.get()
    new_data = {
        website: {
            "email": emails,
            "password": passwords,
        }
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.askretrycancel(title="You have left it open", message="lmao bro")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered :\n "
                                                              f"{email_entry.get()}"
                                                              f"\nPassword: {password_entry.get()}\n "
                                                              f"Is it okay to save?")

        if is_ok == True:
            with open("passwords.json", mode="r") as files:
                data = json.load(files)
                data.update(new_data)
            with open("passwords.json", mode="w") as files:
                json.dump(data, files, indent=4)












# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
logo = PhotoImage(file= "logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,112, image= logo)
canvas.grid(column=2, row=1)


## labels
website_label =  Label(text="Website")
website_label.grid(row=2, column=1)
email = Label(text="Emain/Username")
email.grid(row=3, column=1)
password = Label(text="Password")
password.grid(row=4, column=1)

## entry boxes

website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "sparkrayburn@gmail.com")
email_entry.grid(row=3, column=2, columnspan=2)
password_entry = Entry(width=17)

password_entry.grid(row=4, column=2)


##button

def add_func():
    file_save()
    website_entry.delete(0, END)
    password_entry.delete(0, END)


generate_button = Button(text="Generate Password", command=pw_list)
generate_button.grid(row=4, column=3)
add_button = Button(text="Add",width=36, command=add_func)
add_button.grid(row=5 ,column=2, columnspan=2)






















window.mainloop()















