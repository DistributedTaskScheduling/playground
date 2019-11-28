from api.IBase import IBase

class Usage(IBase):
    """Performs complex calculations."""

    def help(self, x: int) -> str:
        return str(x * 2)
