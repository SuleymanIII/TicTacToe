import customtkinter as ctk
from TSettings import *
from TButtons import ModeChooseButton, GameButton, StatButton
from PIL import Image

#CONFIG SCREEN PANELS
class ModeChoose(ctk.CTkFrame):
    def __init__(self, parent, game_mode):
        super(ModeChoose, self).__init__(parent, fg_color= 'transparent')
        self.columnconfigure((0,2), weight= 2, uniform= 'a')
        self.columnconfigure(1, weight= 1, uniform= 'a')
        self.rowconfigure(0, weight= 1)
        self.game_mode: ctk.StringVar = game_mode
        
        self.pvp_button = ModeChooseButton(self, text= 'PVP', func= self.pvp_selected, col= 0, sticky= 'nse')
        self.pvb_button = ModeChooseButton(self, text= 'PVBot', func= self.pvbot_selected, col= 2, sticky= 'nsw')
        self.pvp_selected()
        
        self.grid(row = 1, column = 0, sticky = 'nsew', pady = 10)
    
    def pvp_selected(self):
        self.game_mode.set(value= 'PVP')
        self.fade_button(self.pvb_button, self.pvp_button)
    
    def pvbot_selected(self):
        self.game_mode.set(value='PVB')
        self.fade_button(self.pvp_button, self.pvb_button)
        
    def fade_button(self, unselected_button:ctk.CTkButton, selected_button:ctk.CTkButton):
        unselected_button.configure(fg_color = PURPLE_FADED)
        selected_button.configure(fg_color = PURPLE)
        
class SignChoose(ctk.CTkFrame):
    def __init__(self, parent, player_sign):
        super(SignChoose, self).__init__(parent, fg_color= 'transparent')
        self.player_sign: ctk.StringVar = player_sign
        
        label = ctk.CTkLabel(self, text= 'Choose your sign:', font= (FONT, SIGN_CHOOSE_LABEL_SIZE), text_color=GREY)
        label.place(relx = 0.5, rely = 0.2, anchor = 'center')
        
        check_button_x = ctk.CTkCheckBox(self, text= 'X', 
                                        width= 50, 
                                        height= 50, 
                                        font= (FONT, SWITCH_FONT_SIZE), 
                                        checkbox_width=40, 
                                        checkbox_height=40,
                                        border_color= PURPLE,
                                        border_width= 5,
                                        hover_color= PURPLE_BLUE,
                                        fg_color=PURPLE_BLUE,
                                        variable= self.player_sign,
                                        onvalue='X',
                                        offvalue='O',
                                        command= lambda: self.click('X'))

        check_button_o = ctk.CTkCheckBox(self, text= 'O', 
                                        width= 50, 
                                        height= 50, 
                                        font= (FONT, SWITCH_FONT_SIZE), 
                                        checkbox_width=40, 
                                        checkbox_height=40,
                                        border_color= PURPLE,
                                        border_width= 5,
                                        hover_color= PURPLE_BLUE,
                                        fg_color=PURPLE_BLUE,
                                        variable= self.player_sign,
                                        onvalue='O',
                                        offvalue='X',
                                        command= lambda: self.click('O'))

        check_button_x.place(relx = 0.39, rely = 0.6, anchor = 'center')
        check_button_o.place(relx = 0.64, rely = 0.6, anchor = 'center')
        
        self.grid(row = 2, column = 0, pady = 10, sticky = 'new')
        
    def click(self, value):
        self.player_sign.set(value= value)     
        
class AgentChoose(ctk.CTkFrame):
    def __init__(self, parent, agent_types, agent_type):
        super(AgentChoose, self).__init__(parent, fg_color= 'transparent')
        self.agent_type = agent_type
        label = ctk.CTkLabel(self, text= 'Choose your agent type:', font= (FONT, SIGN_CHOOSE_LABEL_SIZE), text_color=GREY)
        label.pack()
        
        segbut = ctk.CTkSegmentedButton(self, 
                                        values= agent_types, 
                                        font=(FONT, SWITCH_FONT_SIZE), 
                                        selected_color= PURPLE_BLUE, 
                                        fg_color=PURPLE, 
                                        unselected_color= BACKGROUND_COLOR,
                                        variable=self.agent_type)
        segbut.pack(pady = 20)
        
        self.grid(row = 3, column = 0, sticky = 'nsew')       

#GAME FRAME PANELS
class GameButtonPanel(ctk.CTkFrame):
    def __init__(self, parent, func):
        super(GameButtonPanel, self).__init__(parent)
        self.rowconfigure((0,1,2), weight= 1, uniform= 'a')
        self.columnconfigure((0,1,2), weight= 1, uniform= 'a')
        
        for _, data in BUTTONS.items():
            GameButton(self,
                       row = data['row'],
                       col = data['col'],
                       func= func)
        
        self.grid(row = 1, column = 1, sticky = 'nsew')

