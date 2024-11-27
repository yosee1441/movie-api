from fastapi import HTTPException, status, Path, Query, Depends
from fastapi.responses import JSONResponse
from dtos import MovieCreateDto, MovieUpdateDto
from typing import List
from utils.jwt_manager import create_token
from config.database import Session
from models.movie import Movie 
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from fastapi import APIRouter
from services.movie import MovieService

movie_router = APIRouter()
 
@movie_router.get("/movies", tags=['Movies'], response_model=List[MovieUpdateDto], status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer)])
def find_all() -> List[MovieUpdateDto]:
    db = Session()
    movies = MovieService(db).find_all()

    return JSONResponse(content=jsonable_encoder(movies), status_code=status.HTTP_200_OK)

@movie_router.get("/movies/{id}", tags=['Movies'], response_model=MovieUpdateDto, status_code=status.HTTP_200_OK)
def find_one(id: int = Path(ge=1, le=2000)) -> MovieUpdateDto:
    db = Session()
    movie = MovieService(db).find_one(id)

    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    
    return JSONResponse(content=jsonable_encoder(movie), status_code=status.HTTP_200_OK)

@movie_router.get("/movies/", tags=['Movies'], response_model=List[MovieUpdateDto], status_code=status.HTTP_200_OK)
def find_by_category(category: str = Query(min_length=3, max_length=10)) -> List[MovieUpdateDto]:
    db = Session()
    movies = MovieService(db).find_by_category(category)

    if not movies:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    
    return JSONResponse(content=jsonable_encoder(movies), status_code=status.HTTP_200_OK)

@movie_router.post("/movies", tags=['Movies'], response_model=dict, status_code=status.HTTP_201_CREATED)
def create(dto: MovieCreateDto) -> dict:
    db = Session()
    new_movie = MovieService(db).create(dto)

    return JSONResponse(content=jsonable_encoder(new_movie), status_code=status.HTTP_201_CREATED)

@movie_router.put("/movies/{id}", tags=['Movies'], response_model=dict, status_code=status.HTTP_200_OK)
def update(id: int, dto: MovieUpdateDto) -> dict:
    db = Session()
    movie = MovieService(db).find_one(id)

    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    
    new_movie = MovieService(db).update(id, dto)
    
    return JSONResponse(content=jsonable_encoder(new_movie), status_code=status.HTTP_200_OK)

@movie_router.delete("/movies/{id}", tags=['Movies'], response_model=List[MovieUpdateDto], status_code=status.HTTP_200_OK)
def delete(id: int) -> List[MovieUpdateDto]:
    db = Session()
    movie = MovieService(db).find_one(id)

    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    
    MovieService(db).delete(id)
    
    return JSONResponse(status_code=status.HTTP_200_OK)
