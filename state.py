import numpy as np
from abc import ABC, abstractmethod
from config import N_CELLS_X, N_CELLS_Y


class IState(ABC):
    @abstractmethod
    def get(self) -> any:
        pass

    @abstractmethod
    def update(self, new_state) -> None:
        pass


class GameState(IState):
    def __init__(self, initial_state):
        self.state = initial_state

    def get(self):
        return self.state

    def update(self, new_state):
        self.state = new_state
