from xmlrpc.client import DateTime
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

# class User(BaseModel):
#     name: str
#     father_name: str
#     home: str
#     village: str
#     thana: str
#     district: str
#     phone: int
#     product: str
#     price: int
#     paid: int
#     due: DateTime

def get_user_formatted(item):
    print(item)
    return jsonable_encoder({
    'username': item["username"],
    'email': item["email"],
    'fullname': item["full_name"],
    'password': item["password"],
    'disabled': item["disabled"]
    }) 