from tkinter import *

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.configure(height=350,
                       width=500,
                       bg="#ffe8e8")
        self.title("TCA2")

        # add components
        #self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_amount_label()
        self.__add_amount_entry()
        self.__add_button_frame() 
        self.__add_clear_button()
        self.__add_convert_button()
        self.__add__message_label()

    #Define components
    def __add_heading_label(self):
        #Create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
        #Style
        self.heading_label.configure(   text="Currency Converter",
                                        font="Arial 18")
        # #Events

    def __add_amount_label(self):
        #Create
        self.amount_label = Label()
        self.amount_label.grid(row=1, column=0, sticky=W, padx=20)
        #Style
        self.amount_label.configure( text="Amount",
                                      font="Arial 10"  )
        #Events

    def __add_amount_entry(self):
        #Create
        self.amount_entry = Entry()
        self.amount_entry.grid(row=2, column=0, columnspan=2, padx=20)
        #Style
        self.amount_entry.configure(width=60)
        #Events

    def __add_button_frame(self):
        #Create
        self.button_frame = Frame()
        self.button_frame.grid(row=3, column=0, columnspan=2)
        #Style
        #Events

    def __add_clear_button(self):
        #Create
        self.clear_button = Button(self.button_frame)
        self.clear_button.grid(row=0, column=0, sticky=E, padx=5, pady=20)
        #Style
        self.clear_button.configure(    text="Clear",
                                        width=7)
        #Events

    def __add_convert_button(self):
        #Create
        self.convert_button = Button(self.button_frame)
        self.convert_button.grid(row=0, column=1, sticky=W, padx=5, pady=20)
        #Style
        self.convert_button.configure(    text="Convert")

    def __add__message_label(self):
        #Create
        self.message_label = Label()
        self.message_label.grid(row=4, column=0, columnspan=2, padx=20, pady=10)
        #Style
        self.message_label.configure(   text="System Message Displayed Here",
                                        font="Arial 10",
                                        width=50,
                                        height=7,
                                        bd=3,
                                        bg="#fffbce")
        #Events

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 