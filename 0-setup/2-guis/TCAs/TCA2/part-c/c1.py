from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.cross_image = PhotoImage(file="C:/Data/cross2.gif")
        self.tick_image = PhotoImage(file="C:/Data/tick2.gif")
        self.default_image = PhotoImage(file="C:/Data/cross2.gif")
        self.figure_gbp_image = PhotoImage(file="C:/Data/figuregbp2.gif")
        self.figure_euro_image = PhotoImage(file="C:/Data/figureeuro2.gif")
        self.figure_no_currency_image = PhotoImage(file="C:/Data/figure2.gif")
        self.building_image = PhotoImage(file="C:/Data/building1.gif")

        # set window attributes
        self.configure(height=350,
                       width=500,
                       bg="#ffe8e8")
        self.title("TCA2")

        # set animation attributes
        self.figure_x_pos = 0
        self.figure_x_change = 1

        self.num_ticks = 0

        # add components
        #self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_amount_label()
        self.__add_entry_and_tick_frame()
        self.__add_amount_entry()
        self.__add_from_label()
        self.__add_from_combobox()
        self.__add_to_label()
        self.__add_to_combobox()
        self.__add_tick_or_cross_label()
        self.__add_button_frame() 
        self.__add_clear_button()
        self.__add_convert_button()
        self.__add__message_label()
        self.__add_simulate_button()
        self.__add_animation_frame()
        self.__add_figure_image_label()
        self.__add_building_image_label()
        

    def tick(self):

        #Check reaching building
        if(self.figure_x_pos >300):
            self.figure_x_change = 0

        #Move figure
        self.figure_x_pos = self.figure_x_pos + self.figure_x_change
        self.figure_image_label.place(x=self.figure_x_pos)
        self.after(10, self.tick)

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

    def __add_amount_entry(self):
        #Create
        self.amount_entry = Entry(self.entry_and_tick_frame)
        self.amount_entry.grid(row=0, column=0, padx=20, sticky=W)
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

    def __add_from_label(self):
        #Create
        self.from_label = Label()
        self.from_label.grid(row=3, column=0, padx=20, sticky=W)
        #Style
        self.from_label.configure(  text="From")

    def __add_from_combobox(self):
        #Create
        self.from_combobox = ttk.Combobox(values=("GBP", "Euros"))
        self.from_combobox.grid(row=4, column=0, columnspan=2)
        #Style
        self.from_combobox.configure(   width=60)
        self.from_combobox.set("GBP")

    def __add_to_label(self):
         #Create
        self.to_label = Label()
        self.to_label.grid(row=5, column=0, padx=20, sticky=W)
        #Style
        self.to_label.configure(  text="To")

    def __add_to_combobox(self):
        #Create
        self.to_combobox = ttk.Combobox(values=("Euros", "USD"))
        self.to_combobox.grid(row=6, column=0, columnspan=2)
        #Style
        self.to_combobox.configure(   width=60)
        self.to_combobox.set("Euros")

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
        self.button_frame.grid(row=7, column=0, columnspan=2)
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
        from_currency = (self.from_combobox.get())
        to_currency = (self.to_combobox.get())
        convertion_rate_gbp_to_euros = 1.15
        convertion_rate_gbp_to_usd = 1.42
        convertion_rate_euros_to_usd = 1.24
        convertion_rate = 0
        if(from_currency == "GBP"):
            if(to_currency == "Euros"):
                convertion_rate = convertion_rate_gbp_to_euros
            else:
                convertion_rate = convertion_rate_gbp_to_usd
        elif(from_currency == "Euros"):
            convertion_rate = convertion_rate_euros_to_usd

        converted_amount = (amount_to_convert * convertion_rate)
        self.message_label.configure(text="Converting...")
        messagebox.showinfo("Currency Converter Results", "{} from {} to {} with a rate of {} is {}".format(amount_to_convert, from_currency, to_currency, convertion_rate, converted_amount))

    def __clear_button_clicked(self, event):
        self.message_label.configure(text="System Message Displayed Here")

    def __add__message_label(self):
        #Create
        self.message_label = Label()
        self.message_label.grid(row=8, column=0, columnspan=2, padx=20, pady=10)
        #Style
        self.message_label.configure(   text="System Message Displayed Here",
                                        font="Arial 10",
                                        width=50,
                                        height=2,
                                        bd=3,
                                        bg="#fffbce")
        #Events

    def __add_simulate_button(self):
        #Create
        self.simulate_button = Button()
        self.simulate_button.grid(row=9, column=0, columnspan=2, pady=20)
        #Style
        self.simulate_button.configure( text="Simulate")
        #Event
        self.simulate_button.bind("<ButtonRelease-1>", self.__simulate_button_clicked)

    def __simulate_button_clicked(self, event):
        self.tick()
        from_currency = (self.from_combobox.get())
        if(from_currency == "GBP"):
            self.figure_image_label.configure(image=self.figure_gbp_image)
        elif(from_currency == "Euros"):
            self.figure_image_label.configure(image=self.figure_euro_image)

    def __add_animation_frame(self):
        #Create
        self.animation_frame = Frame(self)
        self.animation_frame.grid(row=10, column=0, columnspan=2, padx=20, pady=20)
        #Style
        self.animation_frame.configure( width=360,
                                        height=200,
                                        bg="#b0b0b0")

    def __add_figure_image_label(self):
        #Create
        self.figure_image_label = Label(self.animation_frame)
        self.figure_image_label.place(x=self.figure_x_pos, y=70)
        #Style
        self.figure_image_label.configure(image=self.figure_no_currency_image)

    def __add_building_image_label(self):
        #Create
        self.building_image_label = Label(self.animation_frame)
        self.building_image_label.place(x=300, y=50)
        #Style
        self.building_image_label.configure(image=self.building_image)
    

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 