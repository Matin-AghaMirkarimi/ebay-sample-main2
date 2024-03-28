from src.models.auction.auction import Auction
from src.models.auction.bid import Bid
from src.models.auction.auction_service_interface import AuctionServiceInterface
from src.common.utility.date.custom_date import CustomDate
from src.common.utility.date.date_type import DateType
from src.models.user.person import Person

from datetime import datetime
from typing import Tuple


class FirstPriceAuction(AuctionServiceInterface):
    """Aunction implementing First-Price auction behaviour"""

    def start_auction(self, auction: Auction) -> Auction:
        """Create a new auction by changing it's start_date from null to current time"""
        if auction.start_date is not None:
            raise ValueError("This auction has been started before")

        auction.start_date = CustomDate(DateType.MILADI, datetime.now())
        return auction

    def end_auction(self, auction: Auction) -> Auction:
        """End an existing auctio by changing it's start_date from null to current time"""
        if auction.end_date is not None:
            raise ValueError("This auction has been ended before")

        auction.end_date = CustomDate(DateType.MILADI, datetime.now())
        return auction

    def add_participant(self, auction: Auction, user: Person) -> Auction:
        """Add a participant to an auction"""
        if user in auction.participants:
            raise KeyError("User already exists")

        auction.participants.append(user)

        return auction

    def place_new_bid(self, auction: Auction, bid: Bid) -> Auction:
        """Add a new bid to an auction
        Throw error if user is not added to auction before"""

        if bid.user not in auction.participants:
            raise KeyError("User is not participated in this auction")

        auction.bids.append(bid)
        return auction

    def get_winner(self, auction: Auction) -> Tuple[Person, Bid]:
        """Return winner of an auction"""
        return max(auction.bids, key=lambda b: b.price.value)

    def remove_user(self, auction: Auction, user: Person) -> Auction:
        """Remove a user from an auction"""
        if user not in auction.participants:
            raise KeyError("User is not participated in this auction")

        auction.participants.remove(user)

        return auction
