from tkinter import *
from tkinter import messagebox #Note - need to import this for the 'messagebox' function to work!
# from tkinter import checkbutton #Note - need to import this for the 'checkbutton' function to work!

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Passport Checker")
        
        # add components
        CheckVarYes3 = IntVar()
        self.__add_heading_label()
        self.__add_q1_label()
        self.__add_q1frame()
        #self.__add_q1no_label()
        self.__add_q1no_checkbutton()
        #self.__add_q1yes_label() 
        self.__add_q1yes_checkbutton()
        self.__add_q2_label()
        self.__add_q2frame()
        #self.__add_q2no_label()
        self.__add_q2no_checkbutton()
        #self.__add_q2yes_label()    
        self.__add_q2yes_checkbutton()
        self.__add_q3_label()
        self.__add_q3frame()
        #self.__add_q3no_label()
        self.__add_q3no_checkbutton()
        #self.__add_q3yes_label()
        self.__add_q3yes_checkbutton()
        #self.add_check_button_clicked()
        self.__add_check_button()
        
        
    def __add_heading_label(self):
        #Create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        #Style
        self.heading_label.configure(  text="Passport Checker",
                                        font="Arial 18" )
        #Event

    def __add_q1_label(self):
        #Create
        self.q1_label = Label()
        self.q1_label.grid(row=1, column=0, sticky=W)
        #Style
        self.q1_label.configure(    text="1. Photo matches face?",
                                    font="Arial 12")
        #Event
    
    def __add_q1frame(self):
        #Create
        self.q1frame = Frame()
        self.q1frame.grid(row=2, column=0, sticky=E)
        #Style
        self.q1frame.configure( bg="#eee", 
                                    padx=40, 
                                    pady=1)
        #Event

    def __add_q1no_label(self):
        #Create
        self.q1no_label = Label(self.q1frame)
        self.q1no_label.pack(side=RIGHT)
        #Style
        self.q1no_label.configure(    text="No",
                                        font="Arial 12")
        #Event


    def __add_q1no_checkbutton(self):
        #Create
        CheckVarNo1 = IntVar()
        self.q1no_checkbutton = Checkbutton(self.q1frame, text="No", font="Ariel 12", variable = CheckVarNo1)
        self.q1no_checkbutton.pack(side=RIGHT)
        #Style

        #Event


    def __add_q1yes_label(self):
        #Create
        self.q1yes_label = Label(self.q1frame)
        self.q1yes_label.pack(side=RIGHT)
        #Style
        self.q1yes_label.configure(    text="Yes",
                                        font="Arial 12")
        #Event

    def __add_q1yes_checkbutton(self):
        #Create
        CheckVarYes1 = IntVar()
        self.q1yes_checkbutton = Checkbutton(self.q1frame, text="Yes", font="Ariel 12", variable = CheckVarYes1)
        self.q1yes_checkbutton.pack(side=RIGHT)
        #Style
        
        #Event

    def __add_q2_label(self):
        #Create
        self.q2_label = Label()
        self.q2_label.grid(row=3, column=0, sticky=W)
        #Style
        self.q2_label.configure(    text="2. Passport has at least 6 months validity?",
                                    font="Arial 12")
        #Event

    def __add_q2frame(self):
        #Create
        self.q2frame = Frame()
        self.q2frame.grid(row=4, column=0, sticky=E)
        #Style
        self.q2frame.configure( bg="#eee", 
                                    padx=40, 
                                    pady=1)
        #Event

    #def __add_q2no_label(self):
        #self.q2no_label = Label(self.q2frame)
        #self.q2no_label.pack(side=RIGHT)
        #Style
        #self.q2no_label.configure(    text="No",
        #                                font="Arial 12")
        #Event

    def __add_q2no_checkbutton(self):
        #Create
        CheckVarNo2 = IntVar()
        self.q2no_checkbutton = Checkbutton(self.q2frame, text="No", font="Ariel 12", variable = CheckVarNo2)
        self.q2no_checkbutton.pack(side=RIGHT)
        #Style

        #Event

    #def __add_q2yes_label(self):
        #Create
        #self.q2yes_label = Label(self.q2frame)
        #self.q2yes_label.pack(side=RIGHT)
        #Style
        #self.q2yes_label.configure(    text="Yes",
        #                                font="Arial 12")
        #Event

    def __add_q2yes_checkbutton(self):
        #Create
        CheckVarYes2 = IntVar()
        self.q2yes_checkbutton = Checkbutton(self.q2frame, text="Yes", font="Ariel 12", variable=CheckVarYes2)
        self.q2yes_checkbutton.pack(side=RIGHT)
        #Style

        #Event

    def __add_q3_label(self):
        #Create
        self.q3_label = Label()
        self.q3_label.grid(row=5, column=0, sticky=W)
        #Style
        self.q3_label.configure(    text="3. Visa, if required, is valid?",
                                    font="Arial 12")
        #Event

    def __add_q3frame(self):
        #Create
        self.q3frame = Frame()
        self.q3frame.grid(row=6, column=0, sticky=E)
        #Style
        self.q3frame.configure( bg="#eee", 
                                    padx=40, 
                                    pady=1)
        #Event

    #def __add_q3no_label(self):
        #Create
        #self.q3no_label = Label(self.q3frame)
        #self.q3no_label.pack(side=RIGHT)
        #Style
        #self.q3no_label.configure(    text="No",
        #                                font="Arial 12")
        #Event

    def __add_q3no_checkbutton(self):
        #Create
        CheckVarNo3 = IntVar()
        self.q3no_checkbutton = Checkbutton(self.q3frame, text="No", font="Ariel 12", variable = CheckVarNo3)
        self.q3no_checkbutton.pack(side=RIGHT)
        #Style

        #Event

    #def __add_q3yes_label(self):
        #Create
        #self.q3yes_label = Label(self.q3frame)
        #self.q3yes_label.pack(side=RIGHT)
        #Style
        #self.q3yes_label.configure(    text="Yes",
        #                                font="Arial 12")
        #Event

    def __add_q3yes_checkbutton(self):
        #Create
        self.q3_is_yes = IntVar()
        self.q3yes_checkbutton = Checkbutton(self.q3frame, text="Yes", font="Ariel 12", variable=self.q3_is_yes)
        self.q3yes_checkbutton.pack(side=RIGHT)
        #Style

        #Event
        #return(CheckVarYes3)

    def __add_check_button(self):
        #Create
        self.check_button = Button()
        self.check_button.grid(row=7, column=0)
        #Style
        self.check_button.configure(    text="Check",
                                        font="Arial 12")
        #Event
        self.check_button.bind("<ButtonRelease-1>", self.__add_check_button_clicked)

    def __add_check_button_clicked(self, event):
        print(self.q3_is_yes.get())
        #print("Hello") - test to make sure this section is invoked (it is)
        #print("Status of Yes 3 Checkbox is %d" % (CheckVarYes3.get())) #Additional check to see if I can print a variable (no luck so far)
        #print(CheckVarYes3.get())
        #if (CheckVarYes3 == 1):
        #    print("Your passport is validated for your journey")
        #else:
        #    print("Your passport is NOT validated for your journey! Seek further assistance from the Passport Office!")
#Got some help from Prins about finding the value of the checjbutton - I need to have self. in front of the variable or it wont be callable from outside.