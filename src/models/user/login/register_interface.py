from abc import ABC, abstractmethod
from models.user.address import Address


from src.models.user.person import Person


class RegisterInterface(ABC):
    """Interface for registration a user"""
    @abstractmethod
    def register(self, username: str, password: str, email: str, phone_number: int, firstname: str, address : Address) -> Person:
        """Add a new user"""
        raise NotImplementedError("function register is not implemented")



