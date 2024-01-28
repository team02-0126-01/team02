from z_jsonplaceholder.module.crud_module import create


class Geo():
    def __init__(self, lat, lng, address_id):
        self.lat = lat
        self.lng = lng
        self.address_id = address_id

    @staticmethod
    def create_table(create_table):
        create(create_table)

    def __str__(self):
        return f'{self.lat}, {self.lng}, {self.address_id}'
