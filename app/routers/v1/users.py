from fastapi import APIRouter

from app.dtos.user import UserRequest
from app.dtos.user import UserResponse
from app.use_cases.users import UserAddUseCase

router = APIRouter()


@router.get("/users/", tags=["users"])
async def get_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/users/", tags=["users"])
async def create_user(user: UserRequest) -> UserResponse:
    # case = UserAddUseCase()
    response = UserResponse(**user.dict())
    return response
