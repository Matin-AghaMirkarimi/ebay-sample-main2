from enum import Enum


class Status(Enum):
    """Enum showing different available kind of order status"""

    FAILED = 1
    PROCESSING = 2
    COMPELETED = 3
    ONHOLD = 4
    CANCELED = 5
    REFUNDED = 6

