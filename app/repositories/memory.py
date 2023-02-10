from abc import ABC
from typing import Dict
from typing import Iterable

from app.entities import BaseEntity
from app.repositories import BaseRepository


class MemoryRepository(BaseRepository, ABC):
    def __init__(self) -> None:
        self.data: Dict[int, BaseEntity] = {}
        self.counter: int = 0

    def get(self, id: int) -> BaseEntity:
        return self.data[id]

    def list(self) -> Iterable[BaseEntity]:
        return list(self.data.values())

    def add(self, other: BaseEntity) -> BaseEntity:
        self.counter += 1
        self.data[self.counter] = other
        return other

    def remove(self, id: int) -> bool:
        del self.data[id]
        return True

    def commit(self) -> None:
        ...
