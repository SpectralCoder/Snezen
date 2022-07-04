import imp
from fastapi import FastAPI
from schemas.products_schema import Product
from models.products_model import get_product

router= FastAPI(openapi_prefix="/redis")

@router.get("/products")
def all_products():
    return [get_product(pk) for pk in Product.all_pks()]

@router.get("/prducts/{pk}")
def single_product(pk: str):
    return Product.get(pk)

@router.post('/products')
def create_product(product: Product):
    return product.save()

@router.delete("/prducts/{pk}")
def delete_product(pk: str):
    return Product.delete(pk)