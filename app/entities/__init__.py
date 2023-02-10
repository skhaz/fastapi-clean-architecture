from abc import ABCMeta
from abc import abstractmethod
from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class BaseEntity(metaclass=ABCMeta):
    id: Optional[str]

    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict):
        ...

    @abstractmethod
    def dict(self):
        ...
