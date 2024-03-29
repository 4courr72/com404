from tkinter import *
from tkinter import messagebox #Note - need to inport this for the 'messagebox' function to work!

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        #Create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        #Style
        self.heading_label.configure(  text="Entrance Ticket",
                                        font="Arial 18" )

    def __add_instruction_label(self):
          #Create
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, sticky=W)
        #Style
        self.instruction_label.configure(  text="How many tickets are needed?",
                                        font="Arial 14" )
        
    def __add_tickets_entry(self):
        #Create
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0)
        self.tickets_entry.get()
        return self.tickets_entry.get

        #Style
        self.tickets_entry.configure(   width=20,
                                        font="Arial 18")

    def __add_buy_button(self):
        #Create
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0)

        #Style
        self.buy_button.configure(  width=15,
                                    text="Buy",
                                    font="Arial 14")

        #Event
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
        # print(self.tickets_entry.get()) - used this to test the get element
        tickets = int(self.tickets_entry.get())
        if (tickets == 1):
            messagebox.showinfo("Purchased!", "You have purchased 1 ticket!")
        elif (tickets > 1):
            messagebox.showinfo("Purchased!", "You have purchased {} ticket!".format(tickets))
        else:
            messagebox.showinfo("Purchased!", "You have entered an invalid number of tickets!")