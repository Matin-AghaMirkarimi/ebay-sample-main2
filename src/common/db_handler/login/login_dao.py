from src.common.db_handler.db_client import DbClient
from src.common.db_handler.login.login_dao_interface import LoginDAOInterface
from src.models.user.person import Person


class LoginDao(LoginDAOInterface):
    """Handling database I/O for userlogin"""

    db_client: DbClient

    def __init__(self, client: DbClient) -> None:
        self.db_client = client


    def login_user(self, username : str , password : str) -> Person:
        """Find user by username from db"""
        result = DbClient.run_query(f"""SELECT * FROM Person WHERE username = {username} AND password = HASH({password})""")
        if result is None :
            raise KeyError("Username or password is wrong")
        
        result = Person(
            name=result[0],
            phone_number =result[1],
            email_address=result[2],
            username=result[3],
            password=result[4],
            address=result[5]
        )
        return result