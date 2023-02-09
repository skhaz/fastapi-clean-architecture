from abc import ABC
from abc import abstractmethod
from typing import Iterable

from app.entities import BaseEntity


class ContextManagerRepository(ABC):
    @abstractmethod
    def commit(self):
        ...

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.commit()


class BaseReadOnlyRepository(ABC):
    @abstractmethod
    def get(self, id: int) -> BaseEntity:
        ...

    @abstractmethod
    def list(self) -> Iterable[BaseEntity]:
        ...


class BaseWriteOnlyRepository(ContextManagerRepository):
    @abstractmethod
    def add(self, other: BaseEntity) -> BaseEntity:
        ...

    @abstractmethod
    def remove(self, other: BaseEntity) -> bool:
        ...  # pragma: no cover


class BaseRepository(BaseReadOnlyRepository, BaseWriteOnlyRepository, ABC):
    ...
