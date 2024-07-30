import customtkinter as ctk
from PIL import Image
from TSettings import *
from TFrames import StartMenu, GameFrame, StatsFrame

class App(ctk.CTk):
    def __init__(self):
        super(App, self).__init__()
        #APP_CONFIGS
        self._set_appearance_mode('dark')
        self.title('TicTacToe')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}+{int(self.winfo_screenwidth()/2-APP_SIZE[0]/2)}+{int(self.winfo_screenheight()/2-APP_SIZE[1]/2)}')
        self.maxsize(APP_SIZE[0], APP_SIZE[1])
        self.minsize(APP_MINSIZE[0], APP_MINSIZE[1])
        self.init_params()
        self.start_frame = StartMenu(self, 
                                     AGENT_TYPES, 
                                     game_mode = self.game_mode, 
                                     player_sign= self.player_sign,
                                     agent_type= self.agent_type, 
                                     start_func= self.start_game)

        self.mainloop()
    
    def init_params(self):
        #init all the params here before adding them to the startmenu for config
        self.game_mode = ctk.StringVar(value= GAME_MODE_DEFAULT)
        self.player_sign = ctk.StringVar(value= START_SIGN_DEFAULT)
        self.agent_type = ctk.StringVar(value= AGENT_TYPE_DEFAULT)
        self.player_X_wins = ctk.IntVar(value= PLAYER_X_WINS_DEFAULT)
        self.player_O_wins = ctk.IntVar(value= PLAYER_Y_WINS_DEFAULT)
        self.ties = ctk.IntVar(value= TIES_DEFAULT)
        self.game_finished = ctk.BooleanVar(value= GAME_FINISHED_DEFAULT)
        self.games_played = ctk.IntVar(value = GAMES_PLAYED_DEFAULT)

        self.game_params = {
        'game_mode': self.game_mode,
        'player_sign': self.player_sign,
        'agent_type': self.agent_type,
        'player_X_wins': self.player_X_wins,
        'player_O_wins': self.player_O_wins,
        'ties': self.ties,
        'game_finished': self.game_finished,
        'games_played': self.games_played
    }
    
    def start_game(self):
        self.start_frame.destroy()
        self.game_frame = GameFrame(self, quit_func= self.quit_frame, again_func = self.play_again_func ,game_vars = self.game_params)
        print(f'Game Mode: {self.game_mode.get()} \n Player sign: {self.player_sign.get()} \n Agent type: {self.agent_type.get()}')
        
    def quit_frame(self, parent: ctk.CTkFrame):
        parent.destroy()
        self.stats_frame = StatsFrame(self, game_vars= self.game_params, main_func = self.main_menu_func, play_func = self.play_func_stat)
        self.maxsize(STATS_SIZE[0], STATS_SIZE[1])
        self.minsize(STATS_MINSIZE[0], STATS_MINSIZE[1])

    def play_again_func(self, parent):
        self.game_finished.set(value = GAME_FINISHED_DEFAULT)
        # print(f'Ties: {self.ties.get()} \n player_x_wins: {self.player_X_wins.get()} \n Player_O_wins: {self.player_O_wins.get()}')
        parent.destroy()
        self.game_frame = GameFrame(self, quit_func= self.quit_frame, again_func = self.play_again_func ,game_vars = self.game_params)

    def play_func_stat(self, parent_frame: ctk.CTkFrame):
        self.maxsize(APP_SIZE[0], APP_SIZE[1])
        self.minsize(APP_MINSIZE[0], APP_MINSIZE[1])
        self.player_X_wins.set(value= PLAYER_X_WINS_DEFAULT)
        self.player_O_wins.set(value= PLAYER_Y_WINS_DEFAULT)
        self.ties.set(value= TIES_DEFAULT)
        self.games_played.set(value = GAMES_PLAYED_DEFAULT)
        self.game_finished.set(value= GAME_FINISHED_DEFAULT)
        parent_frame.destroy()
        self.game_frame = GameFrame(self, quit_func= self.quit_frame, again_func = self.play_again_func ,game_vars = self.game_params)
        
    
    def main_menu_func(self, parent_frame: ctk.CTkFrame):
        self.init_params()
        self.maxsize(APP_SIZE[0], APP_SIZE[1])
        self.minsize(APP_MINSIZE[0], APP_MINSIZE[1])
        parent_frame.destroy()
        self.start_frame = StartMenu(self, 
                                     AGENT_TYPES, 
                                     game_mode = self.game_mode, 
                                     player_sign= self.player_sign,
                                     agent_type= self.agent_type, 
                                     start_func= self.start_game)
    
if __name__ == '__main__':
    App()
    
    