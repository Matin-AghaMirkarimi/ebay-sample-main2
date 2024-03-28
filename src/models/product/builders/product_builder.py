from __future__ import annotations

from common.utility.date.custom_date import CustomDate
from models.product.product import Product
from models.user.person import Person
from product_builder_interface import ProductBuilderInterface


class ProductBuilder(ProductBuilderInterface):
    """Builder pattern for Product"""

    __product: Product

    def __init__(self) -> None:
        self.__product = Product()

    def build(self) -> Product:
        """Build Product object"""
        return self.__product

    def reset(self) -> ProductBuilder:
        """Reset the created Product so far"""
        self.__product = Product()
        return self

    def add_id(self, id: str) -> ProductBuilder:
        self.__product.id = id
        return self

    def add_name(self, name: str) -> ProductBuilder:
        self.__product.name = name
        return self

    def add_picture_path(self, picture_path: str) -> ProductBuilder:
        self.__product.picture_path = picture_path
        return self

    def add_date_added(self, date_added: CustomDate) -> ProductBuilder:
        self.__product.date_added = date_added
        return self

    def add_description(self, description: str) -> ProductBuilder:
        self.__product.description = description
        return self

    def add_user(self, user: Person) -> ProductBuilder:
        self.__product.user = user
        return self
