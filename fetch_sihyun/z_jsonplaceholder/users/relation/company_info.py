from z_jsonplaceholder.module.crud_module import create
class CompanyInfo:
    def __init__(self,  **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.catch_phrase = kwargs.get('catch_phrase')
        self.bs = kwargs.get('bs')

    @staticmethod
    def create_table(create_table):
        create(create_table)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, catch_phrase: {self.catch_phrase}, bs: {self.bs}'