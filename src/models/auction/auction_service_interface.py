from abc import ABC, abstractmethod
from src.models.auction.auction import Auction
from src.models.auction.bid import Bid
from src.models.user.person import Person
from typing import Tuple


class AuctionServiceInterface(ABC):
    """Interface for showing Auction service functionalities"""

    @abstractmethod
    def start_auction(self, auction: Auction) -> Auction:
        """Create a new auction"""
        raise NotImplementedError("function start_auction is not implemented")

    @abstractmethod
    def end_auction(self, auction: Auction) -> Auction:
        """End an existing auction"""
        raise NotImplementedError("function end_auction is not implemented")

    @abstractmethod
    def add_participant(self, auction: Auction, user: Person) -> Auction:
        """Add a participant to an auction"""
        raise NotImplementedError("function add_participant is not implemented")

    @abstractmethod
    def place_new_bid(self, auction: Auction, bid: Bid) -> Auction:
        """Add a new bid to an auction"""
        raise NotImplementedError("function place_new_bid is not implemented")

    @abstractmethod
    def get_winner(self, auction: Auction) -> Tuple[Person, Bid]:
        """Return winner of an auction"""
        raise NotImplementedError("function get_winner is not implemented")

    @abstractmethod
    def remove_user(self, auction: Auction, user: Person) -> Auction:
        """Remove a user from an auction"""
        raise NotImplementedError("function remove_user is not implemented")
