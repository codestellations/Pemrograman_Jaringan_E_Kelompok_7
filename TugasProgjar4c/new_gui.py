import tkinter as tk
import os
from chat_client import ChatClient
import json

root = tk.Tk()
chatClient = ChatClient()

#users = ["Messi", "Arman", "Lana", "Kiko"]
users = []
groups = []

auth = ""

class functions:
    def __init__(self, root=None, ui=None):
        self.root = root
        # self.ui = interfaces(root)

    def login(self, ui, frame, uname, pw):
        # auth function
        username = uname.get()
        password = pw.get()

        cmd = str(f"auth {uname.get()} {pw.get()}")
        result = chatClient.proses(cmd)
        result.split()
        if result[0]=='E':
            print("Wrong username or password")
        else:
            print("auth by " + username + " with password " + password)
            # get all users
            frame.destroy()
            ui.chat(username)

    def sendfile(self):
        #send file function
        print("sending file")

    def sendtext(self, ui, chatbox, box, auth, user):
        #send text function
        input = chatbox.get("1.0", "end-1c")
        print(input)

        cmd = str(f"send {user} {input}")
        result = chatClient.proses(cmd)
        result.split()
        if result[0] == 'E':
            print("Chat failed to send")
        else:
            print("Chat sent!")
            ui.chatbubble(input, auth, box)

        chatbox.delete("1.0", "end-1c")

    def inbox(self, ui, chatbox, box, auth, user):
        cmd = str(f"inbox")
        result = chatClient.proses(cmd)
        if result[0] == 'E':
            print("Failed to get chat")
        else:
            print("Refresh chat!")
            result = json.loads(result)
            if auth in result:
                result.update(result)
            else:
                result = result

            for sender in result:
                if(str(sender) == user):
                    for i in result[sender]:
                        input = i['msg']
                        ui.chatbubble(input, user, box)

        chatbox.delete("1.0", "end-1c")

