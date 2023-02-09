from abc import ABC
from typing import Iterable
from typing import List

from app.entities import BaseEntity
from app.repositories import BaseRepository


class MemoryRepository(BaseRepository, ABC):
    def __init__(self) -> None:
        self.data: List[BaseEntity] = []

    def get(self, id: int) -> BaseEntity:
        return self.data[0]

    def list(self) -> Iterable[BaseEntity]:
        return self.data

    def add(self, other: BaseEntity) -> BaseEntity:
        self.data.append(other)
        return other

    def remove(self, other: BaseEntity) -> bool:
        return True

    def commit(self) -> None:
        print("Commit!")
