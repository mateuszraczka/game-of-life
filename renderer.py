from config import WINDOW, CELL_COLOR, BACKGROUND_FILL_COLOR, GRID_COLOR
import pygame
from abc import abstractmethod, ABC


class IRenderer(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class GameRenderer(IRenderer):
    def __init__(self, game, width, height, cell_width, cell_height, n_cells_x, n_cells_y, buttons):
        self._width = width
        self._height = height
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._n_cells_x = n_cells_x
        self._n_cells_y = n_cells_y
        self.buttons = buttons
        self._game = game

    def _draw_grid(self):
        for y in range(0, self._height, self._cell_height):
            for x in range(0, self._width, self._cell_width):
                cell = pygame.Rect(x, y, self._cell_width, self._cell_height)
                pygame.draw.rect(WINDOW, GRID_COLOR, cell, 1)

    def _draw_cells(self):
        state = self._game.state.get()
        for y in range(self._n_cells_y):
            for x in range(self._n_cells_x):
                cell = pygame.Rect(x * self._cell_width, y * self._cell_height, self._cell_width, self._cell_height)
                if state[x, y] == 1:
                    pygame.draw.rect(WINDOW, CELL_COLOR, cell)

    def _draw_buttons(self):
        for button in self.buttons:
            button.draw()

    def render(self):
        WINDOW.fill(BACKGROUND_FILL_COLOR)
        self._draw_grid()
        self._draw_cells()
        self._draw_buttons()
        pygame.display.flip()
