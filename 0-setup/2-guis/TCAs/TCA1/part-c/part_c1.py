from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # load resources
        self.default_image = PhotoImage(file="c:/Data/default.gif")
        self.filled_image = PhotoImage(file="c:/Data/filled1.gif")
        self.empty_image = PhotoImage(file="c:/Data/empty1.gif")

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#ccc", height=235, width=360)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_email_image_label()
        self.__add_frequency_label()
        self.__add_menu_dropdown()
        self.__add_subscribe_button()
        self.__add_animate_button()
        
    #Define components
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.place(x=10, y=10, relheight = 0.84, relwidth=0.94)
    
    def __add_heading_label(self):
        #Create
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=10)
        #Style
        self.heading_label.configure(   text="RECEIVE OUR NEWSLETTER",
                                        font="Arial 14")
        #Event

    def __add_instruction_label(self):
        #Create
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=W)
        #Style
        self.instruction_label.configure(   text="Please enter your email below to receive our newsletter.")

        #Event

    def __add_email_label(self):
        #Create
        self.email_label = Label(self.outer_frame)
        self.email_label.grid(row=2, column=0, padx=10, sticky=E)
        #Style
        self.email_label.configure( text="Email:")
        #Event

    def __add_email_entry(self):
        #Create
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=1, sticky=W)
        #Style
        self.email_entry.configure( fg="#f00",
                                    bd=2,
                                    width=30)
        #Event
        self.email_entry.bind("<KeyRelease>", self.__email_check)

    def __add_email_image_label(self):
        #Create
        self.email_image_label = Label(self.outer_frame)
        self.email_image_label.grid(row=2, column=1, padx=10, sticky=E)
        #Style
        self.email_image_label.configure(   image=self.default_image)

    def __add_frequency_label(self):
        #Create
        self.frequency_label = Label(self.outer_frame)
        self.frequency_label.grid(row=3, column=0, padx=10, sticky=E)
        #Style
        self.frequency_label.configure( text="Type")
        #Event

    def __add_menu_dropdown(self):
        #Create a variable
        self.menu_list = StringVar()
        choices = {'Yearly', 'Monthly', 'Weekly'}
        self.menu_list.set('Weekly') #Setting the default option
        #A dictionary containing the options
        self.menu_dropdown = OptionMenu(self.outer_frame, self.menu_list, *choices)
        self.menu_dropdown.grid(row=3, column=1, sticky=W)
        self.menu_dropdown.configure(   width=33)

        print (self.menu_list.get())
        ##current_selection = menu_list.()
        #return menu_list

    def __add_subscribe_button(self):
        #Create
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=4, column=0, columnspan=3)
        #Style
        self.subscribe_button.configure(    text="Subscribe",
                                            bg="#fee",
                                            width=47)
        #Event
        self.subscribe_button.bind ("<ButtonRelease-1>", self.__subscribe_button_clicked)

    def __add_animate_button(self):
        #Set variable
        #self.animate_state = Int()
        self.animate_state = 0
        #Create
        self.animate_button = Button(self.outer_frame)
        self.animate_button.grid(row=5, column=0, columnspan=3)
        #Style
        self.animate_button.configure(    text="Start Animation",
                                            bg="#fee",
                                            width=47)
        print(self.animate_state)
        #Event
        self.animate_button.bind ("<ButtonRelease-1>", self.__animate_button_clicked)

    def __subscribe_button_clicked(self, event):
        current_selection = self.menu_list.get()
        if(self.email_entry.get() == ""):
            messagebox.showinfo("Newsletter", "Please enter your email!")
        elif(current_selection == "Weekly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this every Monday.")
        elif(current_selection == "Monthly"):
             messagebox.showinfo("Newsletter", "You have subscribed to the monthly newsletter! You will receive this on the first day of each month.")
        elif(current_selection == "Yearly"):
             messagebox.showinfo("Newsletter", "You have subscribed to the yearly newsletter! You will receive this at the start of each year.")


    def __email_check(self, event):
        if(self.email_entry.get() == ""):
            self.email_image_label.configure(image=self.empty_image)
            messagebox.showinfo("Newsletter", "Please enter your email!")
        else:
            self.email_image_label.configure(image=self.filled_image)

    def __animate_button_clicked(self, event):
        if(self.animate_state == 0):
            self.animate_state = 1
        else:
            self.animate_state = 0

        if(self.animate_state == 0):
            self.animate_button.configure(text="Start Animation")
        else:
            self.animate_button.configure(text="Stop Animation")
            
        print(self.animate_state)
        print("Animate button clicked")

# the object
if __name__ == "__main__":
    gui = Gui()    
    gui.mainloop() 