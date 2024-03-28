from src.common.utility.date.custom_date import CustomDate
from src.common.utility.price.price import Price
from typing import List, Tuple
from src.common.utility.status.status import Status
from src.models.user.person import Person
from src.models.product.product import Product
from src.models.order.order_detail import OrderDetail


class Order:
    """Class for modeling an order"""
    id: str
    description: str
    total_price: Price
    status: Status
    date: CustomDate = None
    user: Person
    order_details: List[OrderDetail] = None,
    product: Product

    def __init__(
            self,
            id: str,
            description: str,
            total_price: Price,
            user: Person,
            product: Product,
            status: Status,
            order_details: List[OrderDetail] = list(),
            date: CustomDate = None,

    ) -> None:
        self.id = id
        self.description = description
        self.total_price = total_price
        self.user = user
        self.product = product
        self.status = status
        self.date = date
        self.order_details = order_details
