import pygame
from config import WINDOW


class Button:
    def __init__(self, button_x, button_y, button_width, button_height, text, font_color, background_color):
        self.button_x = button_x
        self.button_y = button_y
        self.button_width = button_width
        self.button_height = button_height
        self.text = text
        self.font_color = font_color
        self.background_color = background_color
        self.command = None

    def draw(self):
        pygame.draw.rect(WINDOW, self.background_color, (self.button_x, self.button_y, self.button_width, self.button_height))
        font = pygame.font.Font(None, 28)
        text = font.render(self.text, True, self.font_color)
        text_rect = text.get_rect(center=(self.button_x + self.button_width // 2, self.button_y + self.button_height // 2))
        WINDOW.blit(text, text_rect)

    def set_command(self, command):
        self.command = command

    def handle_click(self):
        if self.command:
            self.command.execute()
