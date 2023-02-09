from abc import ABCMeta
from abc import abstractmethod


class BaseUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *args, **kwargs):
        ...
