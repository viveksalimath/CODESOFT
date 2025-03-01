from game import TicTacToe

def main():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe! You are X, AI is O")
    print("Positions are numbered 0-8, left to right, top to bottom")
    
    while True:
        game.print_board()
        
        # Human turn
        while True:
            try:
                position = int(input("Enter your move (0-8): "))
                if position in game.available_moves():
                    break
                print("Invalid move, try again")
            except ValueError:
                print("Please enter a number between 0-8")
        
        game.make_move(position, game.human)
        
        # Check if human won
        if game.check_winner() == game.human:
            game.print_board()
            print("You won! Congratulations!")
            break
        elif game.check_winner() == 'Tie':
            game.print_board()
            print("It's a tie!")
            break
            
        # AI turn
        ai_move = game.get_best_move()
        game.make_move(ai_move, game.ai)
        print(f"\nAI chose position {ai_move}")
        
        # Check if AI won
        if game.check_winner() == game.ai:
            game.print_board()
            print("AI wins!")
            break
        elif game.check_winner() == 'Tie':
            game.print_board()
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
