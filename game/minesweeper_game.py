"""Module for minesweeper game logic."""
import random
from collections import deque

class MinesweeperGame:
    def __init__(self, rows, cols, mines):
        """Initialize a game."""
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = self.initialize_board()
        self.revealed_cells = [[False] * cols for _ in range(rows)]
        self.flags = [[False] * cols for _ in range(rows)]
        self.game_over = False
        self.remaining_tiles = rows * cols - mines
    
    def initialize_board(self):
        """Initialize an empy board."""
        board = [[0] * self.cols for _ in range(self.rows)]

        # Randomly disperse mines throughout board
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for position in mine_positions:
            row = position // self.cols
            col = position % self.cols
            board[row][col] = -1
        
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == 0:
                    board[row][col] = self.calculate_number(row, col, board)
        
        return board
    
    def calculate_number(self, row, col, board):
        """Calculate the number for a cell."""
        count = 0
        for i in range(max(0, row-1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if board[i][j] == -1:
                    count += 1

        return count
    
    def reveal_connected_cells(self, row, col):
        visited = set()
        queue = deque([(row, col)])

        while queue:
            current_row, current_col = queue.popleft()

            if (current_row, current_col) in visited:
                continue

            visited.add((current_row, current_col))

            if self.board[current_row][current_col] == 0:
                self.revealed_cells[current_row][current_col] = True
                self.remaining_tiles -= 1
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        new_row, new_col = current_row + dr, current_col + dc
                        if (
                            0 <= new_row < self.rows
                            and 0 <= new_col < self.cols
                            and (new_row, new_col) not in visited
                        ):
                            queue.append((new_row, new_col))
                            # Reveal outermost edge of non-mines
                            if self.board[new_row][new_col] > 0:
                                self.revealed_cells[new_row][new_col] = True
                        
                     

    def reveal_cell(self, row, col):
        """Reveal a cell."""
        if self.board[row][col] == 0:
            self.reveal_connected_cells(row, col)
    
        if self.board[row][col] == -1:
            self.game_over = True
        
        self.revealed_cells[row][col] = True
        self.remaining_tiles -= 1
    
    def flag_cell(self, row, col):
        """Flag a cell."""
        if self.flags[row][col]:
            self.flags[row][col] = False
        else:
            self.flags[row][col] = True