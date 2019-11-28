from abc import ABC
from abc import abstractmethod


class IBase(ABC):
    """A basic interface that provides a help method."""

    def __init__(self):
        """Base constructor."""
        pass

    @abstractmethod
    def help(self, x: int) -> str:
        """Helps users."""
        pass
