from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class BaseEntity(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict):
        ...

    @abstractmethod
    def dict(self):
        ...
