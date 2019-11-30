from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cross_image = PhotoImage(file="C:/Data/cross2.gif")
        self.tick_image = PhotoImage(file="C:/Data/tick2.gif")
        
        # set window attributes
        self.title("Welcome to the hotel 'Hell'")
        
        # add components
        self.__add_hotel_header()
        #self.__add_name_frame()
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_name_image_label()
        #self.__add_passport_frame()
        self.__add_passport_label()
        self.__add_passport_entry()
        self.__add_passport_image_label()
        #self.__add_nights_frame()
        self.__add_nights_label()
        self.__add_nights_entry()
        self.__add_nights_image_label()
        self.__add_checkin_button()

    def __add_hotel_header(self):
        self.hotel_header = Label()
        self.hotel_header.grid(row=0, column=0, columnspan=3)
        self.hotel_header.configure(    text="Hotel Check In",
                                            font="Ariel 18")

    #def __add_name_frame(self):
        #self.name_frame = Frame()
        #self.name_frame.grid(row=1, column=0, columnspan=3)

    def __add_name_label(self):
        self.name_label = Label()
        self.name_label.grid(row=1, column=0, sticky=W)
        self.name_label.configure(  text="Name:",
                                    font="Ariel 16")

    def __add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column =1)
        self.name_entry.bind("<FocusOut>", self.__left_name_box)

    def __add_name_image_label(self):
        self.name_image_label = Label()
        self.name_image_label.grid(row=1, column=3)
        self.name_image_label.configure(image=self.cross_image)

    #def __add_passport_frame(self):
        #pass

    def __add_passport_label(self):
        self.passport_label = Label()
        self.passport_label.grid(row=2, column=0)
        self.passport_label.configure(  text="Passport Number:",
                                    font="Ariel 16")

    def __add_passport_entry(self):
        self.passport_entry = Entry()
        self.passport_entry.grid(row=2, column =1)
        self.passport_entry.bind("<FocusOut>", self.__left_passport_box)

    def __add_passport_image_label(self):
        self.passport_image_label = Label()
        self.passport_image_label.grid(row=2, column=3)
        self.passport_image_label.configure(image=self.cross_image)

    #def __add_nights_frame(self):
        #pass

    def __add_nights_label(self):
        self.nights_label = Label()
        self.nights_label.grid(row=3, column=0, sticky=W)
        self.nights_label.configure(  text="No. of nights:",
                                    font="Ariel 16")

    def __add_nights_entry(self):
        self.nights_entry = Entry()
        self.nights_entry.grid(row=3, column =1)
        self.nights_entry.bind("<FocusOut>", self.__left_nights_box)

    def __add_nights_image_label(self):
        self.nights_image_label = Label()
        self.nights_image_label.grid(row=3, column=3)
        self.nights_image_label.configure(image=self.cross_image)

    def __add_checkin_button(self):
        self.checkin_button = Button()
        self.checkin_button.grid(row=4, column=0, columnspan=3)
        self.checkin_button.configure(  text="Check In",
                                        font="Ariel 16")
        self.checkin_button.bind("<ButtonRelease-1>", self.__left_button_clicked)

    def __left_name_box(self, event):
        name = (self.name_entry.get())
        if(name == ""):
            self.name_image_label.configure(image=self.cross_image)
            messagebox.showinfo("Blank Name!!!!", "You have not entered your name, please enter your name")
        else:
            self.name_image_label.configure(image=self.tick_image)

    def __left_passport_box(self, event):
        passport = (self.passport_entry.get())
        if(passport == ""):
            self.passport_image_label.configure(image=self.cross_image)
            messagebox.showinfo("Blank passport Number!!!", "You have not entered your passport number, please enter your passport number")
        else:
            self.passport_image_label.configure(image=self.tick_image)

    def __left_nights_box(self, event):
        nights = (self.nights_entry.get())
        if(nights == ""):
            self.nights_image_label.configure(image=self.cross_image)
            messagebox.showinfo("Blank Number of nights!!!", "You have not entered the number of nights, please enter the number of nights")
        else:
            self.nights_image_label.configure(image=self.tick_image)

    def __left_button_clicked(self, event):
        nights = int(self.nights_entry.get())
        name = (self.name_entry.get())
        if(nights == 0):
            self.nights_image_label.configure(image=self.cross_image)
            messagebox.showinfo("Nights Issue!", "Zero nights is not valid, please re-enter the number of nights")
            
        elif(nights > 365):
            self.nights_image_label.configure(image=self.cross_image)
            messagebox.showinfo("Nights Issue!", "Too many nights - please re-enter a number of nights totaling a year or less")
            
        else:
            self.nights_image_label.configure(image=self.tick_image)
            messagebox.showinfo("Welcome to Hell", "Thank you for checking in " + name +", Maurice will take your bags to your room")

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()