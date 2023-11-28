from fastapi import APIRouter, Depends

from crud_project.models.User import UserReturn, User
import crud_project.controllers.user_controller as userctrl
from crud_project.security.jwt import get_current_active_user

from typing import Annotated

router = APIRouter(prefix="/user", tags=["User"])


@router.get("")
async def get_all_users(current_user: Annotated[User, Depends(get_current_active_user)]) -> UserReturn:
    return await userctrl.get_all_users(current_user)
