"""
Factory pattern is a creational pattern that uses factory methods to deal
with the problems of creating objects without having to specify the exact
class of the object that will be created

In this code, we will use car factory example
"""

# 1. Create a metaclass to catch the kind of subclass
KINDS = {}
class MetaCar(type):
    def __init__(cls, name, bases, clsdict):
        # 2. If the class isn't the base class, print the name of the subclass
        #    (Car is base class while MetaCar is meta class)
        if len(cls.mro()) > 2:
            print(f"Subclassed by {name}")
            # 3. Store the subclass type inside dict
            KINDS[cls.kind] = cls

        super(MetaCar, cls).__init__(name, bases, clsdict)

# 4. This is the base class
class Car(metaclass=MetaCar):
    ...

# 5. The the below is the concrete car class
class FlyingCar(Car):
    kind = "flying"
    def __init__(self, name):
        self.name = name

class TurboCar(Car):
    kind = "turbo"
    def __init__(self, name):
        self.name = name

# 6. This is the factory that focused on making car
class CarFactory:
    def create_car(self, name: str, kind: str) -> Car:
        car = KINDS.get(kind)
        return car(name)


if __name__ == "__main__":
    factory = CarFactory()
    flying_car = factory.create_car("nein", "flying")
    print(flying_car)