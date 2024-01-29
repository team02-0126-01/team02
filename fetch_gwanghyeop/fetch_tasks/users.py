from address import Address
from company import Company

class Users:
    def __init__(self, id: int, name: str, username: str, address: Address, email: str, phone: str, website: str, company: Company):
        self.id = id
        self.name = name
        self.username = username
        self.address = address
        self.email = email
        self.phone = phone
        self.website = website
        self.company = company