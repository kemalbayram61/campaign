from interfaces.product import IProduct
from interfaces.enums   import ProductCategory
class SimpleProduct(IProduct):
    __name     : str
    __price    : str
    __category : ProductCategory

    def __init__(self, name, price, category):
        self.__name     = name
        self.__price    = price
        self.__category = category

    def __str__(self):
        return  self.__name + " " + str(self.__price) + " " + self.__category.name

    def setPrice(self, price: float) ->None:
        self.__price = price

    def setName(self, name: str) ->None:
        self.__name = name

    def setCategory(self, category: str) ->None:
        self.__category = category

    def getPrice(self) ->float:
        return  self.__price

    def getName(self) ->str:
        return  self.__name

    def getCategory(self) ->ProductCategory:
        return  self.__category