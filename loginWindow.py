from tkinter import *
import func
import registerWindow


class loginWindow():
    def __init__(self, master, backGroundColor="Black", textColor="#12ff51", eBColor="#1c1c1c", errorColor="#fa2525",
                 entryButtonBackgroundColor="#1c1c1c"):
        self.master = master
        self.backgroundColor = backGroundColor
        self.textColor = textColor
        self.eBColor = eBColor
        self.errorColor = errorColor
        self.entryButtonBackgroundColor = entryButtonBackgroundColor
        master.title("Login Window")
        master.configure(bg=backGroundColor, width=500, height=400)
        master.resizable(0, 0)

        # Frames
        self.frame = Frame(master, bg=entryButtonBackgroundColor)

        # Labels
        self.welcomeLabel = Label(master, text="Welcome to your favorite things!", fg=errorColor, bg=backGroundColor)
        self.usernameLabel = Label(master, text="username:", fg=textColor, bg=backGroundColor)
        self.passwordLabel = Label(master, text="password:", fg=textColor, bg=backGroundColor)
        self.haveAccount = Label(master, text="You must have an account to continue." +
                        "\nIf you do enter the information below", fg=textColor, bg=backGroundColor, justify="left")
        self.infoLabel = Label(self.frame, text="Information:", fg=textColor, bg=entryButtonBackgroundColor)
        self.accidentCloseLabel = Label(master, text="If you accidentally close the register"
                                                     "\nwindow. Please restart the program.",
                                        fg=entryButtonBackgroundColor, bg=backGroundColor, justify="left")
        self.dontWantToRegisterLabel = Label(master, fg=entryButtonBackgroundColor, bg=backGroundColor,
                                             text="If you don't want to make an account. You can use... " +
                                                  "\nusername: user ; password: pass", justify="left")

        # Buttons
        self.unregistedButton = Button(text="Not registed? Click Here", fg=textColor, bg=entryButtonBackgroundColor,
                                       command=lambda: registerWindow.Register(master=master,
                                                                               button=self.unregistedButton))
        self.checkVerificationButton = Button(text="Submit", bg=entryButtonBackgroundColor, fg=textColor,
                                              command=lambda: func.verify_username_and_password(
                                                  self.usernameEntry.get(), self.passwordEntry.get(), master))
        self.helpButton = Button(self.frame, text="Help", fg=textColor, bg=entryButtonBackgroundColor,
                                 command=func.help_message)
        self.copyrightButton = Button(self.frame, text="Copyright", fg=textColor, bg=entryButtonBackgroundColor,
                                      command=func.copyright_message)

        # Entries
        self.usernameEntry = Entry(master, width=50, bg=entryButtonBackgroundColor, fg=textColor)
        self.passwordEntry = Entry(master, width=50, bg=entryButtonBackgroundColor, fg=textColor, show="*")

        # Entry Inserts
        self.usernameEntry.insert(0, "cAsE-SeNsItiVe")
        self.passwordEntry.insert(0, "cAsE-SeNsItiVe")

        # Enable Everything
        self.welcomeLabel.place(x=300 / 2, y=0)
        self.haveAccount.place(x=0, y=30)
        self.usernameLabel.place(x=0, y=70)
        self.usernameEntry.place(x=58, y=70)
        self.passwordLabel.place(x=0, y=90)
        self.passwordEntry.place(x=58, y=90)
        self.checkVerificationButton.place(x=5, y=115)
        self.dontWantToRegisterLabel.place(x=55, y=115)
        self.accidentCloseLabel.place(x=0, y=330)
        self.unregistedButton.place(x=0, y=370)
        self.frame.place(x=402, y=354)
        self.infoLabel.pack(side="top")
        self.copyrightButton.pack(side="right")
        self.helpButton.pack(side="left")
