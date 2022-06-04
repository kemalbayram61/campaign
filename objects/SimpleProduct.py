from interfaces.product import IProduct

class SimpleProduct(IProduct):
    __name     : str
    __price    : str
    __category : str

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

    def getCategory(self) ->str:
        return  self.__category