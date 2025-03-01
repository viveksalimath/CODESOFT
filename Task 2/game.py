from typing import List, Tuple, Optional

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
        
    def print_board(self):
        for i in range(0, 9, 3):
            print(f'{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}')
            if i < 6:
                print('---------')
    
    def available_moves(self) -> List[int]:
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def make_move(self, position: int, player: str) -> None:
        self.board[position] = player
    
    def check_winner(self) -> Optional[str]:
        # Check rows, columns and diagonals
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ' '):
                return self.board[combo[0]]
        
        if ' ' not in self.board:
            return 'Tie'
        return None
    
    def minimax(self, board: List[str], is_maximizing: bool) -> int:
        result = self.check_winner()
        if result == self.ai:
            return 1
        if result == self.human:
            return -1
        if result == 'Tie':
            return 0
            
        if is_maximizing:
            best_score = float('-inf')
            for move in self.available_moves():
                self.board[move] = self.ai
                score = self.minimax(self.board, False)
                self.board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                self.board[move] = self.human
                score = self.minimax(self.board, True)
                self.board[move] = ' '
                best_score = min(score, best_score)
            return best_score
    
    def get_best_move(self) -> int:
        best_score = float('-inf')
        best_move = 0
        
        for move in self.available_moves():
            self.board[move] = self.ai
            score = self.minimax(self.board, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
