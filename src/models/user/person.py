from src.models.user.address import Address
from src.common.utility.date.custom_date import CustomDate

class Person:
    """Main user class"""
    name: str
    phone_number: int
    email_address: str
    user_name: str
    password: str
    address: Address
    last_login: CustomDate

    def __init__(
            self,
            name: str,
            phone_number: int,
            email_address: str,
            user_name: str,
            password: str,
            address: Address,
            last_login : CustomDate

    ) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.user_name = user_name
        self.password = password
        self.address = address
        self.last_login = last_login

