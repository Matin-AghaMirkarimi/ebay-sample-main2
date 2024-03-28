from abc import ABC, abstractmethod
from src.common.utility.date.custom_date import CustomDate
from src.common.utility.price.price import Price
from src.common.utility.status.status import Status
from src.models.order.order import Order
from src.models.product.product import Product


class OrderManagerInterface(ABC):
    """Interface for showing Methods of orderManager"""

    @abstractmethod
    def change_order_status(self,status : Status , order: Order) -> Order:
        """Change status of order"""
        raise NotImplementedError("function change_order_status is not implemented")


    @abstractmethod
    def add_new_order_detail(self,order_detail : Order.order_details , order: Order) -> Order:
        """Add a new order detail"""
        raise NotImplementedError("function add_new_order_detail is not implemented")


    @abstractmethod
    def edit_order(self, product: Product, date:CustomDate, total_price: Price, descryption: str, order: Order ) -> Order:
        """Edit information of an order """
        raise NotImplementedError("function edit_order is not implemented")








