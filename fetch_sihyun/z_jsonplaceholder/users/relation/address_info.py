from z_jsonplaceholder.module.crud_module import create
class AddressInfo:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.street = kwargs.get('street')
        self.suite = kwargs.get('suite')
        self.city = kwargs.get('city')
        self.zipcode = kwargs.get('zipcode')
        self.geo = kwargs.get('geo')

    @staticmethod
    def create_table(create_table):
        create(create_table)

    def __str__(self):
        return f'id: {self.id}, street: {self.street}, suite: {self.suite}, city: {self.city},zipcode: {self.zipcode}, geo: {self.geo}'
