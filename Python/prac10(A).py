from abc import ABC , abstractmethod
class car(ABC):
    def milenge(self):
        pass
class Tesla(car):
    def milenge(self):
        print("The milenge is 30kmph")
class Suzuki(car):
    def milenge(self):
        print("The milenge is 25kmph")
t=Tesla()
t.milenge()
s=Suzuki()
s.milenge()