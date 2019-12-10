#Cross and ticks - 
#Use of LEN - \2-guis\1-classes-and-objects\


#OptionMenu [no import] - TCA1 part_b2
#
#Combobox [Need: from tkinter import ttk] - TCA2 part c1.py
#
#Listbox [no import] - 2-guis\3-events\2-listbox
#
#MessageBox [Need: from tkinter import messagebox] 2-guis\3-events\1-button


#Options:
#pady=10,  padx=10,  row=0,  column=0, columnspan=2  
#bd=3 [borderwidth], 


#Button configure options:
#        self.a_button.configure(    text = "Subscribe",
#                                    font = "Arial 8",
#                                   underline = 0,
#                                    justify = CENTER,
#                                    width = 62)

#Label configure options:
#        self.box_label.configure(   font = "Arial 10",
#                                    text="Email:")

#Entry configure options:
#        self.inner_frame.configure( font = "Arial 10",
#                                    width = 40)

#Listbox    def __add_lyric_scrollbox(self):
        #Create
#        self.lyric_scrollbox = Listbox()
#        self.lyric_scrollbox.grid(row=4, column=0)
#        #Style
#        self.lyric_scrollbox.configure(  height=2,
#                                      width=40)


#EVENTS:
#self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)[RC: 1=left button release, 2=middle, 3=right]
#def __buy_button_clicked(self, event):

#"<KeyRelease>"
#"<FocusOut>" - [see 4-hiding-and-showing] kbd focus was moved from this widget to another widget
#<FocusIn> - kbd focus was moved to this widget

#<B1-Motion> - mouse moved with button 1 held down
#<Double-button-1> - button 1 was double clicked
#<Button-1> - when mouse button pressed over a widget - can be moved away and subsequently can invoke other events such as ButtonRelease
#<Enter> - the mouse pointer entered a widget
#<Leave> - the mouse pointer left a widget
#<Return> - the user pressed the return key - can do this for many of the keys: e.g. Cancel (the break key), BackSpace, Tab, Shift_L, Control_L, Alt_L, Pause, Caps_Lock, Escape, Prior (Page up), Next (page down), End, Home, Left, Up, Down, Right, Print, Insert, Delete, F1, F2 - F12, Num_Lock and Scroll_Lock
#a - the user typed an "a" (note no brackets) - can use for most printable charactors except space and less - note 1 is kdb, <1> is mouse