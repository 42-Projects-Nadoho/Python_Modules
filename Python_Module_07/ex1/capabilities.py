from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str | None = None) -> str:
        raise NotImplementedError


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed = False

    @abstractmethod
    def transform(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def revert(self) -> str:
        raise NotImplementedError
