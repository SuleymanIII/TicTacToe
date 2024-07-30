from Board import Board
def main():
    player='X'
    game_board = Board(player)
    game_board.print_board()
    game_not_finished = True
    while(game_not_finished):
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


        valid_move, player = game_board.make_move(row, col, player)
        
        if not valid_move:
            print(f"player: {player} made an invalid move please select an available square.")
            continue
        else:
            game_board.print_board()
        
        win, tie = game_board.check_game_state()
        if win:   
            player = 'O' if player == 'X' else 'X'
            print(f"player: {player} won the game well done!")
            game_not_finished = False
            
        if tie:
            print(f"ITS A TIE!")
            game_not_finished = False
            
        
        

    
if __name__ == "__main__":
    main()