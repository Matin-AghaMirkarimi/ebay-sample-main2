from src.common.utility.date.custom_date import CustomDate
from src.common.utility.price.price import Price
from src.common.utility.status.status import Status
from src.models.order.order import Order
from src.models.order.order_manager_interface import OrderManagerInterface
from src.models.product.product import Product


class OrderManager(OrderManagerInterface):
    """A class for showing Methods of orderManager"""

    def change_order_status(self, status: Status, order: Order) -> Order:
        """Change status of order in db"""
        order.status = status
        return order


    def add_new_order_detail(self,order_detail : Order.order_details , order: Order) -> Order:
        """add a new order detail to db"""
        order.order_details.append(order_detail)
        return order


    def edit_order(self, product: Product, date:CustomDate ,total_price : Price, description : str , order: Order) -> Order:
        """Edit information of an order in db"""
        order.total_price = total_price
        order.date = date
        order.description = description
        order.product=product
        return order






