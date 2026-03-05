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
        self.current_table: tdb.database.Table | str | None = None


    def get_random_rank(self) -> BaseRank:
        self.current_table = choice(list(self.db.tables()))
        self.current_table = self.db.table(self.current_table)
        return BaseRank(self.current_table.name, cases=[BaseCase(name=case) for case in self.current_table.all()[0][strs.Ranks.Internal.CASES_KEY]])

    def get_random_case(self) -> dict[str, str]:
        random_rank: BaseRank = self.get_random_rank()
        return {self.current_table.name: str(random_rank.get_random_case())}

    def check_exists_rank(self, rank: str) -> bool:
        return rank in self.db.tables()


    def remove_rank(self, rank: str) -> None:
        self.db.drop_table(rank)


    def add_rank(self, rank: Rank) -> None:
        self.db.table(name=str(rank)).insert(rank.__dict__())


def main() -> None:
    db = DBHandler()

    '''db.add_rank(BaseRank(name="Private Rank II", cases=[BaseCase("Huntsman Weapon Case"),
                                                        BaseCase("The Train Collection"),
                                                        BaseCase("The Bank Collection")]))'''


    ic(db.check_exists_rank("Private Rank II"))

if __name__ == "__main__":
    main()