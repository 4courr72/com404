from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.bus_image = PhotoImage(file="C:/Data/bus2.gif")
        self.map_image = PhotoImage(file="C:/Data/map2.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_busjourney_header()
        self.__add_map_frame()
        self.__add_map_image_label()
        self.__add_bus_image_label()

    def __add_busjourney_header(self):
        self.busjourney_header = Label()
        self.busjourney_header.grid(row=0, column=0, columnspan=3)
        self.busjourney_header.configure(    text="Bus Journey",
                                            font="Ariel 18")

    def __add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.grid(row=1, column=0)
        self.map_frame.configure( width=260, height=150)
        #Events
        

    def __add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)
        #Events
        self.map_image_label.bind("<B1-Motion>", self.bus_move)

    def __add_bus_image_label(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=10, y=10)
        self.bus_image_label.configure(image=self.bus_image)
        #Events
        #self.flip_button.bind("<ButtonRelease-1>", self.__left_button_clicked)
        #self.flip_button.bind("<ButtonRelease-3>", self.__right_button_clicked)
 
    def bus_move(self, event):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is" + str(event.x)) #Proves that I can get a return on mouse position for x (works)
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is" + str(event.y)) #Proves that I can get a return on mouse position for y (works)

        #self.bus_image_label = Label(self.map_frame) - by keeping this and the last line in I was 'rewriting' the reference and hence bus image was left where it was. Dont need this.
        self.bus_image_label.place(x=event.x, y=event.y)
        #self.bus_image_label.configure(image=self.bus_image)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()