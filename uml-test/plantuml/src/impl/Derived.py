from api.IBase import IBase


class Derived(IBase):
    def help(self, x: int) -> str:
        print("Helping you to achieve your goals in life")
        return str(x)
