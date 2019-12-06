from typing import Dict
from Message import Message
from pkg.MessageImpl import MessageImpl
import importlib
import inspect

def prepare(msg: Message) -> str:
    full_msg: Dict[str, object] = {}

    module = inspect.getmodule(msg)
    assert(module)

    full_msg['module'] = module.__name__
    full_msg['type'] = msg.__class__.__name__
    full_msg['data'] = msg.serialize()

    return str(full_msg)

def receive(s: str) -> Message:
    dct = eval(s)
    module = importlib.import_module(dct['module'])
    assert module
    cls = getattr(module, dct['type'])
    assert cls

    assert issubclass(cls, Message)
    return cls.parse(dct['data'])

msg = MessageImpl(1, 2)
s = prepare(msg)
rec = receive(s)

print(rec.sum())

