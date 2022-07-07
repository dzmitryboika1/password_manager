from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get().upper()
    password = password_input.get()
    user = username_input.get()

    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    if not website or not password:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't leave any fields empty!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are details entered:\nUser:{user}\n"
                    f"Password: {password}\nIs it OK to save?"
        )
        if is_ok:
            try:
                with open("data_password.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data_password.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data_password.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- SEARCHING ------------------------------- #

def search():
    search_button.config(bg="SteelBlue")
    searching_website = website_input.get().upper()
    try:
        with open("data_password.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Password data file isn't exist yet!")
    else:
        if searching_website in data:
            searching_email = data[searching_website]["email"]
            searching_password = data[searching_website]["password"]
            messagebox.showinfo(
                title=searching_website,
                message=f"Email: {searching_email}\nPassword: {searching_password}"
            )
        else:
            messagebox.showinfo(
                title="Oops",
                message=f"There are no any info about:\n"f"Website:{searching_website}"
            )
    finally:
        search_button.config(bg="SteelBlue")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10)

canvas = Canvas(width=200, height=200)
pwd_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pwd_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2, sticky="e")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")

# entries
website_input = Entry(width=24)
website_input.grid(column=1, row=1, sticky="w")

username_input = Entry(width=44)
username_input.grid(column=1, row=2, columnspan=2, sticky="w")
username_input.insert(0, "dzmitryboika1@gmail.com")

password_input = Entry(width=24)

password_input.grid(column=1, row=3, sticky="w")

# buttons
generate_password_button = Button(text="Generate Password", width=16, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w")

search_button = Button(text="Search", width=16, command=search)
search_button.grid(column=2, row=1, sticky="w")

add_button = Button(text="Add", width=41, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
