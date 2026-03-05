from dataclasses import dataclass

@dataclass(frozen=True)
class Ranks:

    @dataclass(frozen=True)
    class Internal:
        NAME_KEY: str = 'name'
        CASES_KEY: str = 'cases'

@dataclass(frozen=True)
class Handler:

    @dataclass(frozen=True)
    class Internal:
        DOTENV_PATH: str = './paths.env'
        DB_PATH: str = 'DB_PATH'