from z_jsonplaceholder.module.crud_module import create


class Address:
    def __init__(self, **kwargs):
        self.street = kwargs.get('street')
        self.suite = kwargs.get('suite')
        self.city = kwargs.get('city')
        self.zipcode = kwargs.get('zipcode')
        self.user_id = kwargs.get('user_id')

    @staticmethod
    def create_table(create_query):
        create(create_query)

    def __str__(self):
        return f'{self.street}, {self.suite}, {self.city}, {self.zipcode}, {self.user_id}'
