
# Structures:
# Write a Python class that represents a Person with name, age, and gender attributes.
# Implement a method to print the details of the person.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender} ")

Person( "XXX", 6, "Boy").print_info()
