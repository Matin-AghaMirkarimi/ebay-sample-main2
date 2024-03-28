from src.common.db_handler.db_client import DbClient
from src.common.db_handler.order.order_dao_interface import OrderDAOInterface
from src.models.order.order import Order

class OrderDao(OrderDAOInterface):
    """Handling database I/O for Order class"""

    db_client: DbClient

    def __init__(self, client: DbClient) -> None:
        self.db_client = client

    def write_order_to_DB(self, order: Order) -> Order:
        """Write an Order to db"""
        DbClient.run_query(
            f"""INSERT into order(date, user, description , total_price , status ) VALUES({Order.date}, {Order.user},{Order.description}, {Order.total_price} , {Order.status})"""
        )


    def get_order_from_DB(self, id: str) -> Order:
        """Get Order From DB"""
        db_res = DbClient.run_query(f"""SELECT * FROM order WHERE id = {id}""")
        result = Order(
            id=db_res[0],
            date =db_res[1],
            user=db_res[2],
            description=db_res[3],
            totalprice=db_res[4],
            status=db_res[5]
        )

        return result

