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
