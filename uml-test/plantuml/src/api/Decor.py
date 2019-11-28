from abc import ABC, abstractmethod

class Decor(ABC):
    @abstractmethod
    def oper(self):
        pass
