import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

users = ["Messi", "Arman", "Lana", "Kiko"]

auth = "Selena"

def login(frame):

    # auth function

    frame.destroy()

    chat()

def chat():

    # canvas = tk.Canvas(root, height=700, width=1000, bg="#22223b")
    # canvas.pack()

    # base frame
    frame = tk.Frame(root, bg="#4A4E69")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    # left frame
    leftframe = tk.Frame(frame, height=100, width=250, bg="#9a8c98")
    leftframe.pack(side=tk.LEFT, anchor=tk.N, fill=tk.Y)

    logintext = tk.Label(leftframe, text=auth, font=("Poppins Medium", 18),
                         bg="#9a8c98", fg="#f2e9e4")
    logintext.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

    # group frame
    groupframe = tk.LabelFrame(leftframe, height=200, width=250,
                               text="Group chat", bg="#c9ada7")
    groupframe.pack(side=tk.BOTTOM, anchor=tk.SW)

    # right frame
    rightframe = tk.Frame(frame, height=100, width=150, bg="#4a4e69")
    rightframe.pack(side=tk.LEFT, anchor=tk.N, fill=tk.BOTH, expand=True)

    singlechat(leftframe, rightframe)

def singlechat(frame, rightframe):

    userbutton = []

    for x in range(len(users)):
        userbutton.append(tk.Button(frame, text=users[x], anchor='w',
                                    command=lambda y=users[x]: personalchat(y, rightframe)))
        userbutton[x].pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10, pady=5)

def personalchat(user, frame):

    print("pc dengan ", user)

    content = ["Halo lagi apa?", "Udah makan belum?", "Mau minta saran dong",
               "Saran apa", "Makan mi goreng apa rebus ya?"]
    sender = [user, user, user, auth, user]

    rightframe = tk.Frame(frame, height=100, width=150, bg="#4A4E69")
    rightframe.pack(side=tk.LEFT, anchor=tk.N, fill=tk.BOTH, expand=True)

    for x in range(len(content)):
        if (sender[x] == user):
            leftchat(content[x], rightframe)
        elif (sender[x] == auth):
            rightchat(content[x], rightframe)

    # chat box
    # boxframe = tk.Frame(frame, height=100, bg="#F2E9E4")
    # boxframe.pack(side=tk.BOTTOM, anchor=tk.S, fill=tk.X, expand=True)

def leftchat(content, frame):
    text = tk.Label(frame, text=content, font=("Raleway"),
                    bg="#4A4E69", fg="#f2e9e4")
    text.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

def rightchat(content, frame):
    text = tk.Label(frame, text=content, font=("Raleway"),
                    bg="#4A4E69", fg="#f2e9e4")
    text.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=5)

def landing():

    canvas = tk.Canvas(root, height=700, width=1000, bg="#22223b")
    canvas.pack()

    frame = tk.Frame(root, bg="#4A4E69")
    frame.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.25)

    logintext = tk.Label(frame, text="Chat App", font=("Poppins Medium", 36),
                         bg="#4A4E69", fg="#f2e9e4")
    logintext.pack(side=tk.TOP, anchor=tk.N, pady=20)

    # frame form
    formframe = tk.Frame(frame, height=100, width=150)
    formframe.pack(pady=10)

    # label frame
    labelframe = tk.Frame(formframe, height=50)
    labelframe.pack(expand="yes", pady=5)

    # login form
    usernamelabel = tk.Label(labelframe, text="Username", font="Poppins")
    usernamelabel.pack(side=tk.LEFT, anchor=tk.N)
    usernameform = tk.Entry(labelframe, bd=5)
    usernameform.pack(side=tk.RIGHT, fill=tk.X, padx=5, expand=True)

    # password frame
    pwframe = tk.Frame(formframe, height=50)
    pwframe.pack(expand="yes", pady=5)

    # password form
    passwordlabel = tk.Label(pwframe, text="Password", font="Poppins")
    passwordlabel.pack(side=tk.LEFT, anchor=tk.N)
    passwordform = tk.Entry(pwframe, bd=5, show="*")
    passwordform.pack(side=tk.RIGHT, fill=tk.X, padx=5, expand=True)

    # login button
    loginbutton = tk.Button(frame, text="Login", padx=20, pady=5, font="Poppins",
                            fg="#22223b", bg="#9a8c98", command=lambda: login(frame))
    loginbutton.pack(side=tk.BOTTOM, anchor=tk.S, pady=20)

def main():

    root.title("Chat App")

    landing()

    # chat()

    root.mainloop()

if __name__=="__main__":
	main()
