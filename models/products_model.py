from schemas.products_schema import Product

def get_product(pk: str):
    product= Product.get(pk) 
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    } 