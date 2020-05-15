from tkinter import *
from tkinter.ttk import Combobox
import func


class mainWindow:
    userInfo = {
        "favColor": "",
        "ageGroup": "",
        "favFood": "",
        "favSport": ""
    }
    def __init__(self, backGroundColor="Black", textColor="#12ff51", eBColor="#1c1c1c", errorColor="#fa2525",
                 entryButtonBackgroundColor="#1c1c1c"):
        self.backgroundColor = backGroundColor
        self.textColor = textColor
        self.eBColor = eBColor
        self.errorColor = errorColor
        self.entryButtonBackgroundColor = entryButtonBackgroundColor

        self.master = Tk()
        self.master.title("Main Window")
        self.master.configure(bg=backGroundColor, width=500, height=400)
        self.master.resizable(0, 0)

        # Labels
        self.changeTextColorLabel = Label(self.master, text="Options:",
                                          fg=textColor, bg=backGroundColor)
        self.chooseFavColorLabel = Label(self.master, text="Choose Your Favorite Color:", fg=textColor,
                                         bg=backGroundColor)
        self.favColorLabel = Label(self.master, text=f"Favorite Color: {mainWindow.userInfo.get('favColor')}",
                                   bg=backGroundColor, fg=textColor)
        self.ageGroupLabel = Label(self.master, text=f"Age Group: {mainWindow.userInfo.get('ageGroup')}",
                                   bg=backGroundColor, fg=textColor)
        self.favFoodLabel1 = Label(self.master, text=f"Favorite Food: {mainWindow.userInfo.get('favFood')}",
                                   bg=backGroundColor, fg=textColor)

        self.favSportLabel1 = Label(self.master, text=f"Favorite Sport: {mainWindow.userInfo.get('favSport')}",
                                    bg=backGroundColor, fg=textColor)
        self.choseAgeLabel = Label(self.master, text="Choose your age group:", fg=textColor, bg=backGroundColor)
        self.favFoodLabel = Label(self.master, text="Choose your favorite food:", fg=textColor, bg=backGroundColor)
        self.faveSportLabel = Label(self.master, text="Choose your favorite Sport:", fg=textColor, bg=backGroundColor)

        # Buttons
        self.changeTextColorButton = Button(self.master, text="Change Text Color", fg=textColor, bg=backGroundColor,
                                            command=lambda: ChangeColorWindow(self.master,
                                                                              button=self.changeTextColorButton))
        self.chooseFavColorButton = Button(self.master, text="Choose", fg=textColor, bg=backGroundColor,
                                           command=lambda: chooseYourFavoriteColor(textColor=textColor,
                                                                                   master=self.master,
                                                                                   button=self.chooseFavColorButton))
        self.chooseAgeButton = Button(self.master, text="Choose", fg=textColor, bg=backGroundColor,
                                      command=lambda: chooseAgeWindow(textColor=textColor, master=self.master,
                                                                      button=self.chooseAgeButton))
        self.favFoodButton = Button(self.master, text="Choose", fg=textColor, bg=backGroundColor, command=lambda:
        getYourFavoriteFood(textColor=textColor, master=self.master, button=self.favFoodButton))
        self.faveSportButton = Button(self.master, text="Choose", fg=textColor, bg=backGroundColor, command=lambda:
                                      getYourFavoriteSport(textColor=textColor, master=self.master,
                                                           button=self.favFoodButton))

        # Enable placements
        self.favColorLabel.place(x=300, y=0)
        self.ageGroupLabel.place(x=300, y=20)
        self.favFoodLabel1.place(x=300, y=40)
        self.favSportLabel1.place(x=300, y=60)
        self.changeTextColorLabel.place(x=450, y=357)
        self.changeTextColorButton.place(x=392, y=377)
        self.chooseFavColorLabel.place(x=0, y=20)
        self.chooseFavColorButton.place(x=153, y=19)
        self.choseAgeLabel.place(x=0, y=44)
        self.chooseAgeButton.place(x=153, y=45)
        self.favFoodLabel.place(x=0, y=68)
        self.favFoodButton.place(x=153, y=72)
        self.faveSportLabel.place(x=0, y=91)
        self.faveSportButton.place(x=153, y=98)


