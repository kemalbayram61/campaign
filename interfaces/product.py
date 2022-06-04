from abc              import ABC, abstractmethod
from interfaces.enums import ProductCategory
class IProduct(ABC):
    __name     : str
    __price    : str
    __category : ProductCategory

    @abstractmethod
    def setPrice(self, price: float) ->None:
        pass

    @abstractmethod
    def setName(self, name: str) ->None:
        pass

    @abstractmethod
    def setCategory(self, category: str) ->None:
        pass

    @abstractmethod
    def getPrice(self) ->float:
        pass

    @abstractmethod
    def getName(self) ->str:
        pass

    @abstractmethod
    def getCategory(self) ->ProductCategory:
        pass