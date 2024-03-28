from abc import ABC, abstractmethod
from src.models.user.person import Person


class Login_interface(ABC):
    """Interface for Login """
    @abstractmethod
    def login(self, username : str , password : str) -> Person :
        """login method"""
        raise NotImplementedError("function login is not implemented")




