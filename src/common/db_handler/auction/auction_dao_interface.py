from abc import ABC, abstractmethod
from src.models.auction.auction import Auction
from src.common.db_handler.db_client import DbClient
from typing import List


class AuctionDAOInterface(ABC):
    """Interface for reading/writing Auctions to DB"""

    db_client: DbClient

    @abstractmethod
    def write_auction_to_db(self, auction: Auction) -> None:
        """Write an auction to db"""
        raise NotImplementedError("function write_auction_to_db is not implemented")

    @abstractmethod
    def read_auction_by_id(self, id: str) -> Auction:
        """Read a single auction from db"""
        raise NotImplementedError("function read_auction_by_id is not implemented")

    @abstractmethod
    def read_all_auctions(self) -> List[Auction]:
        """Read all of the auctions from db"""
        raise NotImplementedError("function read_all_auctions is not implemented")
