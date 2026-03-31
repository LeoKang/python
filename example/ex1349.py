class Parent:
    def method_a(self):
        print("method_a()")

class Children(Parent):
    def method_b(self):
        super().method_a()
        print("method_b()")

# p1 = Parent()
# p1.method_a()

p2 = Children()
p2.method_a()
p2.method_b()