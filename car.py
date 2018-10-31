from person import Person

class Car:

    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def owner(self):
        return self._owner

    @classmethod
    def cars_driven_by(self, occ):
        chosen_occ = list(filter(lambda p: p._occupation == occ, Person._all))
        chosen_cars = list(filter(lambda car: car.owner in chosen_occ, Car._all))
        people = list(map(lambda p: p.owner.name, chosen_cars))
        return people


pam = Person("Pam Beasley", "Secretary")
toyota = Car("Toyota", "Yaris", 2007, pam)

michael = Person("Michael Scott", "Regional Manager")
sebring = Car("Chrysler", "Sebring Convertible", 2004, michael)

dwight = Person("Dwight Schrute", "Paper Salesperson")
datsun = Car("Datsun", "280Z", 1978, dwight)

meredith = Person("Meredith Palmer", "Purchaser - Supplier Relations")
ford_minivan = Car("Ford", "Aerostar Minivan", 1997, meredith)

jim = Person("Jim Halpert", "Paper Salesperson")
corolla = Car("Toyota", "Corolla", 2000, jim)

stanley = Person("Stanley Hudson", "Paper Salesperson")
camry = Car ("Toyota", "Camry", 2008, stanley)
