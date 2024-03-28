from typing import Any

from product_dao_interface import ProductDAOInterface
from models.product.product import Product
from models.product.builders.product_builder import ProductBuilder

from common.db_handler.db_client import DbClient
from typing import List


class ProductDao(ProductDAOInterface):
    """Handling database I/O for Product class"""

    db_client: DbClient

    def __init__(self, client: DbClient) -> None:
        self.db_client = client

    def write_product_to_db(self, product: Product) -> None:
        """Write an product to db"""
        DbClient.run_query(
            f"""INSERT into product(id, name, ...) VALUES({product.id}, {product.name}, ...)"""
        )

    def read_product_by_id(self, id: str) -> Product:
        """Read a single product from db"""
        db_res = DbClient.run_query(f"""SELECT * FROM product WHERE id = {id}""")

        builder = (
            ProductBuilder()
            .add_id(db_res[0])
            .add_name(db_res[1])
            .add_description(db_res[2])
            .add_picture_path(db_res[3])
            .add_date_added(db_res[4])
        )

        return builder.build()

    def read_all_products(self, id: str) -> List[Product]:
        """Read all of the products from db"""
        db_res = DbClient.run_query(f"""SELECT * FROM product""")
        result: List[Product]
        builder: ProductBuilder = ProductBuilder()

        for p in db_res:
            product = (
                builder.add_id(p[0])
                .add_name(p[1])
                .add_description(p[2])
                .add_picture_path(p[3])
                .add_date_added(p[4])
                .build()
            )
            result.append(product)
            builder = builder.reset()

        return result
