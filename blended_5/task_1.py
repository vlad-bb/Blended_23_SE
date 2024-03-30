class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"I am {self.name}, my gender is {self.gender}"


person_1 = Person('Bob', 'man')
person_2 = Person('Ann', 'women')

print(person_1)
print(person_2)

people = [person_1, person_2]
print(people)



