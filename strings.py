from dataclasses import dataclass

@dataclass(frozen=True)
class Handler:

    @dataclass(frozen=True)
    class Internal:
        DOTENV_PATH: str = './paths.env'
        DB_PATH: str = 'DB_PATH'