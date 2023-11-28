from fastapi.responses import JSONResponse
from crud_project.models.User import UserReturn, User

async def get_all_users(current_user:UserReturn):
    return JSONResponse({ "success": True, "user": current_user })