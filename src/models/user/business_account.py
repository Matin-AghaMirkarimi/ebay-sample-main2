from src.models.user.person import Person
from src.models.user.business_card_number import BusinessCardNumber


class BusinessAccount(Person):
    """Class for modeling an Account business"""
    business_id: int
    business_credit_card: BusinessCardNumber

    def validation_business_account(self):
        """Validation a business account"""
        pass
