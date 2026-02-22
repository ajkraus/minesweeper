"""New game screen class."""
import pygame
from ui.screens.base_screen import BaseScreen

class NewGame(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui, font_size=48)
        self.title = self.font.render("MINESWEEPER", True, pygame.Color("red"))
        self.title_rect = self.title.get_rect(center=(ui.screen_size[0] // 2, 150))
        self.button_font = pygame.font.Font('static/DigitalDisco.ttf', 24)
        self.button_rect = pygame.Rect(0, 300, 300, 50) # (x, y, width, height)
        self.button_rect.centerx = self.ui.screen_size[0] // 2

    def handle_screen_specific_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = pygame.mouse.get_pos()
                if self.button_rect.collidepoint(cursor_pos):
                    self.ui.show_difficulty_screen()

    def update_screen_specific(self):
        # Update logic specific to the welcome screen
        pass

    def draw_screen_specific(self):
        # Drawing logic specific to the new game screen
        self.ui.screen.fill((192, 192, 192))  # Fill the screen with a black background

        # Draw the button
        pygame.draw.rect(self.ui.screen, (100, 100, 100), self.button_rect)
        
        # Draw text on the button
        button_text = self.button_font.render("Start New Game", True, (255, 255, 255))
        text_rect = button_text.get_rect(center=self.button_rect.center)
        self.ui.screen.blit(button_text, text_rect)

        self.ui.screen.blit(self.title, self.title_rect)