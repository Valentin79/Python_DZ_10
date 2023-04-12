from Fabric import *

animal_1 = Fabric.create_animal("dog", "Charly")
animal_2 = Fabric.create_animal("Cat")
animal_3 = Fabric.create_animal("Horse", "Plotva")
animal_4 = Fabric.create_animal("Hamster", "Boo")

print("{}\n{}\n{}\n{}".format(animal_1, animal_2, animal_3, animal_4))