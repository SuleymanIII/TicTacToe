#text sizes
FONT = 'Calibri'
MAINSCREEN_TEXT_SIZE = 54
SIGN_CHOOSE_LABEL_SIZE = 35
GAME_STAT_LABEL_SIZE = 35
SWITCH_FONT_SIZE = 28
QUIT_SIZE = 18

#colors
PURPLE = '#4809FF'
PURPLE_FADED = '#96949d'
GREY = '#CCC'
PURPLE_BLUE = '#2E00D6'
BACKGROUND_COLOR = '#2f2f2f'
DARK_GREY = '#191919'

#app and widget sizes
APP_SIZE = (700,600)
APP_MINSIZE = (516, 478)
STATS_SIZE = (450, 300)
STATS_MINSIZE = (300,200)

#agent types
AGENT_TYPES = ['random_agent', 'minimax_agent', 'mcts_agent']

#button square positions
BUTTONS = {
    '0': {'row': 0, 'col': 0},
    '1': {'row': 0, 'col': 1},
    '2': {'row': 0, 'col': 2},
    '3': {'row': 1, 'col': 0},
    '4': {'row': 1, 'col': 1},
    '5': {'row': 1, 'col': 2},
    '6': {'row': 2, 'col': 0},
    '7': {'row': 2, 'col': 1},
    '8': {'row': 2, 'col': 2}
}
IMAGE_PATH = {'X': 'd:\\AI projects\\TicTacToe\\red_cross.png', 'O': 'd:\\AI projects\\TicTacToe\\yellow_circle.png'}

#DEFAULTS
START_SIGN_DEFAULT = 'X'
GAME_MODE_DEFAULT = 'PVP'
PLAYER_X_WINS_DEFAULT = 0
TIES_DEFAULT = 0
PLAYER_Y_WINS_DEFAULT = 0
GAMES_PLAYED_DEFAULT = 0
AGENT_TYPE_DEFAULT = AGENT_TYPES[0]
GAME_FINISHED_DEFAULT = False