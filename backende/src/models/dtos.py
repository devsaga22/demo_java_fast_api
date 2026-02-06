from pydantic import BaseModel


class ProductDTO(BaseModel):
   
    name: str
    price: float
    description: str
    in_stock_quantity: int

class ProductResponseDTO(ProductDTO):
    id: int
