import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError

        use_special_chars = special_chars_var.get()
        use_digits = digits_var.get()
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()

        if not (use_special_chars or use_digits or use_uppercase or use_lowercase):
            messagebox.showerror("Error", "At least one character type must be selected.")
            return

        char_pools = []
        if use_special_chars:
            char_pools.append(string.punctuation)
        if use_digits:
            char_pools.append(string.digits)
        if use_uppercase:
            char_pools.append(string.ascii_uppercase)
        if use_lowercase:
            char_pools.append(string.ascii_lowercase)

        all_chars = ''.join(char_pools)
        password = ''.join(random.choice(all_chars) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")


def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")


app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")

tk.Label(app, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)

options_frame = tk.Frame(app)
options_frame.pack(pady=10)

special_chars_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Special Characters", variable=special_chars_var).grid(row=0, column=0, padx=5)
tk.Checkbutton(options_frame, text="Digits", variable=digits_var).grid(row=0, column=1, padx=5)
tk.Checkbutton(options_frame, text="Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, padx=5)
tk.Checkbutton(options_frame, text="Lowercase Letters", variable=lowercase_var).grid(row=1, column=1, padx=5)

tk.Label(app, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(app, width=40)
password_entry.pack(pady=5)

buttons_frame = tk.Frame(app)
buttons_frame.pack(pady=10)

tk.Button(buttons_frame, text="Generate Password", command=generate_password).grid(row=0, column=0, padx=5)
tk.Button(buttons_frame, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=0, column=1, padx=5)

app.mainloop()
