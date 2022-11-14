import sqlite3
import tkinter as tk

with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(username text primary key, password text);")


def register():
    uname = username.get()
    pword = password.get()
    cursor.execute(f"SELECT COUNT(*) FROM users WHERE username='{uname}';")
    result = cursor.fetchone()
    if int(result[0]) > 0:
        cursor.execute(f"SELECT password FROM users WHERE username='{uname}';")
        pass_in_db = cursor.fetchone()
        if pass_in_db[0] == pword:
            message_box["text"] = "You Are Logged In"
        else:
            message_box["text"] = "Wrong Password"
    else:
        cursor.execute(f"INSERT INTO users(username, password) values('{uname}','{pword}');")
        message_box["text"] = "User Added"
    db.commit()


screen = tk.Tk()
screen.geometry("500x500-0-0")
screen.title("Pranav | Login")
heading = tk.Label(screen, text="Login/Register Page")
username = tk.Entry(screen)
password = tk.Entry(screen)
register_btn = tk.Button(screen, text="Register/Login", command=register)
message_box = tk.Label(screen, text="")

heading.pack()
username.pack()
password.pack()
register_btn.pack()
message_box.pack()
screen.mainloop()
