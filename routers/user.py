from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from dtos import UserCreationDto
from utils.jwt_manager import create_token
from fastapi import APIRouter

user_router = APIRouter()

@user_router.post('/login', tags=['Auth'], response_model=UserCreationDto, status_code=status.HTTP_200_OK)
def login(dto: UserCreationDto) -> UserCreationDto:
    if dto.email == 'wJHc7@example.com' and dto.password == 'admin123':
        token:str = create_token(dto.model_dump())

        return JSONResponse(content={
            "token": token,
            "user": dto.model_dump()
        }, status_code=status.HTTP_200_OK)
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")