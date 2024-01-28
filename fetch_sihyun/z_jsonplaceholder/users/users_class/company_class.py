from z_jsonplaceholder.module.crud_module import create


class Company():
    def __init__(self, name, catch_phrase, bs, user_id):
        self.name = name
        self.catch_phrase = catch_phrase
        self.bs = bs
        self.user_id = user_id

    @staticmethod
    def create_table(create_table):
        create(create_table)

    def __str__(self):
        return f'{self.name}, {self.catch_phrase}, {self.bs}, {self.user_id}'
