from City import City
class Street(City):
    def __init__(self, city_name, population, street_name):
        City.__init__(self,city_name,population)
        self.__street_name = street_name

    @property
    def street_name(self):
        return self.__street_name

    @street_name.setter
    def street_name(self, street_name):
        self.__street_name = street_name
    def __GetParentChain__(self):
        res = super(Street, self).__GetParentChain__()
        res.append(self.__bases__)
        return res

    def __str__(self):
        return "City name: {} \t population: {} \t street name {}".format(self.city_name, self.population, self.street_name)