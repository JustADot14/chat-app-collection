# Start Date: 3/9/2021
# Last Updated: 3/9/2021
# Author: Lucifer 14
# App Name: Chat App (Multi Client)
# Version: GUI Version 1.0
# Type: Server, Client

# import multiple_chat_app_server as mcas
# import multiple_chat_app_client as mcac
import os, sys
import tkinter
from tkinter import Label, ttk

def requirement_check(): 
    if not os.path.exists('database') :
        os.makedirs('database')

class MenuBar(tkinter.Menu):
    def __init__(self, ws):
        tkinter.Menu.__init__(self, ws)

        connnectionmenu = tkinter.Menu(self, tearoff=False)
        connnectionmenu.add_command(label="New Connection", command=self.donothing, accelerator="Ctrl+N")
        self.bind_all('<Control-n>', self.donothing)
        connnectionmenu.add_command(label="Open Connection", command=self.donothing, accelerator="Ctrl+O")
        self.bind_all('<Control-o>', self.donothing)
        connnectionmenu.add_command(label="Close Connection", underline=1, command=self.donothing, accelerator="Ctrl+Q")
        self.bind_all('<Control-q>', self.donothing)
        connnectionmenu.add_separator()

        connnectionmenu.add_command(label="Exit", accelerator="Alt+F4", command=self.exit)
        self.bind_all('<Alt-F4>', self.exit)
        self.add_cascade(label="Connection", menu=connnectionmenu)
        
        
        helpmenu = tkinter.Menu(self, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        self.add_cascade(label="Help", menu=helpmenu)
    
    def donothing(self, event):
        print('hi')

    def exit(self, event):
        sys.exit()


class MainInterface(tkinter.Frame):
    def __init__(self):
        tkinter.Frame.__init__(self)
        # self.config(width="500px", height="400px", bg="red")
        label = tkinter.Label(self, text='hilkjfa asd jkaljkjakjd jaisdjsajfkj\nafdalkj l\n', bg="#000000")
        label.pack()
        


class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Simple Chat App")
        self.geometry('500x400')
        menubar = MenuBar(self)
        #container = tkinter.Frame(self, width="500px", height="400px", bg="red")
        #container.pack()
        frame = MainInterface()
        frame.pack()
        self.config(menu=menubar)


# def gui_draw():


#     main_frame = tkinter.Frame(root, width="500px", height="400px", bg="")
#     main_frame.pack()
#     btn = tkinter.Button(root, text="Hi", width=6)
#     btn.place(x=10, y=100)
#     root.config(menu=menubar)
#     root.resizable(0,0)
#     root.mainloop()

if __name__ == "__main__":
    address = "127.0.0.1"       # change server IP, don't forget to change in client
    port = 4444                 # change port number, don't forget to change in client
    username = "User"           # change Username
    
    requirement_check()
    app = App()
    app.mainloop()
    # gui_draw()
    
