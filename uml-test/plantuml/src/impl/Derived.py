from api.Base import Base


class Derived(Base):
    def help(self, x: int) -> str:
        print("Helping you to achieve your goals in life")
        return str(x)
