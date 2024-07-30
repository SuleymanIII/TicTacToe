import customtkinter as ctk
from TSettings import *

class ModeChooseButton(ctk.CTkButton):
    def __init__(self, parent, text, func, col, sticky):
        super(ModeChooseButton, self).__init__(parent,
                                     text= text,
                                     command= func,
                                     fg_color= PURPLE,
                                     font=(FONT, SWITCH_FONT_SIZE),
                                     hover_color= PURPLE_BLUE)
        self.grid(row = 0, column = col, sticky = sticky)
        
class ActionButton(ctk.CTkButton):
    def __init__(self, parent, text, func, row, col, width = None):
        super(ActionButton, self).__init__(parent, 
                                           text= text,
                                           command= func, 
                                           fg_color= PURPLE, 
                                           hover_color=PURPLE_BLUE, 
                                           font=(FONT, SWITCH_FONT_SIZE))
        if width:
            self.configure(width = width)
        
        self.grid(row = row, column = col, sticky = 's')
        
class GameButton(ctk.CTkButton):
    def __init__(self, parent, func, row, col, image = None):
        super(GameButton, self).__init__(parent, 
                                         text= ' ',
                                         command= lambda: func(self, row, col),
                                         image= image,
                                         fg_color= PURPLE,
                                         font=(FONT, SWITCH_FONT_SIZE),
                                         hover_color= PURPLE_BLUE,
                                         border_color='black',
                                         border_width= 5)
        
        self.grid(row = row, column = col, sticky = 'nsew')

class QuitButton(ctk.CTkButton):
    def __init__(self, parent, func):
        super(QuitButton, self).__init__(parent,
                                         text= f'Quit',
                                         command= lambda: func(parent), 
                                         fg_color= DARK_GREY,
                                         width= 80,
                                         font=(FONT, QUIT_SIZE),
                                         text_color= GREY,
                                         border_width= 5,
                                         border_color='black')
        
        
        self.place(relx = 0.88, rely = 0.017)
        
        
class StatButton(ctk.CTkButton):
    def __init__(self, parent, text, func, row, col):
        super(StatButton, self).__init__(parent,
                                         text= text,
                                         command= func,
                                         font=(FONT, QUIT_SIZE),
                                         text_color= GREY,
                                         fg_color=PURPLE,
                                         hover_color=PURPLE_BLUE,
                                         height= 50, 
                                         width= 160)
        
        
        
        
        self.grid(row = row, column = col, padx = 5, pady = 2)
        