
from fastapi import Body, FastAPI, HTTPException, Path

from src.models.models import Product
from src.models.dtos import ProductDTO, ProductResponseDTO

app = FastAPI()

prod_list=[
            Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop", in_stock_quantity=14),
            Product(id=2, name="Smartphone", price=499.99, description="A latest model smartphone", in_stock_quantity=30),
            Product(id=3, name="Headphones", price=199.99, description="Noise-cancelling headphones", in_stock_quantity=25),
            Product(id=4, name="Smartwatch", price=299.99, description="A smartwatch with various features", in_stock_quantity=20),
            Product(id=5, name="Tablet", price=399.99, description="A lightweight tablet for work and play", in_stock_quantity=18),
            Product(id=6, name="Camera", price=599.99, description="A high-resolution camera for photography", in_stock_quantity=10),
            Product(id=7, name="Gaming Console", price=499.99, description="A popular gaming console", in_stock_quantity=12),
            Product(id=8, name="Bluetooth Speaker", price=149.99, description="A portable Bluetooth speaker", in_stock_quantity=22),
            Product(id=9, name="External Hard Drive", price=89.99, description="A 1TB external hard drive", in_stock_quantity=15),
            Product(id=10, name="Wireless Mouse", price=29.99, description="A wireless mouse with ergonomic design", in_stock_quantity=40)
            ]

@app.get("/")
def greet():
    return {"message": "Hello from FastAPI!"}

@app.get("/all_products")
def get_all_products():
    return prod_list
@app.get("/product/{prod_id}")
def get_product_by_id(
    # 'alias' tells FastAPI to look for {prod_id} in the URL , shows up in swagger docs
    # and map it to our semantic variable 'internal_id'
    id: int = Path(..., alias="prod_id",title="The ID of the product to fetch")
    ):
    for product in prod_list:
        if product.id == id:
            return product
    return {"message": "Product not found"}

@app.post("/add_product",response_model=ProductResponseDTO,status_code=201)
def add_product(new_product: ProductDTO)->ProductResponseDTO:
    new_id= max([p.id for p in prod_list])+1 if prod_list else 1
    # ObjectMapper like functionality to convert ProductDTO to Product by unpacking the DTO fields and adding the new_id
    new_product=Product(id=new_id,**new_product.model_dump())   
    prod_list.append(new_product)
    return ProductResponseDTO(**new_product.model_dump())

@app.put("/update_product/{prod_id}",response_model=ProductResponseDTO)
def update_product(
    id: int = Path(..., alias="prod_id", title="The ID of the product to update"),
    updated_product: ProductDTO = Body(...)) -> ProductResponseDTO:
    # Body(embed=True) nput with embed=True: The client must send {"updated_product": {"name": "Pizza", ...}}.
    for index, product in enumerate(prod_list):
        if product.id == id:
            updated_prod = Product(id=id, **updated_product.model_dump())
            prod_list[index] = updated_prod
            return ProductResponseDTO(**updated_prod.model_dump())
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/delete_product/{prod_id}", status_code=204)
def delete_product(id: int = Path(..., alias="prod_id", title="The ID of the product to delete")):
    for index, product in enumerate(prod_list):
        if product.id == id:
            del prod_list[index]
            return
    raise HTTPException(status_code=404, detail="Product not found")