import customtkinter as ctk
from TSettings import *
from TPanels import ModeChoose, SignChoose, AgentChoose, GameButtonPanel, ScorePanel, StatLabelsPanel, StatButtonspanel, PostGamePanel
from TButtons import ActionButton, QuitButton
from PIL import Image
from Board import Board

class StartMenu(ctk.CTkFrame):
    def __init__(self, parent, agent_types, start_func, game_mode, player_sign, agent_type):
        super(StartMenu, self).__init__(parent)

        #Layout
        self.rowconfigure((0,4), weight= 1, uniform= 'a')
        self.rowconfigure((1,2,3), weight= 2, uniform= 'a')
        self.columnconfigure(0, weight= 1)
        
        #Widgets
        tic_tac_toe_label = ctk.CTkLabel(self, text= 'TicTacToe APP', font=(FONT, MAINSCREEN_TEXT_SIZE))
        tic_tac_toe_label.grid(row = 0, column = 0, pady = 10)
        mode_panel = ModeChoose(self, game_mode)
        sign_panel = SignChoose(self, player_sign)
        self.agent_panel = None

        game_mode.trace_add('write', lambda *args: self.pack_agent_types(game_mode, agent_types, agent_type))
        
        button = ActionButton(self, 'Start Game', func= start_func, row = 4, col= 0, width= 350)
        
        self.pack(expand = True, fill = 'both')
    
    def pack_agent_types(self, game_mode, agent_types, agent_type, *args):
        if game_mode.get() == 'PVB':
            if self.agent_panel is None:
                self.agent_panel = AgentChoose(self, agent_types, agent_type)
                self.agent_panel.grid(row=3, column=0, sticky='nsew')
        else:
            if self.agent_panel is not None:
                self.agent_panel.grid_forget()  # Remove from grid instead of destroying
                self.agent_panel = None        

class GameFrame(ctk.CTkFrame):
    #gets all game params set by startframe
    def __init__(self, parent, quit_func,again_func, game_vars):
        super(GameFrame, self).__init__(parent)
        self.game_vars = game_vars
        self.board = Board(game_vars['player_sign'])
        
        self.columnconfigure((0,2), weight= 1, uniform= 'a')
        self.columnconfigure(1, weight= 6, uniform= 'a')
        self.rowconfigure(0, weight= 1, uniform= 'a')
        self.rowconfigure(1, weight= 50, uniform= 'a')
        self.rowconfigure(2, weight= 9, uniform= 'a')
        
        self.game_buttons = GameButtonPanel(self, func= self.on_button_click)
     
        self.score_frame = ScorePanel(self, game_vars)
        self.quit_button = QuitButton(self, quit_func)
        
        self.trace_id = self.game_vars['game_finished'].trace_add('write', lambda *args:self.swap_post_game_panel(quit_func, again_func))
        
        self.pack(expand = True, fill = 'both')
    
    def on_button_click(self, button: ctk.CTkButton, row, col):
        if not self.game_vars['game_finished'].get():
            
            if button.cget('image') is None:  
                current_player = self.game_vars['player_sign'].get()
                if current_player == 'X':
                    image_path = IMAGE_PATH['X']
                else:
                    image_path = IMAGE_PATH['O']

            
                pil_image = Image.open(image_path)
                image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(140, 140))
            
                _, player = self.board.make_move(row= row,
                                                      col= col,
                                                      current_player= current_player)
            
                self.board.print_board()
                self.game_vars['player_sign'].set(value = player)
                
                finished, self.tie = self.board.check_game_state()
                button.configure(image=image, state='disabled') 
                if finished:
                    self.game_vars['game_finished'].set(value = finished)
                
                if self.tie:
                    self.game_vars['game_finished'].set(value = self.tie)
                
                         
    def swap_post_game_panel(self,quit_func,again_func ,*args):
        print(self.tie)
        self.game_vars['game_finished'].trace_remove('write', self.trace_id)
        self.game_buttons.destroy()
        self.post_game_panel = PostGamePanel(self, quit_func= quit_func, retry_func= again_func, next_player= self.game_vars['player_sign'].get(), tie = self.tie, game_vars = self.game_vars)  
        
    
        
        
class StatsFrame(ctk.CTkFrame):
    def __init__(self, parent, game_vars, main_func, play_func):
        super(StatsFrame, self).__init__(parent)
        self.rowconfigure(0, weight= 24, uniform= 'a')
        self.rowconfigure(1, weight= 6, uniform= 'a')
        self.columnconfigure(0, weight= 1, uniform= 'a')
        
        label_panel = StatLabelsPanel(self, game_vars)
        button_panel = StatButtonspanel(self, app_class = parent, main_func=main_func, play_func = play_func)
        
        self.pack(expand = True, fill = 'both')

        