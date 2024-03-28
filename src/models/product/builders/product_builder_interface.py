from __future__ import annotations
from abc import ABC, abstractmethod


from common.utility.date.custom_date import CustomDate
from models.product.product import Product
from models.user.person import Person


class ProductBuilderInterface(ABC):
    """Interface for main product builder"""

    __product: Product

    @abstractmethod
    def build(self) -> Product:
        """Build Product object"""
        raise NotImplementedError("function build is not implemented")

    @abstractmethod
    def reset(self) -> ProductBuilderInterface:
        """Reset the created Product so far"""
        raise NotImplementedError("function reset is not implemented")

    @abstractmethod
    def add_id(self, id: str) -> ProductBuilderInterface:
        raise NotImplementedError("function add_id is not implemented")

    @abstractmethod
    def add_name(self, name: str) -> ProductBuilderInterface:
        raise NotImplementedError("function add_name is not implemented")

    @abstractmethod
    def add_picture_path(self, picture_path: str) -> ProductBuilderInterface:
        raise NotImplementedError("function picture_path is not implemented")

    @abstractmethod
    def add_date_added(self, date_added: CustomDate) -> ProductBuilderInterface:
        raise NotImplementedError("function add_id is not implemented")

    @abstractmethod
    def add_description(self, description: str) -> ProductBuilderInterface:
        raise NotImplementedError("function add_description is not implemented")

    @abstractmethod
    def add_user(self, user: Person) -> ProductBuilderInterface:
        raise NotImplementedError("function add_user is not implemented")
