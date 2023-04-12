from Random_name import *

class Animal:
    animal_id = 1
    def __init__(self, name=None):
        if name == None:
            name = Random_name.get_random_name()
        self.name = name
        self.id = Animal.animal_id
        Animal.animal_id += 1

class Dog(Animal):
    def __init__(self, name):
        self.skills = "Лает, кусает"
        self.id = Animal.animal_id
        super().__init__(name)

    def __str__(self):
        return f'id:{self.id}; Class: {type(self).__name__}; Name = {self.name}; Skills: {self.skills}'


class Cat(Animal):
    def __init__(self, name):
        self.skills = "Ловит мышей"
        self.id = Animal.animal_id
        super().__init__(name)

    def __str__(self):
        return f'id:{self.id}; Class: {type(self).__name__}; Name = {self.name}; Skills: {self.skills}'


class Horse(Animal):
    def __init__(self, name):
        self.skills = "Бегает, прыгает"
        self.id = Animal.animal_id
        super().__init__(name)

    def __str__(self):
        return f'id:{self.id}; Class: {type(self).__name__}; Name = {self.name}; Skills: {self.skills}'


if __name__ == '__main__':
    dog = Dog("Patrick")
    cat = Cat("Tom")
    horse = Horse("Plotva")

    print(dog)
    print(cat)
    print(horse)
