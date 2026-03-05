from os import getenv
from dotenv import load_dotenv
import tinydb as tdb
import strings as strs
from rank_class import BaseCase, BaseRank, Case, Rank
from random import choice
from icecream import ic

class DBHandler:
    def __init__(self) -> None:
        load_dotenv(strs.Handler.Internal.DOTENV_PATH)
        self.query: tdb.Query = tdb.Query()
        self.db: tdb.TinyDB = tdb.TinyDB(getenv(strs.Handler.Internal.DB_PATH))
        self.tables: set[str] = self.db.tables()
        self.current_table: tdb.database.Table | str | None = None

        ic(self.tables)

    def get_random_rank(self) -> BaseRank:
        self.current_table = choice(list(self.tables))
        self.current_table = self.db.table(self.current_table)
        ic(self.current_table.all())
        return BaseRank(self.current_table.name, cases=[BaseCase(name=case) for case in self.current_table.all()[0][strs.Ranks.Internal.CASES_KEY]])

    def get_random_case(self) -> dict[str, str]:
        return {self.current_table.name: self.get_random_rank().get_random_case().name}


    def add_rank(self, rank: Rank) -> None:
        self.db.table(name=str(rank)).insert(rank.__dict__())


def main() -> None:
    db = DBHandler()

    '''db.add_rank(BaseRank(name="Private Rank II", cases=[BaseCase("Huntsman Weapon Case"),
                                                        BaseCase("The Train Collection"),
                                                        BaseCase("The Bank Collection")]))'''

    ic(db.get_random_rank())

if __name__ == "__main__":
    main()