from src.common.utility.date.custom_date import CustomDate
from src.models.user.person import Person


class Product:
    """Main product class"""

    id: str
    name: str
    picture_path: str
    date_added: CustomDate
    description: CustomDate
    added_user: Person
