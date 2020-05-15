from tkinter import *
import func


class Register():
    def __init__(self, master, button=None, backGroundColor="Black", textColor="#12ff51", eBColor="#1c1c1c", errorColor="#fa2525",
                 entryButtonBackgroundColor="#1c1c1c"):
        self.master = master
        self.button = button
        self.button.configure(state="disabled")
        self.backGroundColor = backGroundColor
        self.textColor = textColor
        self.errorColor = errorColor
        self.entryButtonBackgroundColor = entryButtonBackgroundColor

        # newAccount Window Configs
        self.registerWindow = Toplevel(master)
        self.registerWindow.title("Register")
        self.registerWindow.configure(bg=self.backGroundColor, width=500, height=300)
        self.registerWindow.resizable(0, 0)

        # Entries, Labels, & Buttons
        self.accountUsernameEntry = Entry(self.registerWindow, width=50, bg=self.entryButtonBackgroundColor,
                                          fg=self.textColor)
        self.accountPasswordEntry = Entry(self.registerWindow, width=50, bg=self.entryButtonBackgroundColor,
                                          fg=self.textColor)
        self.accountUsernameLabel = Label(self.registerWindow, text="username:", fg=self.textColor,
                                          bg=self.backGroundColor)
        self.accountPasswordLabel = Label(self.registerWindow, text="password:", fg=self.textColor,
                                          bg=self.backGroundColor)
        self.accountInfoLabel = Label(self.registerWindow,
                                      text="Enter a username & password below. Click submit and log in!",
                                      fg=self.textColor, bg=self.backGroundColor)
        self.accountSubmitButton = Button(self.registerWindow, text="Submit", fg=self.textColor,
                                          bg=self.backGroundColor,
                                          command=lambda: func.add_acount(self.registerWindow,
                                                                          self.accountUsernameEntry.get(),
                                                                          self.accountPasswordEntry.get()))
        # Enable placements
        self.accountInfoLabel.place(x=0, y=0)
        self.accountUsernameLabel.place(x=0, y=25)
        self.accountPasswordLabel.place(x=0, y=45)
        self.accountSubmitButton.place(x=5, y=70)
        self.accountUsernameEntry.place(x=58, y=25)
        self.accountPasswordEntry.place(x=58, y=45)