class interfaces:
    def __init__(self, master=None, app=None, root=None):
        self.func = functions(root)
        self.root = root
        self.landing()
        # self.chat(func, auth)

    def landing(self):
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
                                fg="#22223b", bg="#9a8c98",
                                command=lambda: self.func.login(self, frame, usernameform, passwordform))
        loginbutton.pack(side=tk.BOTTOM, anchor=tk.S, pady=20)

    def chat(self, auth):
        # canvas = tk.Canvas(root, height=700, width=1000, bg="#22223b")
        # canvas.pack()

        # base frame
        frame = tk.Frame(root, bg="#4A4E69")
        frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        # left frame
        leftframe = tk.Frame(frame, height=100, width=250, bg="#9a8c98")
        leftframe.pack(side=tk.LEFT, anchor=tk.N, fill=tk.Y)

        logintext = tk.Label(leftframe, text=("Welcome, " + auth), font=("Poppins Medium", 18),
                             bg="#9a8c98", fg="#f2e9e4")
        logintext.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

        # group frame
        groupframe = tk.LabelFrame(leftframe, height=200, width=250,
                                   text="Group chat", bg="#c9ada7")

        # new group button
        newgroup = tk.Button(leftframe, text="New Group", padx=5, font=("Poppins", 10),
                             fg="#22223b", bg="#9a8c98", command=lambda: self.grouptoggle(groupframe))
        newgroup.pack(side=tk.BOTTOM, anchor=tk.S, pady=5)

        # right frame
        self.rightframe = tk.Frame(frame, height=100, width=150, bg="#4a4e69")
        self.rightframe.pack(side=tk.LEFT, anchor=tk.N, fill=tk.BOTH, expand=True)

        self.users = self.singlechat(leftframe, auth)
        self.newgroup(groupframe)

    def singlechat(self, frame, auth):
        userbutton = []
        userchat = []

        users = chatClient.proses("getallusers")
        users = json.loads(users)
        # users = [*users]
        print(users)

        for x in range(len(users)):
            # userchat.append(tk.Frame(self.rightframe, height=100, width=150, bg="#4A4E69"))
            # userchat[x].pack(side=tk.LEFT, anchor=tk.N, fill=tk.BOTH, expand=True)
            # userchat[x].pack_forget()

            userbutton.append(tk.Button(frame, text=users[x], anchor='w',
                                        command=lambda y=users[x]: self.personalchat(y, auth)))
                                        # command=lambda y=users[x], z=userchat[x]: self.personalchat(y, z, auth)))
            userbutton[x].pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, padx=10, pady=5)

        return users

    def personalchat(self, user, auth):
        print("pc dengan ", user)

        content = ["Halo lagi apa?", "Udah makan belum?", "Mau minta saran dong",
                   "Saran apa", "Makan mi goreng apa rebus ya?"]
        sender = [user, user, user, auth, user]

        self.changechat()

        logintext = tk.Label(self.rightframe, text=user, font=("Poppins Medium", 14),
                             bg="#4A4E69", fg="#f2e9e4")
        logintext.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

        # new chat
        chatframe = tk.Text(self.rightframe, state="disabled", bg="#4A4E69", fg="#f2e9e4",
                            padx=5, pady=5, font=("Inconsolata", 11))
        chatframe.place(x=5, y=55, width=545, height=400)

        # for existing messages
        for x in range(len(content)):
            self.chatbubble(content[x], sender[x], chatframe)

        # button frame
        buttonframe = tk.Frame(self.rightframe, height=20, width=100)
        buttonframe.pack(side=tk.RIGHT, anchor=tk.SW)

        # chat box
        boxframe = tk.Frame(self.rightframe, height=100, bg="#F2E9E4")
        boxframe.pack(side=tk.BOTTOM, anchor=tk.S, fill=tk.X, expand=True)

        chatbox = tk.Text(boxframe)
        chatbox.place(x=5, y=5, width=455, height=90)

        # send text
        filebutton = tk.Button(buttonframe, text="Send", padx=22, pady=5, font=("Poppins", 10),
                                fg="#22223b", bg="#9a8c98", command=lambda: self.func.sendtext(self, chatbox, chatframe, auth, user))
        filebutton.pack(side=tk.TOP, anchor=tk.SW)

        # send file
        filebutton = tk.Button(buttonframe, text="Send File", padx=10, pady=5, font=("Poppins", 10),
                                fg="#22223b", bg="#9a8c98", command=lambda: self.func.sendfile())
        filebutton.pack(side=tk.TOP, anchor=tk.SW)

        # refresh
        filebutton = tk.Button(buttonframe, text="Refresh Chat", padx=0, pady=5, font=("Poppins", 10),
                               fg="#22223b", bg="#9a8c98", command=lambda: func.inbox(self, chatbox, chatframe, auth, user))
        filebutton.pack(side=tk.TOP, anchor=tk.SW)

    def chatbubble(self, content, name, box):
        if not content.isspace() and content.strip() != '':
            box.configure(state="normal")

            textchat = (name + " : " + content + os.linesep)

            box.insert("end", textchat)

            box.configure(state="disable")

    def changechat(self):
        print(self.rightframe)
        self.rightframe.pack_forget()
        self.rightframe.pack(side=tk.LEFT, anchor=tk.N, fill=tk.BOTH, expand=True)
        self.rightframe.tkraise()

    def newgroup(self, groupframe):
        userlist = []
        self.var = []

        print(self.users)

        groupframe.pack(side=tk.BOTTOM, anchor=tk.SW, fill=tk.X)

        for x in range(len(self.users)):
            self.var.append(tk.IntVar())
            userlist.append(tk.Checkbutton(groupframe, text=self.users[x], variable=self.var[x],
                                           onvalue=1, offvalue=0, bg="#c9ada7"))
            userlist[x].pack(anchor=tk.W)

        create = tk.Button(groupframe, text="Create Group", padx=5, font=("Poppins", 10),
                             fg="#22223b", bg="#9a8c98", command=lambda: self.groupchat(groupframe))
        create.pack(side=tk.BOTTOM, anchor=tk.S, pady=5)

        groupframe.pack_forget()

    def grouptoggle(self, groupframe):
        groupframe.pack(side=tk.BOTTOM, anchor=tk.SW, fill=tk.X)

    def groupchat(self, groupframe):
        temp = []

        for x in range(len(self.var)):
            if(self.var[x].get() == 1):
                temp.append(self.users[x])

        groups.append(temp)
        print(groups)

        print("group chat with ", temp)

        groupframe.pack_forget()

if __name__=="__main__":
    root.title("Chat App")
    app = interfaces(root)
    root.mainloop()
