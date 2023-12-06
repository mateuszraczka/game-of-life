import json
import numpy as np
from abc import abstractmethod, ABC


class IFileManager(ABC):
    @abstractmethod
    def save(self, state) -> None:
        pass

    @abstractmethod
    def load(self) -> any:
        pass


class GameFileManager(IFileManager):
    def __init__(self, file_path):
        self.file_path = file_path

    @staticmethod
    def _serialize_state(state):
        return json.dumps(state.tolist())

    @staticmethod
    def _deserialize_state(serialized_state):
        return np.array(json.loads(serialized_state))

    def save(self, state):
        serialized_state = self._serialize_state(state)
        with open(self.file_path, 'w') as file:
            file.write(serialized_state)

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                serialized_state = file.read()
            return self._deserialize_state(serialized_state)
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON in '{self.file_path}'.")
            return None
