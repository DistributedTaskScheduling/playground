from abc import ABC
from abc import abstractmethod


class IBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def help(self, x: int) -> str:
        pass
