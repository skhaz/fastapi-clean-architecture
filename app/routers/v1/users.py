from fastapi import APIRouter
from google.cloud.firestore import Client as FirestoreClient

from app.dtos.user import UserRequest
from app.dtos.user import UserResponse
from app.repositories.firestore import FirestoreRepository
from app.use_cases.users import UserAddUseCase
from app.use_cases.users import UserListUseCase
from typing import Iterable

router = APIRouter()
firestore = FirestoreClient()
repo = FirestoreRepository(firestore.collection("users"))


@router.get("/users/", tags=["users"])
async def get_users() -> Iterable[UserResponse]:
    entities = UserListUseCase(repo).execute()

    return [UserResponse.from_orm(entity) for entity in entities]


@router.post("/users/", tags=["users"])
async def create_user(user: UserRequest) -> UserResponse:
    entity = UserAddUseCase(repo).execute(user)

    return UserResponse.from_orm(entity)
