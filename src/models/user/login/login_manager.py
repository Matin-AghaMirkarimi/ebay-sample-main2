
from login_interface import Login_interface
from src.models.user.person import Person

from src.common.db_handler.login.login_dao import LoginDao
import logging


class LoginManager(Login_interface):
    """Login manager subsystem"""

    def login(self, username: str, password: str) -> Person:
        """Matching username and password by calling loginuser"""
        try:
            result = LoginDao.login_user(username, password)
        except KeyError:
            logging.exception("User Not Found")
        return result