class getYourFavoriteSport:
    def __init__(self, master, button=None, backGroundColor="Black", textColor="#12ff51", eBColor="#1c1c1c",
                 errorColor="#fa2525", entryButtonBackgroundColor="#1c1c1c"):
        self.master = master
        self.button = button
        self.button.configure(state="disabled")
        self.backgroundColor = backGroundColor
        self.textColor = textColor
        self.eBColor = eBColor
        self.errorColor = errorColor
        self.entryButtonBackgroundColor = entryButtonBackgroundColor

        self.newWindow = Tk()
        self.newWindow.title("Favorite Sport")
        self.newWindow.configure(bg=backGroundColor)

        # Labels
        self.titleLabel = Label(self.newWindow, text="Choose your favorite sport.", fg=textColor, bg=backGroundColor)

        # CheckBox
        self.titleLabel.pack()

        self.v1 = IntVar(self.newWindow)
        self.v2 = IntVar(self.newWindow)
        self.v3 = IntVar(self.newWindow)
        self.v4 = IntVar(self.newWindow)
        self.v5 = IntVar(self.newWindow)
        self.v6 = IntVar(self.newWindow)

        self.sportCheckBox = Checkbutton(self.newWindow, text="Basketball", fg=textColor, bg=backGroundColor,
                                         variable=self.v1, justify='left')
        self.sportCheckBox.pack()
        self.sportCheckBox = Checkbutton(self.newWindow, text="Baseball", fg=textColor, bg=backGroundColor,
                                         variable=self.v2, justify='left')
        self.sportCheckBox.pack()
        self.sportCheckBox = Checkbutton(self.newWindow, text="Soccer", fg=textColor, bg=backGroundColor,
                                         variable=self.v3, justify='left')
        self.sportCheckBox.pack()
        self.sportCheckBox = Checkbutton(self.newWindow, text="Football", fg=textColor, bg=backGroundColor,
                                         variable=self.v4, justify='left')
        self.sportCheckBox.pack()
        self.sportCheckBox = Checkbutton(self.newWindow, text="Golf", fg=textColor, bg=backGroundColor,
                                         variable=self.v5, justify='left')
        self.sportCheckBox.pack()
        self.sportCheckBox = Checkbutton(self.newWindow, text="Cricket", fg=textColor, bg=backGroundColor,
                                         variable=self.v6, justify='left')
        self.sportCheckBox.pack()
        # Button
        self.submitButton = Button(self.newWindow, text="Submit", fg=textColor, bg=backGroundColor, justify='center',
                                   command=lambda: self.getSport(master=self.master, win=self.newWindow,
                                                                 textcolor=self.textColor))
        self.submitButton.pack()
    def getSport(self, master, win, textcolor):
        mainWindow.userInfo['favSport'] = ""
        if self.v1.get() == 1:
            mainWindow.userInfo['favSport'] += '\nBasketball'
        if self.v2.get() == 1:
            mainWindow.userInfo['favSport'] += '\nBaseball'
        if self.v3.get() == 1:
            mainWindow.userInfo['favSport'] += '\nSoccer'
        if self.v4.get() == 1:
            mainWindow.userInfo['favSport'] += '\nFootball'
        if self.v5.get() == 1:
            mainWindow.userInfo['favSport'] += '\nGolf'
        if self.v6.get() == 1:
            mainWindow.userInfo['favSport'] += '\nCricket'
        mainWindow(textColor=textcolor)
        win.destroy()
        master.destroy()

