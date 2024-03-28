from auction_dao_interface import AuctionDAOInterface
from src.models.auction.auction import Auction
from src.common.db_handler.db_client import DbClient
from typing import List


class AuctionDao(AuctionDAOInterface):
    """Handling database I/O for Auction class"""

    db_client: DbClient

    def __init__(self, client: DbClient) -> None:
        self.db_client = client

    def write_auction_to_db(self, auction: Auction) -> None:
        """Write an auction to db"""
        DbClient.run_query(
            f"""INSERT into auction(id, type, ...) VALUES({auction.id}, {auction.type}, ...)"""
        )

    def read_auction_by_id(self, id: str) -> Auction:
        """Read a single auction from db"""
        db_res = DbClient.run_query(f"""SELECT * FROM auction WHERE id = {id}""")
        result = Auction(
            id=db_res[0],
            atype=db_res[1],
            minimum_starting_bid_price=db_res[2],
            product=db_res[3],
        )

        return result

    def read_all_auctions(self) -> List[Auction]:
        """Read all of the auctions from db"""
        db_res = DbClient.run_query(f"""SELECT * FROM auction""")
        result: List[Auction]

        for auction in db_res:
            result.append(
                Auction(
                    id=auction[0],
                    atype=auction[1],
                    minimum_starting_bid_price=auction[2],
                    product=auction[3],
                )
            )

        return result