class ScorePanel(ctk.CTkFrame):
    def __init__(self, parent, game_vars):
        super(ScorePanel, self).__init__(parent, fg_color= 'transparent')
        self.rowconfigure(0, weight= 1)
        self.columnconfigure((0,1,2), weight= 1, uniform= 'a')
        self.X_wins = game_vars['player_X_wins'].get()
        self.O_wins = game_vars['player_O_wins'].get()
        self.ties = game_vars['ties'].get()
        
        label_X = ctk.CTkLabel(self, text= f'Player X wins: {self.X_wins}', font=(FONT, SWITCH_FONT_SIZE))
        label_tie = ctk.CTkLabel(self, text= f'Tie(s): {self.ties}', font=(FONT, SWITCH_FONT_SIZE))
        label_O = ctk.CTkLabel(self, text= f'Player O wins: {self.O_wins}', font=(FONT, SWITCH_FONT_SIZE))
        
        label_X.grid(row = 0, column = 0, sticky = 'ew')
        label_tie.grid(row = 0, column = 1, sticky = 'ew')
        label_O.grid(row = 0, column = 2, sticky = 'ew')
        
        self.grid(row = 2, column = 0, columnspan = 3,sticky = 'nsew')
        
#STATS FRAME PANELS     
class StatLabelsPanel(ctk.CTkFrame):
    def __init__(self, parent, game_vars):
        super(StatLabelsPanel, self).__init__(parent)
        self.rowconfigure((0,1,2,3,4,5), weight= 4, uniform= 'a')
        self.columnconfigure(0, weight= 1, uniform= 'a')
        self.agent = 'None'
        if game_vars['game_mode'].get() == 'PVB':
            self.agent = game_vars['agent_type'].get()
            
        
        self.games_played = ctk.CTkLabel(self, text= f'games_played: {game_vars["games_played"].get()}', font=(FONT, QUIT_SIZE), text_color= GREY)
        self.games_won_x = ctk.CTkLabel(self, text= f'games won by X: {game_vars["player_X_wins"].get()}', font=(FONT, QUIT_SIZE), text_color= GREY)
        self.games_won_y = ctk.CTkLabel(self, text= f'games won by O: {game_vars["player_O_wins"].get()}', font=(FONT, QUIT_SIZE), text_color= GREY)
        self.games_tied = ctk.CTkLabel(self, text= f'Games tied: {game_vars["ties"].get()}', font=(FONT, QUIT_SIZE), text_color= GREY)
        self.agent_type = ctk.CTkLabel(self, text= f'agent type: {self.agent}', font=(FONT, QUIT_SIZE), text_color= GREY)
        self.difficulty = ctk.CTkLabel(self, text= f'Agent difficulty: NA', font=(FONT, QUIT_SIZE), text_color= GREY)
        
        self.games_played.grid(row = 0, column = 0, sticky = 'w')
        self.games_won_x.grid(row = 1, column = 0, sticky = 'w')
        self.games_won_y.grid(row = 2, column = 0, sticky = 'w')
        self.games_tied.grid(row = 3, column = 0, sticky = 'w')
        self.agent_type.grid(row = 4, column = 0, sticky = 'w')
        self.difficulty.grid(row = 5, column = 0, sticky = 'w')
        
        
        self.grid(row = 0, column = 0, sticky = 'nsew')
        
class StatButtonspanel(ctk.CTkFrame):
    def __init__(self, parent, app_class, main_func, play_func):
        super(StatButtonspanel, self).__init__(parent)
        self.rowconfigure(0, weight= 1)
        self.columnconfigure((0,1,2), weight= 1, uniform='a')
        
        

        self.main_manu = StatButton(self,text= 'Main Menu' ,func = lambda: main_func(parent), row= 0, col= 0)
        self.play_again = StatButton(self,text= 'Play Again' ,func = lambda: play_func(parent), row= 0, col= 1)
        self.quit_game = StatButton(self,text= 'Quit Game' ,func = lambda: app_class.destroy(), row= 0, col= 2)

        self.grid(row = 1, column = 0, sticky = 'nsew')
        
class PostGamePanel(ctk.CTkFrame):
    def __init__(self, parent, quit_func, retry_func, next_player, tie, game_vars):
        super(PostGamePanel, self).__init__(parent)
        self.rowconfigure((0,1,2,3), weight= 1, uniform= 'a')
        self.columnconfigure(0, weight= 1, uniform= 'a')
        
        if tie:
            win_label = ctk.CTkLabel(self, text= f'TIE!!', font=(FONT, SIGN_CHOOSE_LABEL_SIZE)).grid(row = 0, column = 0)
            game_vars['ties'].set(value = game_vars['ties'].get()+1)
            game_vars['games_played'].set(value = game_vars['games_played'].get()+1)
        else:
            winner = 'X' if next_player == 'O' else 'O'
            if winner == 'X':                   
                game_vars['player_X_wins'].set(value = game_vars['player_X_wins'].get()+1)
                game_vars['player_sign'].set(value = winner)
            else:
                game_vars['player_O_wins'].set(value = game_vars['player_O_wins'].get()+1)
                game_vars['player_sign'].set(value = winner)
                
            game_vars['games_played'].set(value = game_vars['games_played'].get()+1)
            win_label = ctk.CTkLabel(self, text= f'Player with sign: {winner} HAS WON!!', font=(FONT, SIGN_CHOOSE_LABEL_SIZE)).grid(row = 0, column = 0)
        
        quit_button = StatButton(self,text= 'Quit', func= lambda: quit_func(parent), row= 1, col= 0)
        replay_button = StatButton(self,text='Play Again', func= lambda: retry_func(parent), row= 2, col= 0)
        
        self.grid(row = 1, column = 1, sticky = 'nsew')