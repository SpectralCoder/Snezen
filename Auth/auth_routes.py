from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from Auth.auth_help import get_user, get_password_hash, create_user, timedelta, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, authenticate_user, OAuth2PasswordRequestForm, get_current_active_user, REFRESH_TOKEN_EXPIRE_MINUTES, create_refresh_token
from Auth.auth_models import Token, User

router = APIRouter( prefix="")

@router.post("/signup", response_model=Token, status_code=status.HTTP_201_CREATED)
async def signup(form_data: User):
    user = await get_user(form_data.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        form_data.password = get_password_hash(form_data.password)
        created_user = await create_user(form_data)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": created_user["username"]}, expires_delta=access_token_expires
        )
        refresh_token_expires=timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
        refresh_token = create_refresh_token(
            data={"sub": user["username"]}, expires_delta=refresh_token_expires
        )
        return {"access_token": access_token, "refresh_token":refresh_token, "token_type": "bearer"}


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    refresh_token_expires=timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = create_refresh_token(
        data={"sub": user["username"]}, expires_delta=refresh_token_expires
    )
    return {"access_token": access_token, "refresh_token":refresh_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user["username"]}]
