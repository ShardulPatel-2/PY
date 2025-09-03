class Parrot:

    # instance atribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instantiate the Parrot class
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)
    
# instantiate this object
smurfycat = Parrot("smurfycat", 10)

# call our instance methods 
print(smurfycat.sing("'Happy'"))
print(smurfycat.dance())
