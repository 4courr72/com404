from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="c:/Data/football2.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 250
        self.ball_y_pos = 0
        self.ball_x_change = 1
        self.ball_y_change = 1
        
        # add components
        self.add_ball_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        #Can I put if/elif/else statements within the def? Tested it and yes - works! See my test in next 4 rem'd lines.
        #if(self.ball_x_pos > 499):
        #    print("Greater than 499!")
        #else:
        #    print("Still less than 499 :-()")

        #Note: the football2 image is 30x28 pixels
        if(self.ball_x_pos >469):
            self.ball_x_change = -1

        elif(self.ball_x_pos <1):
            self.ball_x_change = 1
        else:
            pass

        if(self.ball_y_pos >471):
            self.ball_y_change = -1
        
        elif(self.ball_y_pos <1):
            self.ball_y_change = 1
        else:
            pass

        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        self.after(10, self.tick)

    # the ball image
    def add_ball_image_label(self):
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        self.ball_image_label.configure(image=self.ball_image)

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 