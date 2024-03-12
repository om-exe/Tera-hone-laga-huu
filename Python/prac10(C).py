import abc
class Food(abc.ABC):
    def taste(self):
        pass
class north_indian(Food):
    def taste(self):
        print("Cook")
s=north_indian()
print(isinstance(s,Food))