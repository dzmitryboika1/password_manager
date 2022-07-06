from tkinter import *
from tkinter import messagebox
import random
import pyperclip


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
    website = website_input.get()
    password = password_input.get()
    user = username_input.get()

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
            with open("data_password.txt", mode="a") as data:
                data.write(f"{website} | {user} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


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
website_input = Entry(width=44)
website_input.grid(column=1, row=1, columnspan=2, sticky="w")

username_input = Entry(width=44)
username_input.grid(column=1, row=2, columnspan=2, sticky="w")
username_input.insert(0, "dzmitryboika1@gmail.com")

password_input = Entry(width=24)

password_input.grid(column=1, row=3, sticky="w")

# buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=41, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
