import numpy as np
from state import GameState
from filemanager import GameFileManager


class Game:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, n_cells_x, n_cells_y):
        if not hasattr(self, 'initialized'):
            self._n_cells_x = n_cells_x
            self._n_cells_y = n_cells_y
            self.state = GameState(np.random.choice([0, 1], size=(n_cells_x, n_cells_y), p=[0.8, 0.2]))
            self.paused = False
            self.running = True
            self.file_manager = GameFileManager("save.txt")
            self.initialized = True

    def toggle_pause(self):
        self.paused = not self.paused

    def _next_generation(self):
        current_state = self.state.get()
        new_state = np.copy(current_state)

        for y in range(self._n_cells_y):
            for x in range(self._n_cells_x):
                n_neighbors = current_state[(x - 1) % self._n_cells_x, (y - 1) % self._n_cells_y] + \
                              current_state[x % self._n_cells_x, (y - 1) % self._n_cells_y] + \
                              current_state[(x + 1) % self._n_cells_x, (y - 1) % self._n_cells_y] + \
                              current_state[(x - 1) % self._n_cells_x, y % self._n_cells_y] + \
                              current_state[(x + 1) % self._n_cells_x, y % self._n_cells_y] + \
                              current_state[(x - 1) % self._n_cells_x, (y + 1) % self._n_cells_y] + \
                              current_state[x % self._n_cells_x, (y + 1) % self._n_cells_y] + \
                              current_state[(x + 1) % self._n_cells_x, (y + 1) % self._n_cells_y]

                if current_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif current_state[x, y] == 0 and n_neighbors == 3:
                    new_state[x, y] = 1

        self.state.update(new_state)

    def save(self):
        if not self.paused:
            self.toggle_pause()
        current_state = self.state.get()
        self.file_manager.save(current_state)

    def load(self):
        if not self.paused:
            self.toggle_pause()
        loaded_state = self.file_manager.load()
        self.state.update(loaded_state)

    def run(self):
        if not self.paused:
            self._next_generation()

