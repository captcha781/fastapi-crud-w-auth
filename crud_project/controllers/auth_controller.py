from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse

from crud_project.models.User import User, UserRegister, UserSignin
from crud_project.utils.password import hashed_password, compare_password
from crud_project.security.jwt import create_access_token

async def signup_user(user_data:UserRegister):
    is_email_found = await User.find_by_email(user_data.email)
    if is_email_found is not None:
        raise HTTPException(403, { "success": False, "message": "User already exists with this email" })
    password_hash = await hashed_password(user_data.password)
    user = User(email=user_data.email, password=password_hash, first_name=user_data.first_name, last_name=user_data.last_name)
    await user.save()
    return JSONResponse({ "success": True, "message": 'User registered successfully' })

async def signin_user(user_data:UserSignin):
    user = await User.find_by_email(user_data.email)
    if user is None:
        raise HTTPException(403, { "success": False, "message": "No user exists with this email" })
    if not compare_password(user_data.password, user.password):
        raise HTTPException(403, { "success": False, "message": "Incorrect Password" })
    user.password = ""

    token = create_access_token(data={ "id": user.model_dump().get('id') })
    return JSONResponse({ "success": True, "user": user.model_dump(), "token": token, "type": "bearer" })
    