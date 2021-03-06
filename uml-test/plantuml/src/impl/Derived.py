from api.IBase import IBase


class Derived(IBase):
    """A source of infinite wisdom."""

    def help(self, x: int) -> str:
        """Answers user questions."""
        print("Helping you to achieve your goals in life")
        return str(x)
