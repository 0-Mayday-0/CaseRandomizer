from dataclasses import dataclass


@dataclass(frozen=True)
class Menu:

    @dataclass(frozen=True)
    class Internal:
        QUIT_COMMAND: str = 'q'
        ADD_COMMAND: str = 'a'
        REMOVE_COMMAND: str = 'r'
        CLEAR_COMMAND: str = 'cls'

    @dataclass(frozen=True)
    class External:
        COMMAND_DISPLAY: str = '[A]dd rank\n[R]emove rank\n[Q]uit\n\nCommand (leave empty for random case): '
        NO_SUCH_COMMAND: str = "The command doesn't exist.\n\n"
        ADD_RANK: str = "Enter the name of the rank to add, leave blank to exit to main menu: "
        INVALID_CHARACTERS: str = "Invalid characters in input, or rank already exists, please only use letters and numbers.\n"
        ADD_CASE: str = "Enter a case to add, leave blank to save cases and go back to rank adding: "
        INVALID_CHARACTERS_IN_CASE: str = "Invalid characters in input, please use only letters and numbers.\n"
        REMOVE_RANK: str = "Enter the exact name of the rank to remove, leave blank to exit to main menu: "
        RANK_NOT_FOUND: str = "The rank doesn't exist.\n\n"


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