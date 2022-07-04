from redis_om import HashModel, get_redis_connection

redis = get_redis_connection(
    host = "redis-16665.c264.ap-south-1-1.ec2.cloud.redislabs.com",
    port =16665,
    password="AYF2x4U4agLT5dE7PoFFU0aL2ldoxa6Q",
    decode_responses= True
)

class Product(HashModel):
    name: str
    price: int
    quantity: int

    class Meta:
        database = redis  