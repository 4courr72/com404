from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        #set window attributes
        # self.geometry("500x500")
        # self.title("Newsletter")
        self.configure( height=200,
                        width=400)



        # add window components
        self.__add_heading_label()
        self.__add_message_label()
        self.__add_a_button()
        self.__add_box_label()
        self.__add_inner_frame()

    def __add_heading_label(self): #the 2 leading underscores is to make it private!
        
        #Remember these three steps:
        # create component
        self.heading_label = Label() #'label' is a class already in TKinter
        self.heading_label.place(x=27, y=20) # 'place' is .... 0.0 is top left corner and gets bigger as you go down
        # style component
        #'configure' allows you to set multiple attributes in one command, seperated by commas. put on new line to make easier to read
        self.heading_label.configure(   font = "Arial 18",
                                        text="RECEIVE OUR NEWSLETTER")
        # add component events

    def __add_message_label(self):
        #pass
        self.message_label = Label()
        self.message_label.place(x = 35, y = 90)
        self.message_label.configure(   font = "Arial 9", 
                                        text="Please enter your email below to receive our newsletter.")


    def __add_a_button(self):
        self.a_button = Button()
        self.a_button.place(x = 10, y = 170)
        self.a_button.configure(    text = "Subscribe",
                                    font = "Arial 8",
                                    underline = 0,
                                    justify = CENTER,
                                    width = 62)

    def __add_box_label(self):
        self.box_label = Label()
        self.box_label.place(x = 20, y = 130)
        self.box_label.configure(   font = "Arial 10",
                                    text="Email:")

    def __add_inner_frame(self):
        self.inner_frame = Entry()
        self.inner_frame.place(x = 80, y = 130)
        self.inner_frame.configure( font = "Arial 10",
                                    width = 40)