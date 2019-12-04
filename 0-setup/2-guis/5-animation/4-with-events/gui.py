from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.plane_image = PhotoImage(file="c:/Data/plane2.gif")

        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.plane_x_pos = 0
        self.plane_y_pos = 190
        self.plane_x_change = 1
        self.plane_y_change = 0

        self.num_ticks = 0

        # add components
        self.add_plane_image_label()
        self.__add_up_button()
        self.__add_down_button()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):

        #Check right side
        if(self.plane_x_pos >459):
            self.plane_x_change = -1

        #Check left side
        if(self.plane_x_pos <0):
            self.plane_x_change = 1

        #Move plane side to side
        self.plane_x_pos = self.plane_x_pos + self.plane_x_change
        self.plane_y_pos = self.plane_y_pos + self.plane_y_change
        self.plane_image_label.place(x=self.plane_x_pos, 
                                            y=self.plane_y_pos)
        self.after(10, self.tick)

    # the plane image
    def add_plane_image_label(self):
        self.plane_image_label = Label()
        self.plane_image_label.place(x=self.plane_x_pos,
                                    y=self.plane_y_pos)
        self.plane_image_label.configure(image=self.plane_image)

    def __add_up_button(self):
        self.up_button = Button()
        self.up_button.place(x=100, y=400)

        #Style
        self.up_button.configure(  width=7,
                                    text="UP",
                                    font="Arial 18")

        #Event
        self.up_button.bind("<ButtonRelease-1>", self.__up_button_clicked)

    def __add_down_button(self):
        self.down_button = Button()
        self.down_button.place(x=300, y=400)

        #Style
        self.down_button.configure(  width=7,
                                    text="DOWN",
                                    font="Arial 18")

                #Event
        self.down_button.bind("<ButtonRelease-1>", self.__down_button_clicked)

    def __up_button_clicked(self, event):
        self.plane_y_change = -1

    def __down_button_clicked(self, event):
        self.plane_y_change = 1

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 