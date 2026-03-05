from abc import ABC, abstractmethod
from random import choice
import strings as strs

class Case(ABC):
    def __init__(self, name) -> None:
        self.name: str = name

    @abstractmethod
    def __dict__(self) -> dict:
        pass

class Rank(ABC):
    def __init__(self, name: str, cases: list[Case]) -> None:
        self.name: str = name
        self.cases: list[Case] = cases

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __dict__(self) -> dict:
        pass

    @abstractmethod
    def get_random_case(self) -> Case:
        pass


class BaseCase(Case):
    def __init__(self, name) -> None:
        super().__init__(name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'BaseCase({self.name})'

    def __dict__(self) -> dict:
        return {strs.Ranks.Internal.NAME_KEY: self.name}


class BaseRank(Rank):
    def __init__(self, name, cases) -> None:
        super().__init__(name, cases)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'BaseRank({self.name=}, {self.cases=})'

    def __dict__(self) -> dict:
        return {strs.Ranks.Internal.CASES_KEY : [str(case) for case in self.cases]}

    def get_random_case(self) -> Case:
        return choice(self.cases)