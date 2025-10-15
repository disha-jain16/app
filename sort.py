class Person:  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
    def __repr__(self):  
        return f"{self.name} ({self.age})"  
  
people = [  
    Person("Alice", 30),  
    Person("Bob", 25),  
    Person("Charlie", 35)  
]  
  
sorted_people = sorted(people, key=lambda p: p.age)  
print(sorted_people)  
