from xmlrpc.client import DateTime
from pydantic import BaseModel

class User(BaseModel):
    name: str
    father_name: str
    home: str
    village: str
    thana: str
    district: str
    phone: int
    product: str
    price: int
    paid: int
    due: DateTime
