from z_jsonplaceholder.module.crud_module import create
class GeoInfo:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.lat = kwargs.get('lat')
        self.lng = kwargs.get('lng')
        self.address_id = kwargs.get('address_id')

    @staticmethod
    def create_table(create_table):
        create(create_table)

    def __str__(self):
        return f'lat: {self.lat}, lng: {self.lng}'
