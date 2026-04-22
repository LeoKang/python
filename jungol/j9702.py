class Profile:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}"

lst = []
N = int(input())
for i in range(1, N+1):
    name, age = input().split()
    p = Profile(name, age)
    lst.append(p)

for i in range(N):
    print(sorted(lst, key=lambda x: x.age, reverse=True)[i])
# 4. --------------------------------
n = int(input())
people = []

for i in range(n):
    name, age = input().split()
    people.append([name, int(age)])

people.sort(key=lambda x: x[1], reverse=True)

for name, age in people:
    print(f"Name:{name}, Age:{age}"）
# 3. -----------------------------------
class P:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
l=[]
n = int(input())
for i in range(n):
    Name, Age = input().split()
    l.append(P(Name, Age))
L = sorted(l, key=lambda x: x.Age, reverse=True)
for p in L:
    print(f"Name:{p.Name}, Age:{p.Age}")
# 2. -------------------------------
class PersonAge:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

N = int(input())
# print(N)
people = [PersonAge(*input().split()) for i in range(N)]

people.sort(key=lambda x: x.age, reverse=True)

for p in people:
    print(f"Name:{p.name}, Age:{p.age}")

# 1. ------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
    def print(self):
        print(f"Name:{self.name}, Age:{self.age}")

N = int(input())
lst = []

for x in range(N):
    name, age = input().split()
    print(name, age)
    p = Person(name, age)
    lst.append(p)

for x in range(len(lst)):
    lst[x].print()

res = []
for x in range(len(lst)):
    p = lst[x]
    for y in range(x+1, len(lst)):
        if p.age < lst[y].age and p.age != 99:
            p = lst[y]
    print(p.print())
    res.append(p)
    p.age = 99
print("---------")
for x in range(len(res)):
    print(res[x].print())        