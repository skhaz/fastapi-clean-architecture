from abc import ABC
from abc import abstractmethod
from typing import Iterable
from typing import Optional

from app.entities import BaseEntity


class ContextManagerRepository(ABC):
    @abstractmethod
    def commit(self):
        ...

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.commit()


class BaseReadOnlyRepository(ABC):
    @abstractmethod
    def get(self, id: str) -> Optional[BaseEntity]:
        ...

    @abstractmethod
    def list(self) -> Iterable[BaseEntity]:
        ...


class BaseWriteOnlyRepository(ContextManagerRepository):
    @abstractmethod
    def add(self, other: BaseEntity) -> BaseEntity:
        ...

    @abstractmethod
    def remove(self, id: str) -> bool:
        ...


class BaseRepository(BaseReadOnlyRepository, BaseWriteOnlyRepository, ABC):
    ...
