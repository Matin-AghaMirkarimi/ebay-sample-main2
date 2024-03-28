from src.common.utility.price.currency import CurrencyType


class Price:
    """Class for holding different kind of prices"""

    type: CurrencyType
    value: float

    def __init__(self, type: CurrencyType, value: float) -> None:
        self.type = type
        self.value = value
