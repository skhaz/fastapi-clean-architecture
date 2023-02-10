from typing import Optional
from typing import TypedDict

from pydantic.dataclasses import dataclass

from app.entities import BaseEntity
from app.repositories.memory import MemoryRepository


class Dummy(TypedDict):
    id: Optional[int]


@dataclass
class DummyEntity(BaseEntity):
    id: Optional[int]

    @classmethod
    def from_dict(cls, other: dict):
        return cls(
            id=other.get("id"),
        )

    @classmethod
    def dict(self) -> Dummy:
        return {
            "id": self.id,
        }


def test_memory_repository_add_and_list():
    repo = MemoryRepository()
    entity = DummyEntity(id=1)
    repo.add(entity)
    entities = repo.list()

    assert entities == [entity]


def test_memory_repository_remove():
    repo = MemoryRepository()
    entity = DummyEntity(id=1)
    repo.add(entity)
    result = repo.remove(entity.id)

    assert result


def test_memory_repository_get():
    repo = MemoryRepository()
    entity = DummyEntity(id=1)
    repo.add(entity)
    other = repo.get(entity.id)

    assert other == entity
