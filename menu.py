from db_handler import DBHandler
from collections.abc import Callable
import strings as strs
from os import system as os_system
from tinydb import Query
from icecream import ic
from rank_class import BaseRank, BaseCase, Case, Rank

class Menu:
    def __init__(self):
        self.db: DBHandler = DBHandler()
        self.query: Query = Query()
        self.allowed_commands: dict[str, Callable] = {strs.Menu.Internal.QUIT_COMMAND: self.quit_func,
                                                      strs.Menu.Internal.ADD_COMMAND: self.add_func,
                                                      strs.Menu.Internal.REMOVE_COMMAND: self.remove_func}

    def mainloop(self):
        while True:

            user_input: str = input(strs.Menu.External.COMMAND_DISPLAY)

            sanitized: str = user_input.lower()

            if sanitized == '':
                random_case: dict[str, str] = self.db.get_random_case()

                os_system(strs.Menu.Internal.CLEAR_COMMAND)

                print(f'{''.join(random_case.keys())}: {''.join(random_case.values())}\n\n')

            elif sanitized in self.allowed_commands:
                self.allowed_commands[user_input.lower()]()

            else:
                print(strs.Menu.External.NO_SUCH_COMMAND)

    def add_func(self) -> None:
        os_system(strs.Menu.Internal.CLEAR_COMMAND)

        user_invalid: bool = True
        user_input: str = ' '

        while user_invalid and user_input != '':
            user_input: str = input(strs.Menu.External.ADD_RANK)

            user_invalid: bool = (not user_input.replace(' ', '').isalnum()) or self.db.check_exists_rank(user_input)

            if user_input == '':
                os_system(strs.Menu.Internal.CLEAR_COMMAND)
                return None

            if user_invalid:
                print(strs.Menu.External.INVALID_CHARACTERS)

            else:
                self.db.add_rank(rank=BaseRank(user_input, cases=self.get_cases()))

            user_invalid = True
            user_input: str = ' '


    def remove_func(self) -> None:
        os_system(strs.Menu.Internal.CLEAR_COMMAND)

        user_invalid: bool = True
        user_input: str = ' '

        while user_invalid and user_input != '':
            user_input: str = input(strs.Menu.External.REMOVE_RANK)

            user_invalid: bool = not user_input.replace(' ', '').isalnum() or not self.db.check_exists_rank(user_input)

            if user_input == '':
                os_system(strs.Menu.Internal.CLEAR_COMMAND)
                return None

            if user_invalid:
                print(strs.Menu.External.RANK_NOT_FOUND)

            else:
                self.db.remove_rank(rank=user_input)

            user_invalid = True
            user_input: str = ' '

    @staticmethod
    def get_cases() -> list[Case]:
        user_input: str = ' '
        user_invalid: bool = True
        cases: list[Case] = []

        while user_input != '' and user_invalid:
            user_input: str = input(strs.Menu.External.ADD_CASE)

            user_invalid: bool = not user_input.replace(' ', '').isalnum()

            if user_input == '':
                os_system(strs.Menu.Internal.CLEAR_COMMAND)
                return cases

            elif user_invalid:
                print(strs.Menu.External.INVALID_CHARACTERS_IN_CASE)

            else:
                cases.append(BaseCase(user_input))

            user_input = ' '
            user_invalid = True


    @staticmethod
    def quit_func() -> None:
        quit()


def main() -> None:
    main_menu: Menu = Menu()
    main_menu.mainloop()

if __name__ == '__main__':
    main()


