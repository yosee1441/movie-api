from fastapi.security import HTTPBearer
from fastapi import HTTPException, status, Request
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if not (data.email == 'wJHc7@example.com' and data.password == 'admin123'):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authenticated")
        