from abc import ABC
from typing import Iterable
from typing import Optional

from app.entities import BaseEntity
from app.repositories import BaseRepository


class MemoryRepository(BaseRepository, ABC):
    def __init__(self) -> None:
        self.data: list[BaseEntity] = []

    def get(self, id: str) -> Optional[BaseEntity]:
        return next((e for e in self.data if e.id == id), None)

    def list(self) -> Iterable[BaseEntity]:
        return self.data

    def add(self, other: BaseEntity) -> BaseEntity:
        self.data.append(other)
        other.id = str(len(self.data))
        return other

    def remove(self, id: str) -> bool:
        self.data = list(filter(lambda e: e.id != id, self.data))
        return True

    def commit(self) -> None:
        ...
