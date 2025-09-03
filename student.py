class CSSstudent:

    #Class Variable
    stream = "cse"

    #the init method or constructor
    def __init__(self, name, rollnumber):

         # Instance Variable   
        self.roll = roll  

        def setAdress(self, address):
            self.address = address

        #Retrives instance Variable
        def getAddress(self):
            return self.address
        
# Driver code
add = CSSstudent(101)
add.setAdress("Lucknow")
print(add.getAddress())

# Object CSStudent class 
a = CSSstudent(101)
b = CSSstudent(102)
  
print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.roll)    # prints 101
  
# Class variables can be accessed using class
# name also
print(CSSstudent.stream) # prints "cse"  

