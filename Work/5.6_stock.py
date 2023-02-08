class Stock:
    def __init__(self,name:str,shares:int,price:float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self,quantity):
        self.shares -= quantity
        return quantity * self.price

    def __repr__(self) -> str:
        return f'Stock({self.name},{self.shares},{self.price})'