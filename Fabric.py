from Animals import *

class Fabric:

    def create_animal(animal_class: str, name=None):
        if str(animal_class).lower() == "dog":
            animal = Dog(name)
        elif str(animal_class).lower() == "cat":
            animal = Cat(name)
        elif str(animal_class).lower() == "horse":
            animal = Horse(name)
        else:
            print(f"{animal_class}: Не знаю такого")
            return -1

        return animal


if __name__ == '__main__':

    new_animal = Fabric.create_animal("Horse", "bob")
    print(new_animal)