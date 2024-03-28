from datetime import datetime
import unittest


from src.models.auction.first_price_auction import FirstPriceAuction
from src.models.auction.auction import Auction
from src.models.auction.auction_type import AuctionType
from src.models.product.product import Product
from src.common.utility.price.price import Price
from src.common.utility.price.currency import CurrencyType
from src.models.user.person import Person
from src.common.utility.date.custom_date import CustomDate
from src.common.utility.date.date_type import DateType
from src.models.user.address import Address
from src.models.auction.bid import Bid


class TestFirstPriceAuction(unittest.TestCase):
    """Unit tests for first price Auction"""

    def setUp(self) -> None:
        """Run before each test case test to initialize an auction"""
        self.auction = Auction(
            id="1",
            atype=AuctionType.FIRST_PRICE,
            minimum_starting_bid_price=Price(CurrencyType.DOLLAR, 1),
            product=Product(),
            participants=list(),
            bids=list(),
        )
        self.first_price_auction = FirstPriceAuction()

        return super().setUp()

    def test_starting_auction(self):
        """Test if Auction starts successfully"""
        self.assertTrue(self.auction.start_date is None)

        auction = self.first_price_auction.start_auction(self.auction)

        self.assertFalse(auction.start_date is None)
        self.assertFalse(self.auction.start_date is None)

    def test_starting_already_started_auction_fails(self):
        """Test if starting an already started auction fails by raising an Exception"""
        auction = self.first_price_auction.start_auction(self.auction)

        with self.assertRaises(ValueError):
            self.first_price_auction.start_auction(self.auction)

    def test_ending_auction(self):
        """Test if Auction ends successfully"""
        self.assertTrue(self.auction.end_date is None)

        auction = self.first_price_auction.end_auction(self.auction)

        self.assertFalse(auction.end_date is None)
        self.assertFalse(self.auction.end_date is None)

    def test_ending_already_ended_auction_fails(self):
        """Test if ending an already ended auction fails by raising an Exception"""
        auction = self.first_price_auction.end_auction(self.auction)

        with self.assertRaises(ValueError):
            self.first_price_auction.end_auction(self.auction)

    def test_adding_new_participant(self):
        """Test if we can add new participant successfully"""
        self.assertEqual(len(self.auction.participants), 0)

        p = Person(
            name="test",
            phone_number=123,
            email_address="test@test",
            user_name="test",
            password="test",
            address=Address(),
            last_login=CustomDate(DateType.MILADI, datetime.now()),
        )

        auction = self.first_price_auction.add_participant(self.auction, p)

        self.assertTrue(p in self.auction.participants)
        self.assertTrue(p in auction.participants)

    def test_adding_already_added_user_fails(self):
        """Test if adding an already added user fails by raising an Exception"""
        p = Person(
            name="test",
            phone_number=123,
            email_address="test@test",
            user_name="test",
            password="test",
            address=Address(),
            last_login=CustomDate(DateType.MILADI, datetime.now()),
        )

        auction = self.first_price_auction.add_participant(self.auction, p)

        with self.assertRaises(KeyError):
            self.first_price_auction.add_participant(self.auction, p)

    def test_unregistered_user_cannot_add_bid(self):
        """Test if user is not assigned to an auction, can not place a bid"""
        self.assertEqual(len(self.auction.bids), 0)

        p = Person(
            name="test",
            phone_number=123,
            email_address="test@test",
            user_name="test",
            password="test",
            address=Address(),
            last_login=CustomDate(DateType.MILADI, datetime.now()),
        )
        b = Bid(
            user=p,
            price=Price(CurrencyType.DOLLAR, 1),
            date=CustomDate(DateType.MILADI, datetime.now()),
        )

        with self.assertRaises(KeyError):
            self.first_price_auction.place_new_bid(self.auction, b)

    def test_adding_new_bid(self):
        """Test if we can add new bid successfully"""
        self.assertEqual(len(self.auction.bids), 0)

        p = Person(
            name="test",
            phone_number=123,
            email_address="test@test",
            user_name="test",
            password="test",
            address=Address(),
            last_login=CustomDate(DateType.MILADI, datetime.now()),
        )
        b = Bid(
            user=p,
            price=Price(CurrencyType.DOLLAR, 1),
            date=CustomDate(DateType.MILADI, datetime.now()),
        )

        self.first_price_auction.add_participant(self.auction, p)
        auction = self.first_price_auction.place_new_bid(self.auction, b)

        self.assertEqual(len(self.auction.bids), 1)
        self.assertTrue(b in self.auction.bids)

    def test_getting_winner_successfully(self):
        """Test if auction returns the winner successfully using FirstPrice method"""
        p1 = Person(
            name="test_1",
            phone_number=123,
            email_address="test@test",
            user_name="test",
            password="test",
            address=Address(),
            last_login=CustomDate(DateType.MILADI, datetime.now()),
        )
        p2 = Person(
            name="test_2",
            phone_number=123,
            email_address="test@test",
            user_name="test",
            password="test",
            address=Address(),
            last_login=CustomDate(DateType.MILADI, datetime.now()),
        )

        b1 = Bid(
            user=p1,
            price=Price(CurrencyType.DOLLAR, 1),
            date=CustomDate(DateType.MILADI, datetime.now()),
        )
        b2 = Bid(
            user=p2,
            price=Price(CurrencyType.DOLLAR, 2),
            date=CustomDate(DateType.MILADI, datetime.now()),
        )

        self.first_price_auction.add_participant(self.auction, p1)
        self.first_price_auction.add_participant(self.auction, p2)

        self.first_price_auction.place_new_bid(self.auction, b1)
        self.first_price_auction.place_new_bid(self.auction, b2)

        higher_bid = self.first_price_auction.get_winner(self.auction)

        self.assertEqual(higher_bid, b2)

    def test_removing_added_user(self):
        """Test if we can successfully remove a user from an auction"""
        p = Person(
            name="test",
            phone_number=123,
            email_address="test@test",
            user_name="test",
            password="test",
            address=Address(),
            last_login=CustomDate(DateType.MILADI, datetime.now()),
        )

        auction = self.first_price_auction.add_participant(self.auction, p)
        auction = self.first_price_auction.remove_user(auction=auction, user=p)

        # with self.assertRaises(KeyError):
        #     self.first_price_auction.add_participant(self.auction, p)

        self.assertEqual(len(self.auction.participants), 0)

    def test_removing_not_added_user_fails(self):
        """Test if removing a user which doesn't participated in the auction fails"""
        p = Person(
            name="test",
            phone_number=123,
            email_address="test@test",
            user_name="test",
            password="test",
            address=Address(),
            last_login=CustomDate(DateType.MILADI, datetime.now()),
        )

        with self.assertRaises(KeyError):
            self.first_price_auction.remove_user(auction=self.auction, user=p)


if __name__ == "__main__":
    unittest.main()
