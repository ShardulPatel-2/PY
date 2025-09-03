class Parrot:

    # class atribute
    species = "dinosaur"

    # instance atribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
smurfycat = Parrot("drake", 10)
drake = Parrot("drake", 15)

# access the class attributes
print("smurfycat is a {}".format(smurfycat.species))
print("drake is also a {}".format(drake.species))

# access the instance attributes
print("{} is {} years old".format( smurfycat.name, smurfycat.age))
print("{} is {} years old".format( drake.name, drake.age))