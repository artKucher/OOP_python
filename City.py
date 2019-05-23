class City(object):
    def __init__(self, city_name, population):
        self.__city_name = city_name    # устанавливаем имя
        self.__population = population      # устанавливаем возраст

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        if population>=0:
            self.__population = population
        else:
            print("Wrong")
    @property
    def city_name(self):
        return self.__city_name

    def __GetParentChain__(self):
        res = []
        res.append(self.__bases__)
        return res

    def __str__(self):
        return "City name: {} \t population: {}".format(self.__city_name, self.__population)