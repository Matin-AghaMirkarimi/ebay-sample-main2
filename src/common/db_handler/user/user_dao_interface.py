from abc import ABC, abstractmethod
from models.user.address import Address


from src.models.user.person import Person


class UserDAOInterface(ABC):
    """Interface for showing users service functionalities"""

    @abstractmethod
    def read_user_from_db(self, person: Person) -> Person:
        """Read a new user from DB"""
        raise NotImplementedError("function read_user_from_db is not implemented")

    @abstractmethod
    def write_user_to_db(self, username: str, password: str, email: str , phone_number : int , firstname : str , address : Address) -> Person:
        """Write a new user to DB"""
        raise NotImplementedError("function write_user_to_db is not implemented")

    @abstractmethod
    def get_user_by_id(self, person: Person) -> Person:
        """Getting personal information using username"""
        raise NotImplementedError("function get_user_by_id is not implemented")
