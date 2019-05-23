from Street import  Street
from City import City
from Building import Building
from Apartment import Apartment

def search(list, x, what):
    res = []
    if int(x) == 1:
        for m in list:
            print(m.__class__.__subclasses__())
            if m.city_name == what:
                res.append(m)
    elif int(x) == 2:
        for m in list:
            if m.population == what:
                res.append(m)
    elif int(x) == 3:
        for m in list:
            if m.street == what:
                res.append(m)
    elif int(x) == 4:
        for m in list:
            if m.building_number == what:
                res.append(m)
    else:
        for m in list:
            if m.apartment_number == what:
                res.append(m)
    return res

def delete(list, x,what):
    res = search(list,x,what)
    for m in res:
        list.remove(m)
    return list
def main():
    list = []
    while(True):
        print("1 - add new")
        print("2 - delete")
        print("3 - search")
        print("4 - show all")
        x = input()
        if int(x)==1 :
            print("City name:")
            city_name = input()
            print("population:")
            population = input()
            print("Street name")
            street_name = input()
            print("Building number:")
            building_number = input()
            print("Apartment number:")
            apartment_number = input()
            if street_name=="" and building_number=="" and apartment_number=="":
                item = City(city_name,population)
            elif building_number=="" and apartment_number=="":
                item = Street(city_name, population,street_name)
            elif apartment_number=="":
                item = Building(city_name,population,street_name,building_number)
            else:
                item = Apartment(city_name,population,street_name,building_number,apartment_number)

            list.append(item)
        elif int(x)==2:
            print("1 - City name")
            print("2 - Population")
            print("3 - Street name")
            print("4 - Building number")
            print("5 - Apartment")
            field = input()
            print("What?")
            what = input()
            print("DELETED")
            for m in delete(list, field, what):
                print(m)
        elif int(x)==3:
            print("1 - City name")
            print("2 - Population")
            print("3 - Street name")
            print("4 - Building number")
            print("5 - Apartment")
            field = input()
            print("What?")
            what = input()

            for m in search(list, field, what):
                print(m)
        else :
            for m in list:
                print(m)

if __name__ == '__main__':
    main()