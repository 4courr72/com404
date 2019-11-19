from tkinter import *
from tkinter import messagebox #Note - need to inport this for the 'messagebox' function to work!

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Song Maker")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_inner_frame()
        self.__add_lyric_input()
        self.__add_add_button()
        self.__add_output_label()
        self.__add_lyric_scrollbox()
        
    def __add_heading_label(self):
        #Create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        #Style
        self.heading_label.configure(  text="Song Maker",
                                        font="Arial 18" )

    def __add_instruction_label(self):
        #Create
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, sticky=W)
        #Style
        self.instruction_label.configure(   text="Lyric to add:",
                                            font="Arial 10" )

    def __add_inner_frame(self):
        #Create
        self.inner_frame = Frame()
        self.inner_frame.grid(row=2, column=0)
        #Style
        self.inner_frame.configure( bg="#eee", 
                                    padx=10, 
                                    pady=10)

    def __add_lyric_input(self):
        #Create
        self.lyric_input = Entry(self.inner_frame)
        self.lyric_input.pack(side=LEFT)
        #Style
        self.lyric_input.configure( width=30)


    def __add_add_button(self):
        #Create
        self.add_button = Button(self.inner_frame)
        self.add_button.pack(side=RIGHT)
        #Style
        self.add_button.configure(  text="Add")
        #Event
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)

    def __add_button_clicked(self, event):
        #print(self.lyric_input.get()) #- used this to test the get element
        self.lyric_scrollbox.insert(END, self.lyric_input.get())

    def __add_output_label(self):
        #Create
        self.output_label = Label()
        self.output_label.grid(row=3, column=0, sticky=W)
        #Style
        self.output_label.configure(    text="Lyrics:",
                                        font="Arial 10")

    def __add_lyric_scrollbox(self):
        #Create
        self.lyric_scrollbox = Listbox()
        self.lyric_scrollbox.grid(row=4, column=0)
        #Style
        self.lyric_scrollbox.configure(  height=2,
                                      width=40)
