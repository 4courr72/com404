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
        self.plane_y_pos = 250
        self.plane_x_change = 1
        self.plane_y_change = 0

        self.num_ticks = 0

        # add components
        self.add_plane_frame()
        self.add_plane_image_label()
        self
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):

        #Check right side
        if(self.plane_x_pos >439):
            self.figure1_x_change = -1

        #Check left side
        if(self.plane_x_pos <0):
            self.figure1_x_change = 1

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

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 