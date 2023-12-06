import pygame
from abc import ABC, abstractmethod


class IEventHandler(ABC):
    @abstractmethod
    def handle_events(self) -> None:
        pass


class IMouseEvent(ABC):
    @abstractmethod
    def handle_mouse_button_down(self, event) -> None:
        pass

    @abstractmethod
    def handle_mouse_button_up(self, event) -> None:
        pass

    @abstractmethod
    def handle_mouse_move(self, event) -> None:
        pass


class GameEventHandler(IEventHandler, IMouseEvent):
    def __init__(self, buttons, game):
        self.buttons = buttons
        self.game = game

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_button_down(event)

    def handle_mouse_button_down(self, event):
        for button in self.buttons:
            if self._is_click_inside_button(event.pos, button):
                button.handle_click()

    def handle_mouse_button_up(self, event):
        pass

    def handle_mouse_move(self, event):
        pass

    @staticmethod
    def _is_click_inside_button(click_pos, button):
        x, y = click_pos
        return (
            button.button_x <= x <= button.button_x + button.button_width and
            button.button_y <= y <= button.button_y + button.button_height
        )
