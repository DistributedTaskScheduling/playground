import Message

class MessageImpl(Message.Message):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @classmethod
    def parse(cls, dct):
        assert 'x' in dct and 'y' in dct
        return MessageImpl(dct['x'], dct['y'])

    def serialize(self) -> dict:
        return { 'x' : self._x, 'y' : self._y }

    def sum(self) -> int:
        return self._x + self._y
