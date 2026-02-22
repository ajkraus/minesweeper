"""Gameplay screen class."""
import pygame
from ui.screens.base_screen import BaseScreen
from game.minesweeper_game import MinesweeperGame

class Gameplay(BaseScreen):
    def __init__(self, ui, rows, cols, mines):
        super().__init__(ui)
        self.title = self.font.render("Gameplay", True, pygame.Color("blue"))

        self.title_rect = self.title.get_rect(center=(ui.screen_size[0] // 2, ui.screen_size[1] // 2))
        self.game = MinesweeperGame(rows, cols, mines)

        self.cell_image = pygame.image.load('static/tile.png')
        self.flag_image = pygame.image.load('static/flag.png')
        self.bomb_image = pygame.image.load('static/bomb.png')
        self.bomb_time = 0
        self.win_time = 0

        self.playing_area = [0, self.ui.screen_size[1] - 100]
        self.cell_width = 0
        self.cell_height = 0
        self.rows = rows
        self.cols = cols

        self.scale_cells(rows, cols)
        self.scale_images()

        font_size = int(self.cell_width * 0.9)
        self.font = pygame.font.Font('static/DigitalDisco.ttf', font_size)
        
        self.colors = {
            1: pygame.Color('blue'),
            2: pygame.Color('forestgreen'),
            3: pygame.Color('red'),
            4: pygame.Color('darkslateblue'),
            5: pygame.Color('chocolate4'),
            6: pygame.Color('darkorchid4'),
            7: pygame.Color('gold'),
            8: pygame.Color('black')

        }
    
    def scale_cells(self, rows, cols):
        """Scale cells to size of board."""
        original_width, original_height = self.cell_image.get_size()
        aspect_ratio = original_height / original_width
        new_height = self.playing_area[1] // rows
        new_width = int(new_height / aspect_ratio)

        self.cell_image = pygame.transform.scale(self.cell_image, (new_width, new_height))

        self.playing_area = [new_width * cols, new_height * rows]
        self.cell_width = new_width
        self.cell_height = new_height

    
    def scale_images(self):
        """Scale flag and bomb image to size of cell."""
        self.flag_image = pygame.transform.scale(self.flag_image, (self.cell_width // 1.2, self.cell_height // 1.2))
        self.bomb_image = pygame.transform.scale(self.bomb_image, (self.cell_width // 1.2, self.cell_height // 1.2))

    def draw_board(self):
        """Draw the board."""
        x_offset = (self.ui.screen_size[0] // 2) - (self.playing_area[0] // 2)
        y_offset = 100
        for row in range(self.game.rows):
            for col in range(self.game.cols):
                x = col * self.cell_width + x_offset
                y = row * self.cell_height + y_offset
                if self.game.revealed_cells[row][col]:
                    rect = pygame.Rect((x, y, self.cell_width, self.cell_height))
                    num = self.game.board[row][col]
                    if num > 0:
                        color = self.colors[num]
                        text = self.font.render(f'{num}', True, color)
                        text_rect = text.get_rect(center=rect.center)
                        self.ui.screen.blit(text, text_rect)
                    
                    elif num == 0:
                        if not self.game.game_over:
                            pygame.draw.rect(self.ui.screen, (192, 192, 192), rect)
                    
                    else:
                        rect = self.flag_image.get_rect()
                        rect.centerx= x + self.cell_width // 2
                        rect.centery = y + self.cell_height // 2
                        self.ui.screen.blit(self.bomb_image, rect)

                else:
                    self.ui.screen.blit(self.cell_image, (x, y))

                    if self.game.flags[row][col]:
                            rect = self.flag_image.get_rect()
                            rect.centerx= x + self.cell_width // 2
                            rect.centery = y + self.cell_height // 2
                            self.ui.screen.blit(self.flag_image, rect)
                            
                    
    
    def handle_click(self, event, left):
        """Handle left and right clicks."""
        cursor_x, cursor_y = event.pos
        board_x = (self.ui.screen_size[0] // 2) - (self.playing_area[0] // 2)
        board_y = 100
        col = (cursor_x - board_x) // self.cell_width
        row = (cursor_y - board_y) // self.cell_height

        if 0 <= col < self.cols and 0 <= row < self.rows:
            if left:
                self.game.reveal_cell(row, col)
                if self.game.board[row][col] == -1:
                    self.bomb_time = pygame.time.get_ticks()
                if self.game.remaining_tiles == 0:
                    self.win_time = pygame.time.get_ticks()
            else:
                self.game.flag_cell(row, col)

    def handle_screen_specific_events(self, events):
        """Handle events specific to gameplay screen."""
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    self.handle_click(event, left=True)
                else:
                    self.handle_click(event, left = False)
        
        if self.game.game_over:
            if pygame.time.get_ticks() - self.bomb_time > 1500:
                self.ui.show_gameover_screen()

    def update_screen_specific(self):
        # Update logic specific to the welcome screen
        if self.game.remaining_tiles == 0 and self.win_time - pygame.time.get_ticks > 1000:
            self.ui.show_game_won_screen()


    def draw_screen_specific(self):
        # Drawing logic specific to the welcome screen
        color = pygame.Color('red') if self.game.game_over else (192, 192, 192)
        self.ui.screen.fill(color)  
        
        self.draw_board()