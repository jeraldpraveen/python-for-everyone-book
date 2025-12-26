# Inheritance in Python
class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


class Cat(Animal):
    def speak(self):
        return "Cat meows"


c0 = Animal()
c1 = Dog()
c2 = Cat()
print(c0.speak())  # Output: Animal speaks
print(c1.speak())  # Output: Dog barks
print(c2.speak())  # Output: Cat meows
print(isinstance(c1, Animal))  # Output: True
print(isinstance(c2, Animal))  # Output: True
print(issubclass(Dog, Animal))  # Output: True
print(issubclass(Cat, Animal))  # Output: True
print(issubclass(Dog, Cat))     # Output: False
