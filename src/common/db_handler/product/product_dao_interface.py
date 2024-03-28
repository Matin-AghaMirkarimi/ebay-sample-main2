from abc import ABC, abstractmethod

from models.product.product import Product

from common.db_handler.db_client import DbClient
from typing import List


class ProductDAOInterface(ABC):
    """Interface for reading/writing Products to DB"""

    db_client: DbClient

    @abstractmethod
    def write_product_to_db(self, product: Product) -> None:
        """Write an product to db"""
        raise NotImplementedError("function write_product_to_db is not implemented")

    @abstractmethod
    def read_product_by_id(self, id: str) -> Product:
        """Read a single product from db"""
        raise NotImplementedError("function read_product_by_id is not implemented")

    @abstractmethod
    def read_all_products(self, id: str) -> List[Product]:
        """Read all of the products from db"""
        raise NotImplementedError("function read_all_products is not implemented")
