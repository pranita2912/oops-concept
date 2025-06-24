#3] use the abc module to define an abstract class animal with an abstract method sound().create subclasses DOg and Cat to implement the sound()mrthod.


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")

d = Dog()
d.sound()

c = Cat()
c.sound()
