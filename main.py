# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from routes.redis import router

# router.add_middleware(
#     CORSMiddleware,
#     allow_origins=['http://localhost:3000'],
#     allow_methods=['*'],
#     allow_headers=['*']
# )

# app = FastAPI()

# app.mount("/redis", router)

# @app.get("/")
# async def root():
#     return {"message": "alive"}

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}