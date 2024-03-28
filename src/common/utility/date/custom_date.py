from datetime import datetime
from src.common.utility.date.date_type import DateType


class CustomDate:
    """Custom class for handling different kind of dates"""

    date_type: DateType
    date_value: datetime

    def __init__(self, dtype: DateType, dvalue: datetime) -> None:
        self.date_type = dtype
        self.date_value = dvalue
