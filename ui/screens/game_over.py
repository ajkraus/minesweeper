"""Game over screen class."""
import pygame
from ui.screens.base_screen import BaseScreen

class GameOver(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)
        self.title = self.font.render("Game Over", True, pygame.Color("red"))
        self.title_rect = self.title.get_rect(center=(ui.screen_size[0] // 2, 100))
        self.buttons = [
            {'text': 'New Game', 'rect': pygame.Rect(400, 300, 300, 50)},
            {'text': 'Quit', 'rect': pygame.Rect(200, 450, 300, 50)}
        ]
        self.selected_button = None


    def handle_click(self, pos):
        for button in self.buttons:
            if button['rect'].collidepoint(pos):
                return button['text']
        return None

    def handle_screen_specific_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_button = self.handle_click(event.pos)
                if selected_button == 'Quit':
                    self.ui.running = False

                elif selected_button == 'New Game':
                    self.ui.show_difficulty_screen()

    def update_screen_specific(self):
        # Update logic specific to the welcome screen
        pass

    def draw_screen_specific(self):
        # Drawing logic specific to the welcome screen
        self.ui.screen.fill((192, 192, 192))  # Fill the screen with a black background
        self.ui.screen.blit(self.title, self.title_rect)

        for button in self.buttons:
            button_rect = button['rect']
            button_rect.centerx = self.ui.screen_size[0] // 2
            pygame.draw.rect(self.ui.screen, (100, 100, 100), button_rect)

            button_text = self.font.render(button['text'], True, (255, 255, 255))
            text_rect = button_text.get_rect(center=button_rect.center)
            self.ui.screen.blit(button_text, text_rect)