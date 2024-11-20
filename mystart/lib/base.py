from abc import ABC, abstractmethod


class ModuleBase(ABC):
    @abstractmethod
    def run(self) -> None:
        ...
