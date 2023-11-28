from datetime import timedelta, datetime
from jose import jwt, JWTError
from typing import Annotated
from bson import ObjectId

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import HTTPException, status, Depends

from pydantic import BaseModel

from crud_project.config.index import config
from crud_project.models.User import User, UserReturn

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenData(BaseModel):
    id: str | None = None

def create_access_token(data:dict, expires:timedelta|None=None):
    to_encode = data.copy()
    if expires:
        expire = datetime.utcnow() + expires
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, config.jwt_secret, algorithm='HS256')
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.jwt_secret, algorithms=['HS256'])
        id: str = payload.get("id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception

    user = await User.find_one({"_id": ObjectId(token_data.id) }, projection_model=UserReturn)
    if user is None:
        raise credentials_exception
    user = user.model_dump()
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    # if current_user: // Add Disable / locked status here
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user