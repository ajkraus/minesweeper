"""Difficult screen class."""
import pygame
from ui.screens.base_screen import BaseScreen

class DifficultyScreen(BaseScreen):
    def __init__(self, ui):
        super().__init__(ui)
        
        self.difficulties = [
            {"name": "Easy", "rows": 12, "cols": 15, "mines": 10},
            {"name": "Medium", "rows": 15, "cols": 20, "mines": 40},
            {"name": "Hard", "rows": 20, "cols": 25, "mines": 100},
        ]

        for i, difficulty in enumerate(self.difficulties):
            button_rect = pygame.Rect((250, 50 + 125*i, 300, 50))
            difficulty['button_rect'] = button_rect

        # Input fields for custom board size and number of mines
        self.custom_rows = 8
        self.custom_cols = 8
        self.custom_mines = 10

        # Button rect for starting the game
        self.start_button_rect = pygame.Rect(250, 550, 300, 50)
        self.start_button_rect.centerx = self.ui.screen_size[0] // 2
        self.selected_difficulty = None


    def handle_screen_specific_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Check if a difficulty button is clicked
                for difficulty in self.difficulties:
                    if difficulty["button_rect"].collidepoint(mouse_pos):
                        self.selected_difficulty = difficulty

                # Check if the start button is clicked
                if self.start_button_rect.collidepoint(mouse_pos):
                    # If a difficulty is selected, transition to the game screen
                    if self.selected_difficulty:
                        self.ui.show_gameplay_screen(
                            rows=self.selected_difficulty["rows"],
                            cols=self.selected_difficulty["cols"],
                            mines=self.selected_difficulty["mines"],
                        )
                    else:
                        # If no difficulty is selected, use custom values
                        self.ui.show_gameplay_screen(
                            rows=self.custom_rows,
                            cols=self.custom_cols,
                            mines=self.custom_mines,
                        )
                elif event.type == pygame.KEYDOWN:
                    if self.selected_input is not None:
                        # Handle numeric input for custom game parameters
                        if event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                            digit = int(pygame.key.name(event.key))
                            if self.selected_input == 0:
                                self.custom_rows = self.custom_rows * 10 + digit
                            elif self.selected_input == 1:
                                self.custom_cols = self.custom_cols * 10 + digit
                            elif self.selected_input == 2:
                                self.custom_mines = self.custom_mines * 10 + digit
                        elif event.key == pygame.K_BACKSPACE:
                            # Handle backspace to delete the last digit
                            if self.selected_input == 0:
                                self.custom_rows //= 10
                            elif self.selected_input == 1:
                                self.custom_cols //= 10
                            elif self.selected_input == 2:
                                self.custom_mines //= 10

    def update_screen_specific(self):
        # Update logic specific to the welcome screen
        pass

    def draw_screen_specific(self):
        # Drawing logic specific to the difficulty screen
        self.ui.screen.fill((192, 192, 192))  # Fill the screen with a black background

        # Draw difficulty buttons
        for difficulty in self.difficulties:
            button_rect = difficulty['button_rect']
            button_rect.centerx = self.ui.screen_size[0] // 2
            button_color = (100, 100, 100) if difficulty is not self.selected_difficulty else pygame.Color('red')
            pygame.draw.rect(self.ui.screen, button_color, button_rect)

            # Draw text on the button
            button_text = self.font.render(difficulty["name"], True, (255, 255, 255))
            text_rect = button_text.get_rect(center=button_rect.center)
            self.ui.screen.blit(button_text, text_rect)

            # Draw description boxes
            y_val = button_rect.y + 50
            description_rect = pygame.Rect((250, y_val, 300, 50))
            description_rect.centerx = self.ui.screen_size[0] // 2
            pygame.draw.rect(self.ui.screen, (150, 150, 150), description_rect)
            mines = difficulty['mines']
            rows = difficulty['rows']
            cols = difficulty['cols']
            description_text = self.font.render(f'{rows} rows, {cols} cols, {mines} mines',
                                                True, (255, 255, 255))
            desc_text_rect = description_text.get_rect(center=description_rect.center)
            self.ui.screen.blit(description_text, desc_text_rect)

        # # Draw custom input fields
        # pygame.draw.rect(self.ui.screen, (100, 100, 100), (225, 475, 100, 30))  # Custom rows
        # pygame.draw.rect(self.ui.screen, (100, 100, 100), (350, 475, 100, 30))  # Custom cols
        # pygame.draw.rect(self.ui.screen, (100, 100, 100), (475, 475, 100, 30))  # Custom mines

        # # Draw labels for custom input fields
        # rows_label = self.font.render("Rows:", True, (255, 255, 255))
        # cols_label = self.font.render("Cols:", True, (255, 255, 255))
        # mines_label = self.font.render("Mines:", True, (255, 255, 255))

        # self.ui.screen.blit(rows_label, (225, 270))
        # self.ui.screen.blit(cols_label, (350, 270))
        # self.ui.screen.blit(mines_label, (475, 270))

        # # Draw text input for custom values
        # custom_rows_text = self.font.render(str(self.custom_rows), True, (255, 255, 255))
        # custom_cols_text = self.font.render(str(self.custom_cols), True, (255, 255, 255))
        # custom_mines_text = self.font.render(str(self.custom_mines), True, (255, 255, 255))

        # self.ui.screen.blit(custom_rows_text, (250, 305))
        # self.ui.screen.blit(custom_cols_text, (400, 305))
        # self.ui.screen.blit(custom_mines_text, (550, 305))

        # Draw the start button
        pygame.draw.rect(self.ui.screen, (100, 100, 100), self.start_button_rect)
        start_button_text = self.font.render("Start Game", True, (255, 255, 255))
        start_text_rect = start_button_text.get_rect(center=self.start_button_rect.center)
        self.ui.screen.blit(start_button_text, start_text_rect)