class getYourFavoriteFood:
    def __init__(self, master, button=None, backGroundColor="Black", textColor="#12ff51", eBColor="#1c1c1c",
                 errorColor="#fa2525", entryButtonBackgroundColor="#1c1c1c"):
        self.master = master
        self.button = button
        self.button.configure(state="disabled")
        self.backgroundColor = backGroundColor
        self.textColor = textColor
        self.eBColor = eBColor
        self.errorColor = errorColor
        self.entryButtonBackgroundColor = entryButtonBackgroundColor

        self.newWindow = Tk()
        self.newWindow.title("Favorite Food")
        self.newWindow.configure(bg=backGroundColor)

        # Labels
        self.titleLabel = Label(self.newWindow, text="Choose your favorite food.", fg=textColor, bg=backGroundColor)

        # Button
        self.submitButton = Button(self.newWindow, text="Submit", fg=textColor, bg=backGroundColor, justify='center',
                                   command=lambda: self.getFood(master=self.master, win=self.newWindow,
                                                                textcolor=self.textColor,
                                                                item=self.comboBox.get()))

        # ComboBox
        self.list_food = ["Burger", "Chicken", "Pizza", "Pork Chops", "Burritos", "Tacos", "Soup", "Hotdogs"]
        self.comboBox = Combobox(self.newWindow, values=self.list_food, width=20)
        self.comboBox.set('Select Food')

        # Enable
        self.titleLabel.pack()
        self.comboBox.pack()
        self.submitButton.pack()

    def getFood(self, master, win, textcolor, item=None):
        for items in self.list_food:
            if item == items:
                mainWindow.userInfo['favFood'] = item
                mainWindow(textColor=textcolor)
                win.destroy()
                master.destroy()


def getAge(master, win, textcolor, item=None):
    if item == 1:
        item = "0 - 5"
    elif item == 2:
        item = "6 - 10"
    elif item == 3:
        item = "11 - 15"
    elif item == 4:
        item = "16 - 20"
    elif item == 5:
        item = "21 - 25"
    elif item == 6:
        item = "26 - 30"
    elif item == 7:
        item = "31 - 35"
    elif item == 8:
        item = ">35"
    mainWindow.userInfo['ageGroup'] = item
    mainWindow(textColor=textcolor)
    win.destroy()
    master.destroy()


class chooseAgeWindow:
    def __init__(self, master, button=None, backGroundColor="Black", textColor="#12ff51", eBColor="#1c1c1c",
                 errorColor="#fa2525", entryButtonBackgroundColor="#1c1c1c"):
        self.master = master
        self.button = button
        self.button.configure(state="disabled")
        self.backGroundColor = backGroundColor
        self.textColor = textColor
        self.ebColor = eBColor
        self.errorColor = errorColor
        self.entryButtonBackgroundColor = entryButtonBackgroundColor

        self.newWindow = Tk()
        self.newWindow.title("Age group")
        self.newWindow.configure(bg=backGroundColor)

        self.s = IntVar()
        self.s.set(1)
        self.ageGroup1 = Radiobutton(self.newWindow, text="0 - 5", fg=textColor, bg=backGroundColor, variable=self.s,
                                     value=1)
        self.ageGroup1.pack()
        self.ageGroup1 = Radiobutton(self.newWindow, text="6 - 10", fg=textColor, bg=backGroundColor, variable=self.s,
                                     value=2)
        self.ageGroup1.pack()
        self.ageGroup1 = Radiobutton(self.newWindow, text="11 - 15", fg=textColor, bg=backGroundColor, variable=self.s,
                                     value=3)
        self.ageGroup1.pack()
        self.ageGroup1 = Radiobutton(self.newWindow, text="16 - 20", fg=textColor, bg=backGroundColor, variable=self.s,
                                     value=4)
        self.ageGroup1.pack()
        self.ageGroup1 = Radiobutton(self.newWindow, text="21 - 25", fg=textColor, bg=backGroundColor, variable=self.s,
                                     value=5)
        self.ageGroup1.pack()
        self.ageGroup1 = Radiobutton(self.newWindow, text="26 - 30", fg=textColor, bg=backGroundColor, variable=self.s,
                                     value=6)
        self.ageGroup1.pack()
        self.ageGroup1 = Radiobutton(self.newWindow, text="31 - 35", fg=textColor, bg=backGroundColor, variable=self.s,
                                     value=7)
        self.ageGroup1.pack()
        self.ageGroup1 = Radiobutton(self.newWindow, text=">35", fg=textColor, bg=backGroundColor, variable=self.s,
                                     value=8)
        self.ageGroup1.pack()
        self.colorSubmitButton = Button(self.newWindow, text="Select Color", fg=textColor, bg=backGroundColor,
                                        command=lambda: getAge(self.master, self.newWindow, self.textColor,
                                                               self.s.get()))
        self.colorSubmitButton.pack()


