from fastapi import FastAPI
from Auth import auth_routes
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

from datetime import datetime, timedelta
from gc import collect
from jose import JWTError, jwt


# to get a string like this run:
# openssl rand -hex 32

app = FastAPI()
app.include_router(auth_routes.router)





