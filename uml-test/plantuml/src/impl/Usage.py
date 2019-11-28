from api.IBase import IBase

class Usage(IBase):
    def help(self, x: int) -> str:
        return str(x * 2)