class ChangeColorWindow:
    def __init__(self, master, button=None, backGroundColor="Black", textColor="#12ff51", eBColor="#1c1c1c",
                 errorColor="#fa2525", entryButtonBackgroundColor="#1c1c1c"):
        self.master = master
        self.button = button
        self.button.configure(state="disabled")
        self.backgroundColor = backGroundColor
        self.textColor = textColor
        self.eBColor = eBColor
        self.errorColor = errorColor
        self.entryButtonBackgroundColor = entryButtonBackgroundColor

        self.newWindow = Tk()
        self.newWindow.title("Text Color Editor")
        self.newWindow.geometry("250x30")
        self.newWindow.configure(bg=backGroundColor)
        self.colorLabel = Label(self.newWindow, text="Select one of the colors from the menu above.", fg=textColor,
                                bg=backGroundColor).place(x=0, y=0)
        self.colorMenu = Menu(self.newWindow)
        self.colorMenu.add_command(label="Red", command=lambda: func.selection(master, self.newWindow, 1))
        self.colorMenu.add_command(label="Light Green", command=lambda: func.selection(master, self.newWindow, 2))
        self.colorMenu.add_command(label="Yellow", command=lambda: func.selection(master, self.newWindow, 3))
        self.colorMenu.add_command(label="Light Blue", command=lambda: func.selection(master, self.newWindow, 4))
        self.newWindow.config(menu=self.colorMenu)


class chooseYourFavoriteColor:
    def __init__(self, master, button=None, backGroundColor="Black", textColor="#12ff51", eBColor="#1c1c1c",
                 errorColor="#fa2525",
                 entryButtonBackgroundColor="#1c1c1c"):
        self.master = master
        self.button = button
        self.button.configure(state="disabled")
        self.backgroundColor = backGroundColor
        self.textColor = textColor
        self.eBColor = eBColor
        self.errorColor = errorColor
        self.entryButtonBackgroundColor = entryButtonBackgroundColor

        self.newWindow = Tk()
        self.newWindow.title("Pick your favorite color")
        self.newWindow.configure(bg=backGroundColor)

        self.listBox = Listbox(self.newWindow)
        self.favoriteColor = Label(self.newWindow, text="What is your favorite color?",
                                   fg=textColor, bg=backGroundColor)
        self.listBox.insert(1, "Red")
        self.listBox.insert(2, "Orange")
        self.listBox.insert(3, "Yellow")
        self.listBox.insert(4, "Green")
        self.listBox.insert(5, "Blue")
        self.listBox.insert(6, "Purple")
        self.listBox.insert(7, "Other")
        # Button
        self.colorSubmitButton = Button(self.newWindow, text="Select Color", fg=textColor, bg=backGroundColor,
                                        command=lambda: func.getColor(self.master, self.newWindow, self.textColor,
                                                                      self.listBox.get(self.listBox.curselection())))

        # Enable Everything
        self.favoriteColor.pack()
        self.listBox.pack()
        self.colorSubmitButton.pack()

        # Mainloop
        self.newWindow.mainloop()
