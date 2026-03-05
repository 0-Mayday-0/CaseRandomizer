from abc import ABC, abstractmethod

class Case(ABC):
    def __init__(self, name) -> None:
        self.name: str = name

    @abstractmethod
    def __dict__(self) -> dict:
        pass

class Rank(ABC):
    def __init__(self) -> None:
        self.cases: list[Case]

    @abstractmethod
    def __dict__(self) -> dict:
        pass

    @abstractmethod
    def get_random_case(self) -> Case:
        pass