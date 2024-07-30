from abc import ABC, abstractmethod
from random import choice
from Board import Board
import copy

class Agent(ABC):
    def __init__(self, board, current_player):
        self.board:Board = board
        self.current_player = current_player

        
    @abstractmethod
    def evaluate_board(self, board, current_player): #random agent will find all available coords and make them into a list of tuples to be passed to make move passed to main
        pass
    
    @abstractmethod #random_agent will return row, col  tuple randomly from tuple list 
    def make_move(self):
        pass
    
    def update_board(self, board):
        self.board = board
        
        
class RandomAgent(Agent):
    def __init__(self, board, current_player):
        super().__init__(board, current_player)

        
    def evaluate_board(self):
        return [(row, col) for row in range(3) for col in range(3) if self.board.board[row][col] == ' ']

    
    def make_move(self):
        possible_moves = self.evaluate_board()
        return choice(possible_moves)
    
class MiniMaxAgent(Agent):
    def __init__(self, board, depth, current_player, alpha, beta):
        super(MiniMaxAgent, self).__init__(board, current_player)
        self.depth = depth
        self.alpha = alpha
        self.beta = beta
        
    def evaluate_board(self, virtual_board: Board, current_player): #when exploring game states we evaluate from if X won in that state or O pass it during minimax exploration
        #POSITIVE FAVOURS X NEGATIVE FAVOURS O
        score = 0
        #switching is done to check whether the last player won as my board only returns the boolean for if there was a win or not.
        agent_sign = 'X' if current_player == 'O' else 'O'
        game_won, tie = virtual_board.check_game_state()
        if game_won:
            return float(10) if agent_sign == 'X' else float(-10) 
        elif tie:
            return 0
        else:
            for row in virtual_board.board:
                for cell in row:
                    if cell == 'X':
                        score += 1
                    elif cell == 'O':
                        score -= 1
        return score
    
    def make_move(self):
        best_move = self.mini_max(self.board, self.depth, self.current_player, self.alpha, self.beta)
        score, coordinates = best_move
        return score, coordinates
    
    def available_moves(self, virtual_board):
        return [(row, col) for row in range(3) for col in range(3) if virtual_board.board[row][col] == ' ']
         
    
    def mini_max(self, board:Board, depth, agent_sign, alpha, beta):
        game_won, tie = board.check_game_state()
        if depth == 0 or game_won or tie:
            state_eval = self.evaluate_board(board, agent_sign)
            return state_eval, None
        #extra logic to complete minimax still in progress below are placeholders
        if agent_sign == 'X':
            max_eval = (float('-inf'), None)
            available_moves = self.available_moves(board)
            for move in available_moves:
                #now we generate call stack and propagate values up from basecase
                new_board:Board = copy.deepcopy(board)
                _, next_child = new_board.make_move(move[0],move[1], agent_sign)
                value = self.mini_max(new_board, depth -1, next_child, alpha, beta)
                if value[0] > max_eval[0]:
                    max_eval = (value[0], move)
                alpha = max(alpha, value[0])
                if beta < alpha:
                    break
                    
            return max_eval
                
        
        if agent_sign == 'O':
            min_eval = (float('inf'), None)
            available_moves = self.available_moves(board)
            for move in available_moves:
                #now we generate call stack and propagate values up from basecase
                new_board:Board = copy.deepcopy(board)
                _, next_child = new_board.make_move(move[0],move[1], agent_sign)
                value = self.mini_max(new_board, depth -1, next_child, alpha, beta)
                if value[0] < min_eval[0]:
                    min_eval = (value[0], move)
                beta = min(beta, value[0])
                if beta < alpha:
                    break
            print(min_eval[0])
            return min_eval
    
class MCTS_Agent(Agent):
    #UCB1 = (w_i / n_i) + C * sqrt(ln(N) / n_i)
        # Where:
        # w_i is the total value of the node
        # n_i is the number of visits to the node
        # N is the total number of visits to the parent node
        # C = exploration parameter (often sqrt(2))
        
    def __init__(self, board, current_player, rollout_depth_max): #STILL TODO BEFORE STARTING MCTS IS IMPLEMENT NODE STRUCTURE FOR TREE
        super(MCTS_Agent, self).__init__(board, current_player)
        
    @abstractmethod
    def evaluate_board(self, board:Board, current_player): #returns the score when rollout hits basecase (win, tie)
        pass
    
    @abstractmethod #mcts agent will return row, col  tuple after calling mcts method 
    def make_move(self):
        pass
    
    def mcts(self): #main mcts logic will happen here controlling when selection, expansion, rollout and backpropagation happen
        pass
    
    def rollout(self): #handles the rollout from a gamestate this will playout like a random agent until terminal state is reached. (limited by a max depth)
        pass
    
    def available_moves(self, board:Board): #returns available moves will be used during rollout.
        return [(row, col) for row in range (3) for col in range(3) if board.board[row][col] == ' ']