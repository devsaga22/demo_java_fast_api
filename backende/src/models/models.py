from pydantic import BaseModel
# class Product:

#    id: int
#    name: str
#    description: str
#    price: float
#    in_stock_quantity: int
# #    initialisation
#    def __init__(self, id: int, name: str, description: str, price: float, in_stock_quantity: int):
#        self.id = id
#        self.name = name
#        self.description = description
#        self.price = price
#        self.in_stock_quantity = in_stock_quantity
class Product(BaseModel):
#    pydantic validations and baseModel features its like lombok in java
   id: int
   name: str
   description: str
   price: float
   in_stock_quantity: int