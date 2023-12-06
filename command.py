from abc import ABC, abstractmethod
from enum import Enum


class Commands(Enum):
    PAUSE = "pause"
    SAVE = "save"
    LOAD = "load"


class ICommand(ABC):
    def __init__(self, subject, command):
        self.subject = subject
        self.command = command

    @abstractmethod
    def execute(self):
        pass


class GameCommand(ICommand):
    def __init__(self, subject, command):
        super().__init__(subject, command)

    def execute(self):
        if self.command == Commands.PAUSE:
            self.subject.toggle_pause()
        elif self.command == Commands.SAVE:
            self.subject.save()
        elif self.command == Commands.LOAD:
            self.subject.load()
        else:
            print(f"Unknown command type: {self.command}")
