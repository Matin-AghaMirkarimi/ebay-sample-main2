from src.common.utility.date.custom_date import CustomDate
from src.common.utility.price.price import Price
from src.models.user.person import Person


class Bid:
    """Class for modeling a bid"""

    user: Person
    price: Price
    date: CustomDate

    def __init__(self, user: Person, price: Price, date: CustomDate) -> None:
        self.user = user
        self.price = price
        self.date = date
