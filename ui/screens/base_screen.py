"""Base screen class."""
import pygame

class BaseScreen:
    def __init__(self, ui, font_size=24):
        self.ui = ui
        self.font = pygame.font.Font('static/DigitalDisco.ttf', font_size)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.ui.running = False

        # Handle events specific to each screen
        self.handle_screen_specific_events(events)

    def update(self):
        # Update logic common to all screens
        self.update_common()

        # Update logic specific to each screen
        self.update_screen_specific()

    def draw(self):
        # Drawing logic common to all screens
        self.draw_common()

        # Drawing logic specific to each screen
        self.draw_screen_specific()

    def handle_screen_specific_events(self, events):
        # Override this method in specific screen classes to handle screen-specific events
        pass

    def update_common(self):
        # Common update logic for all screens
        pass

    def update_screen_specific(self):
        # Override this method in specific screen classes to handle screen-specific updates
        pass

    def draw_common(self):
        # Common drawing logic for all screens
        pass

    def draw_screen_specific(self):
        # Override this method in specific screen classes to handle screen-specific drawing
        pass
