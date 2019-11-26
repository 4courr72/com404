from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cactusleaf_plain_image = PhotoImage(file="C:/Data/cactusplain.gif")
        self.cactusleaf_name_image = PhotoImage(file="C:/Data/cactusname.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_cactus_header()
        self.__add_cactus_image_label()
        self.__add_flip_button()

    def __add_cactus_header(self):
        self.cactus_header = Label()
        self.cactus_header.grid(row=0, column=0, columnspan=3)
        self.cactus_header.configure(    text="Cactus Leaves",
                                            font="Ariel 18")

    def __add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=1)
        self.cactus_image_label.configure(image=self.cactusleaf_plain_image,
                                             height=264,
                                             width=459)

    def __add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=1)
        self.flip_button.configure( text="Flip")
        #Events
        self.flip_button.bind("<ButtonRelease-1>", self.__left_button_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.__right_button_clicked)
 
    def __left_button_clicked(self, event):
        #print("Left button clicked") #Added for testing purposes
        self.cactus_image_label.configure(image=self.cactusleaf_plain_image)

    def __right_button_clicked(self, event):
        #print("Right button clicked") #Added for testing purposes
        self.cactus_image_label.configure(image=self.cactusleaf_name_image)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()