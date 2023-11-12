# JSON Notes
# json.dump() - write
# json.load() - read
# json.update() - update

from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    password = random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    pw_entry.insert(0,password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    website = web_entry.get()
    email = email_entry.get()
    password = pw_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't forget to enter info")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} n\Password: {password} ")

        if is_ok:
            try:
                with open("password.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("password.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)

                with open("password.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                web_entry.delete(0, END)
                # email_entry.delete()
                pw_entry.delete(0, END)

# Search Function

def search():
    website_entry = web_entry.get()
    if len(website_entry) == 0:
        messagebox.showinfo(title="Oops", message="Don't forget to enter info")

    else:

        try:
            with open("password.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No passwords saved yet")
        else:
            try:
                website = data[website_entry]
            except KeyError:
                messagebox.showinfo(title="Oops", message="Website not found")
            else:
                email = website['email']
                password = website['password']
                is_ok = messagebox.askokcancel(title=website_entry,
                                               message=f"Email: {email} n\Password: {password} ")
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", fg="black", highlightthickness=0, bg="white", font=("Arial", 12, "normal"))
website_label.grid(column=0, row=1)

web_entry = Entry(width=21, highlightthickness=0, fg="black", bg="white")
web_entry.grid(column=1, row=1)
web_entry.focus()

search_button = Button(width=14, text="Search", highlightthickness=0, bg="white", highlightbackground="white", command=search)
search_button.grid(column=2, row=1, sticky="w")

email_label = Label(text="Email/Password:", fg="black", highlightthickness=0, bg="white", font=("Arial", 12, "normal"))
email_label.grid(column=0, row=2)

email_entry = Entry(width=35, highlightthickness=0, bg="white")
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "mckeown.james@gmail.com")

password_label = Label(text="Password:", fg="black", highlightthickness=0, bg="white", font=("Arial", 12, "normal"))
password_label.grid(column=0, row=3)

pw_entry = Entry(width=18, highlightthickness=0, bg="white")
pw_entry.grid(column=1, row=3)

pw_button = Button(width=14, text="Generate Password", highlightthickness=0, bg="white", highlightbackground="white", command=generate_password)
pw_button.grid(column=2, row=3, sticky="w")

add_button = Button(width=30, text="Add", highlightthickness=0, bg="white", highlightbackground="white",
                    command=save_pw)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
