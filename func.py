from tkinter import messagebox
import mainWindow
import os

def add_acount(win, user, passw):
    fileDir = os.getcwd() + "\\user_pass.txt"
    # fileDir = os.path.dirname(os.path.realpath(__file__)) + "\\user_pass.txt"
    if (len(user) != 0 or len(passw) != 0):
        try:
            with open(fileDir, 'a+') as file_user_pass:
                file_user_pass.write(f"{user}:{passw}\n")
                win.destroy()
        except Exception:
            pass
    else:
        messagebox.showerror("Error", "You didn't put a username or password")


def verify_username_and_password(user, passw, master):
    fileDir = os.getcwd() + "\\user_pass.txt"
    # fileDir = os.path.dirname(os.path.realpath(__file__)) + "\\user_pass.txt"
    try:
        with open(fileDir, 'r') as file_user_pass:
            line = file_user_pass.readline().strip("\n").split(":")
            accountFound = False
            while line != ['']:
                if (user == line[0]) and (passw == line[1]):
                    master.destroy()
                    mainWindow.mainWindow()
                    accountFound = True
                line = file_user_pass.readline().strip("\n").split(":")
            if not accountFound:
                messagebox.showinfo("Status", "Account not found! Try another!")
    except FileNotFoundError:
        messagebox.showinfo("No Accounts", "It seems like there is no accounts. Please make an account.")


def help_message():
    messagebox.showinfo("Help", "\n1. Login into your account. If you have one, if not, please register."
                                "\n2. After logging in you can select your favorite items"
                                "\n3. After selecting your items you can close the program. The items selected will not"
                                " be saved, so you have to redo them after relogging. Your username & password are "
                                "saved.")


def copyright_message():
    messagebox.showwarning("Copyrights", "There is no copyrights to this program, but if I \n"
                                         "see you steal it. I will do absolutely do nothing.")

def selection(master, cP, item):
    if item == 1:
        textColor = "#fa2525"
        mainWindow.mainWindow(textColor=textColor)
        cP.destroy()
        master.destroy()
    elif item == 2:
        textColor = "#12ff51"
        mainWindow.mainWindow(textColor=textColor)
        cP.destroy()
        master.destroy()
    elif item == 3:
        textColor = "#faec25"
        mainWindow.mainWindow(textColor=textColor)
        cP.destroy()
        master.destroy()
    else:
        textColor = "#17e5fc"
        mainWindow.mainWindow(textColor=textColor)
        cP.destroy()
        master.destroy()


def getColor(master, win, textcolor, item=None):
    mainWindow.mainWindow.userInfo['favColor'] = item
    mainWindow.mainWindow(textColor=textcolor)
    win.destroy()
    master.destroy()