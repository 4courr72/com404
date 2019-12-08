from tkinter import *
from tkinter import messagebox

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.cross_image = PhotoImage(file="C:/Data/cross2.gif")
        self.tick_image = PhotoImage(file="C:/Data/tick2.gif")
        self.default_image = PhotoImage(file="C:/Data/cross2.gif")

        # set window attributes
        self.configure(height=350,
                       width=500,
                       bg="#ffe8e8")
        self.title("TCA2")

        # add components
        #self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_amount_label()
        self.__add_entry_and_tick_frame()
        self.__add_from_label()
        self.__add_from_combobox()
        self.__add_to_label()
        self.__add_to_combobox()
        self.__add_tick_or_cross_label()
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

    def __add_entry_and_tick_frame(self):
        #Create
        self.entry_and_tick_frame = Frame()
        self.entry_and_tick_frame.grid(row=2, column=0, columnspan=2)
        #Style

    def __add_from_label(self):
        #Create
        self.from_label = Label()
        self.from_label.grid(row=3, column=0, padx=20, sticky=W)
        #Style
        self.from_label.configure(  text="From")

    def __add_from_combobox(self):
        #Create
        self.from_combobox = Combobox(values=("GPB", "Euros"))
        self.from_combobox.grid(row=4, column=0, columnspan=2)
        #Style
        self.from_combobox.configure

    def __add_to_label(self):
        pass

    def __add_to_combobox(self):
        pass

    def __add_amount_entry(self):
        #Create
        self.amount_entry = Entry(self.entry_and_tick_frame)
        self.amount_entry.grid(row=0, column=0, columnspan=2, padx=20, sticky=E)
        #Style
        self.amount_entry.configure(width=60)
        #Events
        self.amount_entry.bind("<KeyRelease>", self.__amount_box_check)

    def __add_tick_or_cross_label(self):
        #Create
        self.tick_or_cross_label = Label(self.entry_and_tick_frame)
        self.tick_or_cross_label.grid(row=0, column=1, sticky=E)
        #Style
        self.tick_or_cross_label.configure(   image=self.default_image)


    def __amount_box_check(self, event):
        if(self.amount_entry.get() == ""):
            self.default_image = PhotoImage(file="C:/Data/cross2.gif")
            self.tick_or_cross_label.configure(   image=self.default_image)
        else:
            self.default_image = PhotoImage(file="C:/Data/tick2.gif")
            self.tick_or_cross_label.configure(   image=self.default_image)

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
        self.clear_button.bind("<ButtonRelease-1>", self.__clear_button_clicked)

    def __add_convert_button(self):
        #Create
        self.convert_button = Button(self.button_frame)
        self.convert_button.grid(row=0, column=1, sticky=W, padx=5, pady=20)
        #Style
        self.convert_button.configure(    text="Convert")
        #Event
        self.convert_button.bind("<ButtonRelease-1>", self.__convert_button_clicked)

    def __convert_button_clicked(self, event):
        amount_to_convert = float(self.amount_entry.get())
        convertion_rate1 = 1.15
        converted_amount1 = (amount_to_convert * convertion_rate1)
        self.message_label.configure(text="Converting...")
        messagebox.showinfo("Results", "£{} is {} euros with a convertion rate of {}".format(round(amount_to_convert,2), round(converted_amount1,2), convertion_rate1))

    def __clear_button_clicked(self, event):
        self.message_label.configure(text="System Message Displayed Here")

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