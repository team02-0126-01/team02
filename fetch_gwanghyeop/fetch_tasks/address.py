from geo import Geo

class Address:
    def __init__(self, id: int, street: str, suite: str, city: str, zipcode: str, geo: Geo):
        self.id = id
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo
