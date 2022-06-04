from abc import ABC, abstractmethod

class IProduct(ABC):
    __name     : str
    __price    : str
    __category : str

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
    def getCategory(self) ->str:
        pass
