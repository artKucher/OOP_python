from Street import  Street
class Building(Street):
    def __init__(self, city_name, population, street_name, building_number):
        Street.__init__(self,city_name,population, street_name)
        self.__building_number = building_number

    @property
    def building_number(self):
        return self.__building_number

    @building_number.setter
    def building_number(self, building_number):
        self.__building_number = building_number

    def __str__(self):
        return "City name: {} \t population: {} \t street name {} \t building number {}".format(self.city_name, self.population, self.street_name, self.building_number)