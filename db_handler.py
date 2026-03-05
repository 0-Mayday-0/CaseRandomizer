from os import getenv
from dotenv import load_dotenv
import tinydb as tdb
import strings as strs
from rank_class import Rank, Case

class DBHandler:
    def __init__(self) -> None:
        load_dotenv(strs.Handler.Internal.DOTENV_PATH)
        self.db: tdb.TinyDB = tdb.TinyDB(getenv(strs.Handler.Internal.DB_PATH))

    def add_rank(self, rank: Rank) -> None:
        self.db.table(name=str(rank)).insert(dict(rank))