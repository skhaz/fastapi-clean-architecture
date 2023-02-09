from pydantic import BaseModel

from app.entities.user import UserEntity
from app.repositories import BaseRepository
from app.use_cases import BaseUseCase
from app.entities import BaseEntity


def transform(origin: BaseModel) -> BaseEntity:
    return UserEntity.from_dict(origin.dict()).dict()


class UserAddUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, other: BaseModel) -> BaseEntity:
        with self.repo as repo:
            return repo.add(transform(other))
