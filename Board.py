class Board:
    def __init__(self, player_one):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = player_one
        
    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 9)
            
    def make_move(self, row, col, current_player):
        if not (0 <= row <= 2) or not (0 <= col <= 2):
            return False, current_player
        
        if self.board[row][col] == ' ':
            #move is valid proceed
            self.board[row][col] = current_player
            next_player = 'O' if current_player == 'X' else 'X'
            print(f'Move valid current player: {next_player}')
            return True, next_player
        else:
            #move invalid
            print(f'Move invalid current player: {current_player}')
            return False, current_player
        
    
    def check_game_state(self):
        game_won = False
        tie = False
        
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                game_won = True
        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                game_won = True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            game_won = True
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            game_won = True
        

        if not game_won:
            tie = True
            for row in self.board:
                for col in range(3):
                    if row[col] != ' ':
                        pass
                    else:
                        tie = False
                        break
                        
                

        
        return game_won, tie