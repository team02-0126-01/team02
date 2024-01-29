from z_jsonplaceholder.module.crud_module import create
class UserInfo:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.address = kwargs.get('address')
        self.phone = kwargs.get('phone')
        self.website = kwargs.get('website')
        self.company = kwargs.get('company')

    @staticmethod
    def create_table(create_query):
        create(create_query)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, username: {self.username}, email: {self.email}, address: {self.address}, phone: {self.phone}, website: {self.website}, company: {self.company}'