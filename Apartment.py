from Building import Building

class Apartment(Building):
    def __init__(self, city_name, population, street_name, building_number, apartment_number):
        Building.__init__(self,city_name,population, street_name, building_number)
        self.__apartment_number = apartment_number
        self.qwer = 1


    @property
    def apartment_number(self):
        return self.__apartment_number

    @apartment_number.setter
    def apartment_number(self, apartment_number):
        self.__apartment_number = apartment_number

    def __str__(self):
        return "City name: {} \t population: {} \t street name {} \t building number {} \t apartment_number {}".format(self.city_name, self.population, self.street_name, self.building_number, self.apartment_number)