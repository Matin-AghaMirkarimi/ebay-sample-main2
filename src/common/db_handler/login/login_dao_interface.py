from abc import ABC, abstractmethod

from src.models.user.person import Person


class LoginDAOInterface(ABC):
    """Interface for userLogin"""


    @abstractmethod
    def login_user(self, username : str , password : str) -> Person:
        """Find user from username"""
        raise NotImplementedError("function get_user_by_id is not implemented")
