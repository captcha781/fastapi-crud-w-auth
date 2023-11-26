import uvicorn

from crud_project.config.index import config

from crud_project.app import app
from crud_project.routes.user_routes import router as UserRouter
from crud_project.routes.auth_routes import router as AuthRouter

app.include_router(AuthRouter)
app.include_router(UserRouter)


def start_server():
    uvicorn.run("crud_project.server:app", host='0.0.0.0', port=int(config.port),reload=True, workers=4)

# if __name__ == "__main__":
    # uvicorn.run("crud_project.server:app", host='0.0.0.0', port=int(config.port),reload=True, workers=4)