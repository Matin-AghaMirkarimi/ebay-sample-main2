from src.common.db_handler.db_client import DbClient
from src.models.user.person import Person
from src.models.user.address import Address
from user_dao_interface import UserDAOInterface

class UserDao(UserDAOInterface):
    """Handling database I/O for Person class"""

    db_client: DbClient

    def __init__(self, client: DbClient) -> None:
        self.db_client = client



    def write_user_to_db(self, username: str, password: str, email: str , phone_number : int , firstname : str , address : Address) -> Person:
        """Write a user to db"""
        check = DbClient.run_query(f"""SELECT * FROM Person WHERE username = {username}""")
        if check is None:
            db_res = DbClient.run_query(
                f"""INSERT into User (firstname, phone_number, email_address , username , password ,address  ) VALUES({firstname}, {phone_number},{email}, {username} , {password}, {address})"""
            )

            if db_res is None:
                raise RuntimeError(f"Could not write {username} to database")
        else:
            raise KeyError("This username is Already existed")
        
        result = Person(
            name=firstname,
            phone_number=phone_number,
            email_address=email,
            username=username,
            password=password,
            address=address
        )
        return result




    def read_user_from_db(self, username: str) -> Person:
        """Read user information from db by username"""
        db_res = DbClient.run_query(f"""SELECT * FROM Person WHERE username = {username}""")
        result = Person(
            name=db_res[0],
            phone_number =db_res[1],
            email_address=db_res[2],
            username=db_res[3],
            password=db_res[4],
            address=db_res[5]
        )
        return result




    def get_user_by_id(self, id :str) -> Person:
        """Getting personal information using username"""
        db_res = DbClient.run_query(f"""SELECT * FROM Person WHERE id = {id}""")
        result = Person(
            name=db_res[0],
            phone_number =db_res[1],
            email_address=db_res[2],
            username=db_res[3],
            password=db_res[4],
            address=db_res[5]
        )
        return result

        




