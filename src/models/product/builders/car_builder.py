from __future__ import annotations

from models.product.car import Car
from product_builder import ProductBuilder


class CarBuilder(ProductBuilder):
    """Interface for main product builder"""

    __product: Car

    def __init__(self) -> None:
        self.__product = Car()

    def build(self) -> Car:
        """Build Product object"""
        return self.__product

    def reset(self) -> CarBuilder:
        """Reset the created Product so far"""
        self.__product = Car()
        return self

    def add_color(self, color: str) -> CarBuilder:
        self.__product.color = color
        return self

    def add_vin_numer(self, vin_numer: str) -> CarBuilder:
        self.__product.vin_numer = vin_numer
        return self

    def add_creator(self, creator: str) -> CarBuilder:
        self.__product.creator = creator
        return self
