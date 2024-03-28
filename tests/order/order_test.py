from datetime import datetime
import unittest

from src.common.utility.status.status import Status

from src.common.utility.price.price import Price
from src.common.utility.price.currency import CurrencyType
from src.models.order.order_manager import OrderManager
from src.models.product.product import Product
from src.models.user.person import Person
from src.common.utility.date.custom_date import CustomDate
from src.common.utility.date.date_type import DateType
from src.models.user.address import Address
from src.models.order.order import Order
from src.models.order.order_detail import OrderDetail


class OrderTest(unittest.TestCase):
    def setUp(self) -> None:
        """Run before each test case test to initialize an order"""
        self.order = Order(
            id="1",
            description="This Is My Order Description",
            total_price=Price(CurrencyType.DOLLAR, 1),
            status=Status(1),
            date=CustomDate(DateType.MILADI, datetime.now()),
            user=Person("matin", 444, "test@test", "username", "password", Address(), CustomDate(DateType.MILADI, datetime.now())),
            product=Product()

        )
        self.order_manager = OrderManager()

        return super().setUp()



    def test_adding_new_order_detail(self):
            """Test if we can add new orderdetail successfully"""

            detail = OrderDetail(
            product_id=1,
            quantity=5,
            total_weight=12.5
            )

            order = self.order_manager.add_new_order_detail(detail, self.order)
            self.assertTrue(detail in self.order.order_details)
            self.assertTrue(detail in order.order_details)




    def test_change_order_status(self):
        """Test if we can change order status successfully"""

        status = Order.status = Status(3)
        order = self.order_manager.change_order_status(status, self.order)

        self.assertTrue(status == self.order.status)
        self.assertTrue(status == order.status)





    def test_edit_order(self):
        """Test if we can edit an order successfully"""
        product = Product()
        date = CustomDate(DateType.SHAMSI , datetime.now())
        total_price = Price(CurrencyType.DOLLAR, 14),
        description = "Changed"


        order = self.order_manager.edit_order(product,date,total_price,description, self.order)
        self.assertTrue(self.order.product == product and self.order.date == date and self.order.total_price == total_price and self.order.description == description)
        self.assertTrue(order.product == product and order.date == date and order.total_price == total_price and order.description == description)



if __name__ == "__main__":
    unittest.main()
