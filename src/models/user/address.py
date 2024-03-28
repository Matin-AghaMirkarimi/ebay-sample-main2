import re


class Address:
    """Class for modeling an Address information"""
    street: str
    city: str
    state: str
    postal_code: str
    country: str

    # def __init__(self,country: str ,city: str , street:str, state: str ,postal_code: str ) -> None:
    #     self.street = street
    #     self.city = city
    #     self.state=state
    #     self.postal_code=postal_code
    #     self.country=country

    # def validation(user_country: country , user_postal_code =postal_code) :
    #     if (user_country == 'UNITED STATES') and (user_postal_code == [re.compile('^(\\d{5})(?:[ \\-](\\d{4}))?$')]) :
    #         pass
    #     else:
    #         raise "Invalid Information"
