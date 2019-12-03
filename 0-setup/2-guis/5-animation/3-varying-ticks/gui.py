from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.figure1_image = PhotoImage(file="c:/Data/figure1-2.gif")
        self.figure2_image = PhotoImage(file="c:/Data/figure2-2.gif")
        self.figure3_image = PhotoImage(file="c:/Data/figure3-2.gif")

        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.figure1_x_pos = 0
        self.figure1_y_pos = 0
        self.figure1_x_change = 1
        self.figure1_y_change = 0
        self.figure2_x_pos =0
        self.figure2_y_pos = 200
        self.figure2_x_change = 1
        self.figure2_y_change = 0
        self.figure3_x_pos =0
        self.figure3_y_pos =400
        self.figure3_x_change = 1
        self.figure3_y_change = 0
        self.num_ticks = 0

        # add components
        self.add_figure1_image_label()
        self.add_figure2_image_label()
        self.add_figure3_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.num_ticks = self.num_ticks + 1

        #Person 1
        if (self.num_ticks % 5 == 0):
            #Check right side
            if(self.figure1_x_pos >469):
                self.figure1_x_change = -1

            #Check left side
            if(self.figure1_x_pos <0):
                self.figure1_x_change = 1

            #Move person 1
            self.figure1_x_pos = self.figure1_x_pos + self.figure1_x_change
            self.figure1_y_pos = self.figure1_y_pos + self.figure1_y_change
            self.figure1_image_label.place(x=self.figure1_x_pos, 
                                            y=self.figure1_y_pos)

        #Person 2
        if (self.num_ticks % 10 == 0):
            #Check right side
            if(self.figure2_x_pos >469):
                self.figure2_x_change = -1

            #Check left side
            if(self.figure2_x_pos <0):
                self.figure2_x_change = 1

            #Move person 2
            self.figure2_x_pos = self.figure2_x_pos + self.figure2_x_change
            self.figure2_y_pos = self.figure2_y_pos + self.figure2_y_change
            self.figure2_image_label.place(x=self.figure2_x_pos, 
                                            y=self.figure2_y_pos)
            
        #Person 3
        if (self.num_ticks % 2 == 0):
            #Check right side
            if(self.figure3_x_pos >469):
                self.figure3_x_change = -1

            #Check left side
            if(self.figure3_x_pos <0):
                self.figure3_x_change = 1

            #Move person 3
            self.figure3_x_pos = self.figure3_x_pos + self.figure3_x_change
            self.figure3_y_pos = self.figure3_y_pos + self.figure3_y_change
            self.figure3_image_label.place(x=self.figure3_x_pos, 
                                            y=self.figure3_y_pos)
            
        else:
            pass
        self.after(3, self.tick)

    # the figure1 image
    def add_figure1_image_label(self):
        self.figure1_image_label = Label()
        self.figure1_image_label.place(x=self.figure1_x_pos,
                                    y=self.figure1_y_pos)
        self.figure1_image_label.configure(image=self.figure1_image)

    # the figure2 image
    def add_figure2_image_label(self):
        self.figure2_image_label = Label()
        self.figure2_image_label.place(x=self.figure2_x_pos,
                                    y=self.figure2_y_pos)
        self.figure2_image_label.configure(image=self.figure2_image)

    # the figure3 image
    def add_figure3_image_label(self):
        self.figure3_image_label = Label()
        self.figure3_image_label.place(x=self.figure3_x_pos,
                                    y=self.figure3_y_pos)
        self.figure3_image_label.configure(image=self.figure3_image)

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 