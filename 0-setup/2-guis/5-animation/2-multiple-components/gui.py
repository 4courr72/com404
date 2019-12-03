from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball1_image = PhotoImage(file="c:/Data/football2.gif")
        self.ball2_image = PhotoImage(file="c:/Data/beachball2.gif")

        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball1_x_pos = 350
        self.ball1_y_pos = 0
        self.ball1_x_change = 1
        self.ball1_y_change = 1
        self.ball2_x_pos = 150
        self.ball2_y_pos = 0
        self.ball2_x_change = -1
        self.ball2_y_change = -1
        
        # add components
        self.add_ball1_image_label()
        self.add_ball2_image_label() 
        
        # start the timer
        self.tick1()
        self.tick2()
        
    # the timer tick function    
    def tick1(self):
        if(self.ball1_x_pos >469):
            self.ball1_x_change = -1

        elif(self.ball1_x_pos <1):
            self.ball1_x_change = 1
        else:
            pass

        if(self.ball1_y_pos >471):
            self.ball1_y_change = -1
        
        elif(self.ball1_y_pos <1):
            self.ball1_y_change = 1
        else:
            pass
        self.ball1_x_pos = self.ball1_x_pos + self.ball1_x_change
        self.ball1_y_pos = self.ball1_y_pos + self.ball1_y_change
        self.ball1_image_label.place(x=self.ball1_x_pos, 
                                    y=self.ball1_y_pos)
        self.after(10, self.tick1)

    def tick2(self):
        if(self.ball2_x_pos >469):
            self.ball2_x_change = -1

        elif(self.ball2_x_pos <1):
            self.ball2_x_change = 1
        else:
            pass

        if(self.ball2_y_pos >471):
            self.ball2_y_change = -1
        
        elif(self.ball2_y_pos <1):
            self.ball2_y_change = 1
        else:
            pass
        self.ball2_x_pos = self.ball2_x_pos + self.ball2_x_change
        self.ball2_y_pos = self.ball2_y_pos + self.ball2_y_change
        self.ball2_image_label.place(x=self.ball2_x_pos, 
                                    y=self.ball2_y_pos)
        self.after(5, self.tick2)

    # the ball1 image
    def add_ball1_image_label(self):
        self.ball1_image_label = Label()
        self.ball1_image_label.place(x=self.ball1_x_pos,
                                    y=self.ball1_y_pos)
        self.ball1_image_label.configure(image=self.ball1_image)

    # the ball2 image
    def add_ball2_image_label(self):
        self.ball2_image_label = Label()
        self.ball2_image_label.place(x=self.ball2_x_pos,
                                    y=self.ball2_y_pos)
        self.ball2_image_label.configure(image=self.ball2_image)

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 