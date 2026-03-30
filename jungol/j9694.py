class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        print(f'my name is {self.name}.')
        print(f'I am {self.age} years old')

name, age = input().split()
# print(name, age)
p1 = person(name, age)
p1.print()

# 4. --------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name}.\nI am {self.age} years old."

name, age = input().split()
p = Person(name, int(age))
print(p)

# 3. ---------------------------------------

class My_name:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name, age = input().split()
person = My_name(name, age)

print(f"My name is {person.name}.")
print(f"I am {person.age} years old.")
# 2. --------------------------------------
class Box:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a,b=input().split()
d=Box(a,b)
print(f"My name is {d.name}.")
print(f"I am {d.age} years old.")

# 1. ---------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

name, age = input().split()
# print(name, age)
p1 = Person(name, age)
p1.print()
