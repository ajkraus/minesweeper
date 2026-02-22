"""Main UI module."""
# minesweeper/ui/minesweeper_ui.py
import pygame
from ui.screens.welcome_screen import WelcomeScreen
from ui.screens.new_game import NewGame
from ui.screens.difficulty import DifficultyScreen
from ui.screens.game_screen import Gameplay
from ui.screens.game_over import GameOver
from ui.screens.game_won import GameWon

class MinesweeperUI:
    def __init__(self):
        pygame.init()
        self.screen_size = (1200, 750)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Minesweeper")

        self.clock = pygame.time.Clock()
        self.running = True
        self.current_screen = WelcomeScreen(self)

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        self.current_screen.handle_events(events)

    def update(self):
        self.current_screen.update()

    def draw(self):
        self.current_screen.draw()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(30)  # Adjust the frame rate as needed
    
    def show_new_game_screen(self):
        self.current_screen = NewGame(self)
    
    def show_difficulty_screen(self):
        self.current_screen = DifficultyScreen(self)
    
    def show_gameplay_screen(self, rows, cols, mines):
        self.current_screen = Gameplay(self, rows, cols, mines)
    
    def show_gameover_screen(self):
        self.current_screen = GameOver(self)
    
    def show_game_won_screen(self):
        self.current_screen = GameWon(self)



        