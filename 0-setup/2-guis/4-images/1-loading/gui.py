#from tkinter import *
from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="C:/Data/ambulance.gif")
        self.bike_image = PhotoImage(file="C:/Data/bike.gif")
        self.plane_image = PhotoImage(file="C:/Data/plane.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_transport_header()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()

    def __add_transport_header(self):
        self.transport_header = Label()
        self.transport_header.grid(row=0, column=0, columnspan=3)
        self.transport_header.configure(    text="Transport",
                                            font="Ariel 18")

    def __add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image,
                                             height=60,
                                             width=60)

    def __add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.grid(row=1, column=1)
        self.bike_image_label.configure(image=self.bike_image,
                                             height=60,
                                             width=60)
 
    def __add_plane_image_label(self):
        self.plane_image_label = Label()
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image,
                                             height=60,
                                             width=60)
 

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()