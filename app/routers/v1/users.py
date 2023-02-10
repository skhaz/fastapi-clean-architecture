from fastapi import APIRouter

from app.dtos.user import UserRequest
from app.dtos.user import UserResponse
from app.repositories.memory import MemoryRepository
from app.use_cases.users import UserAddUseCase
from app.use_cases.users import UserListUseCase

router = APIRouter()
repo = MemoryRepository()


@router.get("/users/", tags=["users"])
async def get_users():
    entities = UserListUseCase(repo).execute()

    return [UserResponse.from_orm(entity) for entity in entities]


@router.post("/users/", tags=["users"])
async def create_user(user: UserRequest) -> UserResponse:
    entity = UserAddUseCase(repo).execute(user)

    return UserResponse.from_orm(entity)
