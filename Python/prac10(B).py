class Chocolate:
    def __init__(self,items):
        self.__items=items
    def __len__(self):
        return len(self.__items)
    def __contains__(self,items):
        return items in self.__items 
fav__ch=Chocolate(["Kitkat","Silk","Munch","5Star"])
print(len(fav__ch))
print("Kitkat" in fav__ch)
print("Silk" in fav__ch)
print("Munch" in fav__ch)
print("5 Star" in fav__ch)
