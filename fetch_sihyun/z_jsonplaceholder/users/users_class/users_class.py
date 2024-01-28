from z_jsonplaceholder.module.crud_module import create


class Users():
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.phone = kwargs.get('phone')
        self.website = kwargs.get('website')

    @staticmethod
    def create_table(create_query):
        create(create_query)

    def __str__(self):
        return f'{self.name}, {self.username}, {self.email}, {self.phone}, {self.website}'
