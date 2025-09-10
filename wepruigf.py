import random
fname = ['John', 'Andre' 'Paul']
lname = ['Smith', 'Doe', 'Paul']
street_names = ['Goon Town', 'Sigma Street', 'Ohio alpha street']
fake_cites = ['New York', 'Los Angeles', 'Chicago']
states = ['NY', 'CA', 'IL']

class Name:
    def __init__(self):
        '''
        num = Total number of names you want to print is default 1
        
        To print more than one name, change the value of num
        '''
        self.num = 1
    def first_name(self):
        #print first name
        for i in range(self.num):
          first = random.choice(fname)
          print(first)

    def last_name(self):
        #print last name
        for i in range(self.num):
          last = random.choice(lname)
          print(last)
   
    def full_profile(self):
        #print full profile
        
        for i in range(self.num):
          first = random.choice(fname)
          last = random.choice(lname)
          phone = f'+91-{random.randint(800, 999)}{random.randint(800, 999)}{random.randint(1000,9999)}'