from src.common.utility.date.custom_date import CustomDate
from src.common.utility.gender.gender import Gender
from src.models.user.person import Person


class PersonalAccount(Person):
    """Class for modeling a personal account"""
    birthdate: CustomDate
    age: int
    gender: Gender

