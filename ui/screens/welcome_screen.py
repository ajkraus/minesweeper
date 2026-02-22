"""Welcome screen class."""
import pygame
from ui.screens.base_screen import BaseScreen

class WelcomeScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui, font_size=48)
        self.title = self.font.render("MINESWEEPER", True, pygame.Color("red"))
        self.title_rect = self.title.get_rect(center=(ui.screen_size[0] // 2, 150))

        self.start_time = pygame.time.get_ticks()
        self.display_time = 1000
    
    def handle_screen_specific_events(self, events):
        # Handle events specific to the welcome screen
        pass

    def update_screen_specific(self):
        # Update logic specific to the welcome screen
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.display_time:
            self.ui.show_new_game_screen()

    def draw_screen_specific(self):
        # Drawing logic specific to the welcome screen
        self.ui.screen.fill((192, 192, 192))  # Fill the screen with a black background
        self.ui.screen.blit(self.title, self.title_rect)