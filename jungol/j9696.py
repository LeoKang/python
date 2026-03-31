class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

people = []

for _ in range(2):
    n, a = input().split()
    # print(n, a)
    people.append(Person(n, a))

for p in people:
    category = "adult" if p.age >= 18 else "child"
    print(f"{p.name}({p.age}) : {category}")
# 1. -----------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        isOld = 'child'
        if int(age) >= 18:
            isOld = 'adult'
        else:
            isOld = 'child'

        print(f"{name}({age}) : {isOld}")
    
for x in range(2):
    name, age = input().split()
    obj = Person(name, age)
    obj.print()