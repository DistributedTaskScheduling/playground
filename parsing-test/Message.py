from abc import ABC, abstractmethod

class Message:
    @classmethod
    @abstractmethod
    def parse(cls, dct):
        pass

    @abstractmethod
    def sum(self) -> int:
        pass

    @abstractmethod
    def serialize(self) -> dict:
        pass
