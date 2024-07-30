from Board import Board
from Agent import RandomAgent, MiniMaxAgent
def main():
    human_player_sign = 'X'
    current_player = human_player_sign
    game_board = Board(current_player)
    game_board.print_board()
    game_not_finished = True
    while(game_not_finished):
        if current_player == human_player_sign:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))

            except ValueError:
                print("Invalid input. Please enter a valid integer.") 
                
            valid_move, current_player = game_board.make_move(row, col, current_player)
            if not valid_move:
                print(f"player: {current_player} made an invalid move please select an available square.")
                continue
            else:
                game_board.print_board()
        else:
            # random_agent = RandomAgent(game_board, current_player)
            # random_agent.evaluate_board()
            # coordinate = random_agent.make_move()
            
            minimax_agent = MiniMaxAgent(game_board, 8, current_player, float('-inf'), float('inf'))
            score, coordinate = minimax_agent.make_move()
            print(score)
            
            valid_move, current_player = game_board.make_move(coordinate[0], coordinate[1], current_player)
            if not valid_move:
                print(f"player: {current_player} made an invalid move please select an available square.")
                continue
            else:
                game_board.print_board()
        
        win, tie = game_board.check_game_state()
        if win:   
            current_player = 'O' if current_player == 'X' else 'X'
            print(f"player: {current_player} won the game well done!")
            game_not_finished = False
            
        if tie:
            print(f"ITS A TIE!")
            game_not_finished = False
            
    
if __name__ == "__main__":
    main()