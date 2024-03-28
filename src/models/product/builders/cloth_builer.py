from __future__ import annotations

from models.product.cloth import Cloth
from product_builder import ProductBuilder


class ClothBuilder(ProductBuilder):
    """Interface for main product builder"""

    __product: Cloth

    def __init__(self) -> None:
        self.__product = Cloth()

    def build(self) -> Cloth:
        """Build Product object"""
        return self.__product

    def reset(self) -> ClothBuilder:
        """Reset the created Product so far"""
        self.__product = Cloth()
        return self

    def add_size(self, size: str) -> ClothBuilder:
        self.__product.size = size
        return self

    def add_brand(self, brand: str) -> ClothBuilder:
        self.__product.brand = brand
        return self

    def add_picture_path(self, material: str) -> ClothBuilder:
        self.__product.material = material
        return self
