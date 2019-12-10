from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.configure(height=350,
                       width=500)
        self.title("TCA2")

        # add components
        #self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_x_label()
        self.__add_x_entry()
        self.__add_x_frame() 
        self.__add_x_button()
        self.__add_x_listbox()

    #Define components
    def __add_heading_label(self):
        #Create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
        #Style
        self.heading_label.configure(   text="yyyyy",
                                        font="Arial 18")
        # #Events

    #pady=10,  padx=10,  row=0,  column=0, columnspan=2,  

    #bd=3 [borderwidth],   

    def __add_x_label(self):
        #Create
        pass
        #Style

        #Events

    def __add_x_entry(self):
        #Create
        pass
        #Style
        
        #Events

    def __add_x_frame(self):
        #Create
        pass
        #Style

        #Events

    def __add_x_button(self):
        #Create
        pass
        #Style

        #Events

    def __add_x_listbox(self):
        #Create
        #width=,  height=,  
        pass
        #Style

        #Events

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 