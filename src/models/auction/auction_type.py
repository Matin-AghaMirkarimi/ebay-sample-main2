from enum import Enum


class AuctionType(Enum):
    """Enum showing different available auctions"""

    FIRST_PRICE = 1
    SECOND_PRICE = 2
    DUTCH_AUCTION = 3
