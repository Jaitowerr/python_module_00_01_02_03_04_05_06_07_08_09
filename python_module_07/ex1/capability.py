from abc import ABC, abstractmethod
import typing


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):

    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> typing.Any:
        pass

    @abstractmethod
    def revert(self) -> typing.Any:
        pass
