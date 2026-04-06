
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def ReadOut(self):
        print(f"My name is {self.name} and I'm {self.age} years old!")

class person_extended(person):
    def __init__(self, name, age, hobby, country):
        super().__init__(name, age)
        self.hobby = hobby
        self.country = country
    def ReadOut(self):
        print(f"""My name is {self.name} and I'm {self.age} years old! 
              I am from {self.country} and have the following hobbies: {self.hobby}""")
        
try:
    name = input("What is your name? ")
    age = str(input("What is your age? "))
    county = input("What country are you from? ")
    hobby = input("What are your hobbies? ")
    user = person_extended(name, age, hobby, county)
    print(user.ReadOut())
except Exception as e:
    print(f"An error occurred: {e}")
