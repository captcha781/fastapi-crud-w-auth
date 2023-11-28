from decouple import config
from pydantic import BaseModel

class ConfigSetting(BaseModel):
    mongo_uri:str = config('MONGO_URI')
    port:int = config('PORT')
    jwt_secret:str = config('JWT_SECRET')

config = ConfigSetting()