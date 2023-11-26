from fastapi import APIRouter

from crud_project.models.User import UserReturn, User
import crud_project.controllers.user_controller as userctrl

router = APIRouter(prefix="/user", tags=["User"])


@router.get("")
async def get_all_users():
    return await userctrl.get_all_users()
