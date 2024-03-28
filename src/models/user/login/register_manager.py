
from models.user.address import Address
from register_interface import RegisterInterface
from src.models.user.person import Person

from src.common.db_handler.user.user_dao import UserDao
import  logging


class RegisterManager(RegisterInterface):
    """Handling database I/O for register a new user"""
    def register(self, username: str, password: str, email: str, phone_number: int, firstname: str, address : Address) -> Person :
        try:
            result = UserDao.write_user_to_db(username, password, email, phone_number, firstname, address)
        except KeyError as e:
            logging.exception(f"user {username} already exists")
            raise e
        except RuntimeError as e:
            logging.exception(f"Could not write {username} to DB")
            raise e
        
        return result



