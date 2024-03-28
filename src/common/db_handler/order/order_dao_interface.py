from abc import ABC, abstractmethod
from src.models.order.order import Order


class OrderDAOInterface(ABC):
    """Interface for showing Order service functionalities"""

    @abstractmethod
    def write_order_to_DB(self, order: Order) -> Order:
        """Write a new order to DB"""
        raise NotImplementedError("function write_order_to_DB is not implemented")

    @abstractmethod
    def get_order_from_DB(self, order: Order) -> Order:
        """Get Order From DB"""
        raise NotImplementedError("function get_order_from_DB is not implemented")



