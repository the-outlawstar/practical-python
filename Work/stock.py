# stock.py

import typedproperty

class Stock:
    name = typedproperty.String('name')
    shares = typedproperty.Integer('shares')
    price = typedproperty.Float('price')

    def __init__(self,name:str,shares:int,price:float) -> None:
        self.name = name
        self.shares = shares
        self.price = price
    
    def __repr__(self) -> str:
        return f'Stock({self.name},{self.shares},{self.price})'

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self,quantity):
        self.shares -= quantity
        return self.shares
    
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self,value):
        if not isinstance(value,int):
            raise TypeError('Expected int')
        self._shares = value