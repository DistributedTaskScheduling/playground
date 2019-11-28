from abc import ABC, abstractmethod

class Decor(ABC):
    """An abstract decorator class."""

    @abstractmethod
    def oper(self) -> None:
        """Performs an operation."""
        pass
