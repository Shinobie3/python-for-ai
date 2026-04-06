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
        



kenthi = person("Kentiii", 62)
print(kenthi.ReadOut())

mama = person("mama", 57)
print(mama.ReadOut())

kenthi_v = person_extended("Kenthi", 62, "motorcycle", "Germany")
print(kenthi_v.ReadOut())