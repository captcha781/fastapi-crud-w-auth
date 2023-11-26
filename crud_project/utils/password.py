from bcrypt import hashpw, gensalt, checkpw

async def hashed_password(password:str) -> str:
    return hashpw(password.encode(), gensalt(10)).decode()

async def compare_password(password:str, hashed_password:str) -> bool:
    return await checkpw(password, hashed_password)