from typing import List

from fastapi import APIRouter
from google.cloud.firestore import Client as FirestoreClient

from app.dtos.user import UserRequest
from app.dtos.user import UserResponse
from app.repositories.firestore import FirestoreRepository
from app.use_cases.users import UserAddUseCase
from app.use_cases.users import UserListUseCase

router = APIRouter()
firestore = FirestoreClient()
repo = FirestoreRepository(firestore.collection("users"))


@router.get("/users/")
async def get_users() -> List[UserResponse]:
    return [UserResponse.from_orm(e) for e in UserListUseCase(repo).execute()]


@router.post("/users/")
async def create_user(user: UserRequest) -> UserResponse:
    entity = UserAddUseCase(repo).execute(user)

    return UserResponse.from_orm(entity)
