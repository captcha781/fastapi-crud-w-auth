from fastapi import APIRouter

from crud_project.models.User import User, UserRegister
import crud_project.controllers.auth_controller as auth_ctrl

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post('/signup')
async def add_user(user_data:UserRegister):
    return await auth_ctrl.signup_user(user_data)