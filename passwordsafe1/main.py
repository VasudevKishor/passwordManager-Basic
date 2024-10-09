import tkinter as tk
from tkinter import messagebox
import pandas as pd


root = tk.Tk()
root.title("User Management System")

tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show='*')  
password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Age").grid(row=3, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Phone").grid(row=4, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=5, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=5, column=1, padx=10, pady=5)


def clear_entries():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def add_user():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if username and password:
        try:
            df = pd.read_csv('data.csv', index_col=0)
        except FileNotFoundError:

            df = pd.DataFrame(columns=["Username", "Password", "Email", "Age", "Phone", "Address"])

        df = df.append({
            "Username": username,
            "Password": password,
            "Email": email,
            "Age": age,
            "Phone": phone,
            "Address": address
        }, ignore_index=True)

        df.to_csv('data.csv')
        messagebox.showinfo("Success", "User added successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Username and password are required.")


def get_user():
    username = username_entry.get()

    if username:
        try:
            df = pd.read_csv('data.csv', index_col=0)
            user_data = df[df["Username"] == username]
            if not user_data.empty:
                user_info = user_data.iloc[0]  
                messagebox.showinfo("User Details", 
                    f"Username: {user_info['Username']}\n"
                    f"Password: {user_info['Password']}\n"
                    f"Email: {user_info['Email']}\n"
                    f"Age: {user_info['Age']}\n"
                    f"Phone: {user_info['Phone']}\n"
                    f"Address: {user_info['Address']}")
            else:
                messagebox.showerror("Error", "User not found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")
    else:
        messagebox.showerror("Error", "Username is required.")


def delete_user():
    username = username_entry.get()

    if username:
        try:
            df = pd.read_csv('data.csv', index_col=0)
            if username in df["Username"].values:
                df = df[df["Username"] != username]
                df.to_csv('data.csv')  
                messagebox.showinfo("Success", "User deleted successfully.")
                clear_entries()
            else:
                messagebox.showerror("Error", "User not found.")
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found.")
    else:
        messagebox.showerror("Error", "Username is required.")

tk.Button(root, text="Add User", command=add_user).grid(row=6, column=0, padx=10, pady=10)
tk.Button(root, text="Get User", command=get_user).grid(row=6, column=1, padx=10, pady=10)
tk.Button(root, text="Delete User", command=delete_user).grid(row=6, column=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
