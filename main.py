from fastapi import FastAPI 
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movies import movie_router
from routers.user import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)
 