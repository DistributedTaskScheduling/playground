from api.Base import Base

class Usage(Base):
    def help(self, x: int) -> str:
        return str(x * 2)
