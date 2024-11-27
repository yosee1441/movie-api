from pydantic import BaseModel

class UserCreationDto(BaseModel):
    email: str
    password: str