class GeoInfo:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.lat = kwargs.get('lat')
        self.lng = kwargs.get('lng')
        self.address_id = kwargs.get('address_id')

    def __str__(self):
        return f'lat: {self.lat}, lng: {self.lng}'
