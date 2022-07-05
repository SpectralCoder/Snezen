import motor.motor_asyncio
import os
from dotenv import load_dotenv
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client.main

def get_database() -> motor.motor_asyncio.AsyncIOMotorClient:
    return db.get_collection("User")