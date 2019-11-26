from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cross_image = PhotoImage(file="C:/Data/cross2.gif")
        self.tick_image = PhotoImage(file="C:/Data/tick2.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_hotel_header()
        self.__add_name_frame()
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_name_image_label()
        self.__add_passport_frame()
        self.__add_passport_label()
        self.__add_passport_entry()
        self.__add_passport_image_label()
        self.__add_nights_frame()
        self.__add_nights_label()
        self.__add_nights_entry()
        self.__add_nights_image_label()
        self.__add_checkin_button()

    def __add_hotel_header(self):
        pass

    def __add_name_frame(self):
        pass

    def __add_name_label(self):
        pass

    def __add_name_entry(self):
        pass

    def __add_name_image_label(self):
        pass

    def __add_passport_frame(self):
        pass

    def __add_passport_label(self):
        pass

    def __add_passport_entry(self):
        pass

    def __add_passport_image_label(self):
        pass

    def __add_nights_frame(self):
        pass

    def __add_nights_label(self):
        pass

    def __add_nights_entry(self):
        pass

    def __add_nights_image_label(self):
        pass

    def __add_checkin_button(self):
        pass
    
# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()