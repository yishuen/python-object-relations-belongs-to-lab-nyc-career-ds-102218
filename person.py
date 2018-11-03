# import car class here
from car import Car

class Person:

    _all = []

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
        Person._all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def occupation(self):
        return self._occupation

    @classmethod
    def has_oldest_car(cls):
        cars = Car._all
        oldest = cars[0]
        for car in cars:
            if car.year < oldest.year:
                oldest = car
        return oldest.owner

    @classmethod
    def drives_a(cls, make):
        car_makes = {}
        for car in Car._all:
            car_makes[car._owner] = car._make
        matches = {}
        for k, v in car_makes.items():
            if v == make:
                matches[k] = v
        return list(map(lambda obj: obj, matches.keys()))

    def drives_same_make_as_me(self):
        my_make = list(filter(lambda car: car.owner == self, Car._all))[0]._make
        print(my_make)
        matches = list(filter(lambda car: car.make == my_make, Car._all))
        matches_xself = list(filter(lambda car: car.owner != self, matches))
        people = list(map(lambda car: car.owner, matches_xself))
        return people
