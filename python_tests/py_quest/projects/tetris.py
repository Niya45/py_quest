import random
import time
import os
from dataclasses import dataclass
from typing import List, Tuple

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

@dataclass
class Tetromino:
    shape: List[List[int]]
    position: Tuple[int, int]
    
    def rotate(self):
        # Rotate the shape 90 degrees clockwise
        return list(zip(*self.shape[::-1]))

class Tetris:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = None
        self.game_over = False
        self.score = 0
        
    def new_piece(self):
        shape = random.choice(SHAPES)
        position = (0, self.width // 2 - len(shape[0]) // 2)
        self.current_piece = Tetromino(shape, position)
        
    def valid_move(self, piece: Tetromino) -> bool:
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    board_y = piece.position[0] + y
                    board_x = piece.position[1] + x
                    if (board_x < 0 or board_x >= self.width or 
                        board_y >= self.height or 
                        (board_y >= 0 and self.board[board_y][board_x])):
                        return False
        return True
    
    def merge_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    board_y = self.current_piece.position[0] + y
                    board_x = self.current_piece.position[1] + x
                    if board_y >= 0:
                        self.board[board_y][board_x] = 1
    
    def clear_lines(self):
        lines_cleared = 0
        for y in range(self.height):
            if all(self.board[y]):
                del self.board[y]
                self.board.insert(0, [0 for _ in range(self.width)])
                lines_cleared += 1
        self.score += lines_cleared * 100
    
    def move_down(self):
        new_position = (self.current_piece.position[0] + 1, self.current_piece.position[1])
        new_piece = Tetromino(self.current_piece.shape, new_position)
        if self.valid_move(new_piece):
            self.current_piece = new_piece
            return True
        return False
    
    def move_sideways(self, direction):
        new_position = (self.current_piece.position[0], 
                       self.current_piece.position[1] + direction)
        new_piece = Tetromino(self.current_piece.shape, new_position)
        if self.valid_move(new_piece):
            self.current_piece = new_piece
    
    def rotate(self):
        rotated_shape = self.current_piece.rotate()
        new_piece = Tetromino(rotated_shape, self.current_piece.position)
        if self.valid_move(new_piece):
            self.current_piece = new_piece
    
    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {self.score}\n")
        
        # Create a temporary board with the current piece
        temp_board = [row[:] for row in self.board]
        if self.current_piece:
            for y, row in enumerate(self.current_piece.shape):
                for x, cell in enumerate(row):
                    if cell:
                        board_y = self.current_piece.position[0] + y
                        board_x = self.current_piece.position[1] + x
                        if 0 <= board_y < self.height and 0 <= board_x < self.width:
                            temp_board[board_y][board_x] = 2
        
        # Draw the board
        print("+" + "-" * self.width + "+")
        for row in temp_board:
            print("|" + "".join("█" if cell == 2 else "■" if cell == 1 else " " for cell in row) + "|")
        print("+" + "-" * self.width + "+")
        print("\nControls: ← → to move, ↑ to rotate, ↓ to drop faster")

def main():
    game = Tetris()
    game.new_piece()
    
    while not game.game_over:
        game.draw()
        
        # Simple input handling
        try:
            import msvcrt  # Windows
            if msvcrt.kbhit():
                key = msvcrt.getch().decode()
                if key == 'q':
                    break
                elif key == '\xe0':  # Arrow key prefix
                    key = msvcrt.getch().decode()
                    if key == 'H':  # Up
                        game.rotate()
                    elif key == 'P':  # Down
                        game.move_down()
                    elif key == 'K':  # Left
                        game.move_sideways(-1)
                    elif key == 'M':  # Right
                        game.move_sideways(1)
        except ImportError:
            import sys
            import tty
            import termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                key = sys.stdin.read(1)
                if key == 'q':
                    break
                elif key == '\x1b':  # Arrow key prefix
                    key = sys.stdin.read(2)
                    if key == '[A':  # Up
                        game.rotate()
                    elif key == '[B':  # Down
                        game.move_down()
                    elif key == '[D':  # Left
                        game.move_sideways(-1)
                    elif key == '[C':  # Right
                        game.move_sideways(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        # Move piece down automatically
        if not game.move_down():
            game.merge_piece()
            game.clear_lines()
            game.new_piece()
            if not game.valid_move(game.current_piece):
                game.game_over = True
        
        time.sleep(0.1)

if __name__ == "__main__":
    main() 