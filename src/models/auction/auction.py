from src.models.auction.auction_type import AuctionType
from src.models.auction.bid import Bid
from src.common.utility.date.custom_date import CustomDate
from src.common.utility.price.price import Price
from src.models.user.person import Person
from src.models.product.product import Product


from typing import List, Tuple


class Auction:
    """Class for modeling an auction"""

    id: str
    type: AuctionType
    start_date: CustomDate = None  # None shows that auction is not started yet
    end_date: CustomDate = None  # None shows that auction is not finished yet
    minimum_starting_bid_price: Price
    participants: List[
        Person
    ] = list()  # at starting of auction, there aren't any participants
    product: Product
    bids: List[Bid] = list()  # at starting of auction, there aren't any bids

    def __init__(
        self,
        id: str,
        atype: AuctionType,
        minimum_starting_bid_price: Price,
        product: Product,
        start_date: CustomDate = None,
        end_date: CustomDate = None,
        participants: List[Person] = list(),
        bids: List[Bid] = list(),
    ) -> None:
        self.id = id
        self.type = atype
        self.start_date = start_date
        self.end_date = end_date
        self.minimum_starting_bid_price = minimum_starting_bid_price
        self.participants = participants
        self.product = product
        self.bids = bids
