from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        #set window attributes
        # self.geometry("500x500")
        self.title("Newsletter")
        self.configure( height=200,
                        width=400)



        # add window components
        
        self.__add_outer_frame() #Got this from answer posted by Prins ('GFAP')
        self.__add_heading_label()
        self.__add_message_label()
        self.__add_email_frame()
        self.__add_box_label()
        #self.__add_inner_frame()
        self.__add_a_button()
        
    def __add_outer_frame(self): #GFAP all this block
        self.outer_frame = Frame()
        self.outer_frame.pack(fill=X) # fill=X allows widget to expand in vertical direction as required
        self.outer_frame.configure( bg="#eee", #Changes colour around edge - can obly see top edge though
                                    padx=200, #mmm, does seem to matter what figure I put in
                                    pady=200) #...or this setting

    def __add_heading_label(self): #the 2 leading underscores is to make it private!
        #Remember these three steps:
        # create component ('Create')
        self.heading_label = Label() #'label' is a class already in TKinter
        self.heading_label.pack() # 'place' is .... 0.0 is top left corner and gets bigger as you go down
        # style component ('Style')
        #'configure' allows you to set multiple attributes in one command, seperated by commas. put on new line to make easier to read
        self.heading_label.configure(   font = "Arial 18",
                                        text="RECEIVE OUR NEWSLETTER")
        # add component events ('Events')


    def __add_message_label(self):
        #pass - use this as a placeholder when 1st created - it will let program just run through. 
        
        #Create
        self.message_label = Label()
        self.message_label.pack()

        #Style
        self.message_label.configure(   font = "Arial 9", 
                                        text="Please enter your email below to receive our newsletter.")

    def __add_email_frame(self):
        #Create
        self.email_frame = Frame(width=20, height=2)
        self.email_frame.pack()

        #Style
        # self.email_frame.configure(width = 40)

    def __add_box_label(self):
        #Create
        self.box_label = Label(self.email_frame)
        self.box_label.pack(side=RIGHT) #Took this out of brackets: self.email_frame, side=LEFT

        #Style
        self.box_label.configure(   font = "Arial 10",
                                    text="Email:")

    def __add_a_button(self):
        #Create
        self.a_button = Button()
        self.a_button.pack()

        #Style
        self.a_button.configure(    text = "Subscribe",
                                    font = "Arial 8",
                                    underline = 0,
                                    justify = CENTER,
                                    width = 62)
    
    def __add_inner_frame(self):
        #Create
        self.inner_frame = Entry()
        self.inner_frame.pack()
        
        #Style
        self.inner_frame.configure( font = "Arial 10",
                                    width = 40)
        