import random


class Vehicle:
    distance_to_check = None

    def __init__(self, color, track_kilometrage):
        self.color = color
        self.track_kilometrage = track_kilometrage
        self.unit = 1

    def __str__(self):
        return f'color: {self.color}, covered distance: {self.track_kilometrage}'


class Car(Vehicle):
    distance_to_check = 30000

    def __init__(self, color, track_kilometrage, vendor, marketing_slogan):
        super().__init__(color, track_kilometrage)
        self.vendor = vendor
        self.marketing_slogan = marketing_slogan

    def __str__(self):
        return f'vendor: {self.vendor}, slogan: {self.marketing_slogan}, ' + super().__str__()

    def change_slogan(self, comp, new_slogan):
        if self.vendor == comp:
            self.marketing_slogan = new_slogan

    def change_unit(self, new):
        self.unit = new
        self.track_kilometrage /= new


class Truck(Car):
    def __init__(self, color, track_kilometrage, vendor, marketing_slogan, model_name, max_speed):
        super().__init__(color, track_kilometrage, vendor, marketing_slogan)
        self.model_name = model_name
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f', model: {self.model_name}'

    def change_model_name(self, comp, old_name, new_name):
        if self.vendor == comp:
            if self.model_name == old_name:
                self.model_name = new_name


class Family(Car):
    def __init__(self, color, track_kilometrage, vendor, marketing_slogan, model_name, max_speed):
        super().__init__(color, track_kilometrage, vendor, marketing_slogan)
        self.model_name = model_name
        self.max_speed = max_speed

        def __str__(self):
            return super().__str__() + f', model: {self.model_name}'

    def change_model_name(self, comp, old_name, new_name):
        if self.vendor == comp:
            if self.model_name == old_name:
                self.model_name = new_name


class Sport(Car):
    def __init__(self, color, track_kilometrage, vendor, marketing_slogan, model_name, max_speed):
        super().__init__(color, track_kilometrage, vendor, marketing_slogan)
        self.model_name = model_name
        self.max_speed = max_speed

        def __str__(self):
            return f'model: {self.model_name}, {super().__str__()}'

    def change_model_name(self, comp, old_name, new_name):
        if self.vendor == comp:
            if self.model_name == old_name:
                self.model_name = new_name


class Bike(Vehicle):
    def __init__(self, color, track_kilometrage):
        super().__init__(color, track_kilometrage)


class Mountain(Bike):
    def __init__(self, color, track_kilometrage, model_name, max_speed):
        super().__init__(color, track_kilometrage)
        self.model_name = model_name
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f", model: {self.model_name}"


class Road(Bike):
    def __init__(self, color, track_kilometrage, model_name, max_speed):
        super().__init__(color, track_kilometrage)
        self.model_name = model_name
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f", model: {self.model_name}"


def add_rand_distance(obj: Vehicle | Bike | Car | Truck | Family | Sport | Mountain | Road):
    obj.track_kilometrage += random.randint(1, 500) / obj.unit


def distance_until_check(obj: Vehicle):
    if obj.distance_to_check is None:
        return 'no need checks'
    return obj.distance_to_check - (obj.track_kilometrage % obj.distance_to_check)


def max_speed(*vehivle_lst):
    return max(vehivle_lst, key=lambda x: x.max_speed)


if __name__=='__main__':
    Vehicles = [Road('red', 300, 'rainbow', 80), Sport('white', 10292, 'Mazda', 'cars is a love', '6', 250)]
    print(max_speed(*Vehicles))
    print(Car('white', 50000, 'kia', 'lkbkf'))