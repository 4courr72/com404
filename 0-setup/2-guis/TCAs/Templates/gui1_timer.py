from tkinter import *
import messagebox
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.1_image = PhotoImage(file="c:/Data/figure1-2.gif")
        self.2_image = PhotoImage(file="c:/Data/figure2-2.gif")
        self.3_image = PhotoImage(file="c:/Data/figure3-2.gif")

        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.1_x_pos = 0
        self.1_y_pos = 0
        self.1_x_change = 1
        self.1_y_change = 0
        self.num_ticks = 0

        # add components
        self.add_1_image_label()
        self.add_2_image_label()
        self.add_3_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.num_ticks = self.num_ticks + 1

        #Person 1
        if (self.num_ticks % 5 == 0):
            #Check right side
            if(self.1_x_pos >500):
                self.1_x_change = -1

            #Check left side
            if(self.1_x_pos <0):
                self.1_x_change = 1

            #Move [item] 1
            self.1_x_pos = self.1_x_pos + self.1_x_change
            self.1_y_pos = self.1_y_pos + self.1_y_change
            self.1_image_label.place(x=self.1_x_pos, 
                                            y=self.1_y_pos)
            
        else:
            pass
        self.after(3, self.tick)

    # the 1 image
    def add_1_image_label(self):
        self.1_image_label = Label()
        self.1_image_label.place(x=self.1_x_pos,
                                    y=self.1_y_pos)
        self.1_image_label.configure(image=self.1_image)

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 