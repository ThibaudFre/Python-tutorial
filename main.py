#Operator Overloading

class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Dog("Roger", 8)
syd = Dog("syd", 9)

print(roger > syd)