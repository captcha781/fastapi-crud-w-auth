from fastapi.responses import JSONResponse
from crud_project.models.User import UserReturn, User

async def get_all_users():
    users_data = await User.find({}).project(UserReturn).to_list()
    if len(users_data) == 0:
        return JSONResponse(content={ "success": False, "message": "No users found" }, status_code=401)
    
    users_data = [user.model_dump() for user in users_data]    
    return JSONResponse(content={ "success": True, "users": users_data }, status_code=201)