#inheritance
class Animal:
    def  speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def  bark(self):
        print("Dog Barking")
class Dogchild(Dog):
    def  eat(self):
        print("Eating bread")
d=Dogchild()
d.bark()
d.eat()
d.speak()
