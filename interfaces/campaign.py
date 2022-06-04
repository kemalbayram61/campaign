from abc   import ABC, abstractmethod
from enums import CampaignImplementationType, CampaignType, CalculationType
class ICampaign(ABC):
    __name               : str
    __implementationType : CampaignImplementationType
    __campaignType       : CampaignType
    __calculationType    : CalculationType
    __amount             : float
    __count              : int

    @abstractmethod
    def setName(self, name: str) ->None:
        pass

    @abstractmethod
    def setImplementationType(self, implementationType: CampaignImplementationType) ->None:
        pass

    @abstractmethod
    def setCampaignType(self, campaignType: CampaignType) ->None:
        pass

    @abstractmethod
    def setCalculationType(self, calculationType: CalculationType) ->None:
        pass

    @abstractmethod
    def setAmount(self, amount: float) ->None:
        pass

    @abstractmethod
    def setCount(self, count: int) ->None:
        pass

    @abstractmethod
    def getName(self) ->str:
        pass

    @abstractmethod
    def getImplementationType(self) ->CampaignImplementationType:
        pass

    @abstractmethod
    def getCampaignType(self) ->CampaignType:
        pass

    @abstractmethod
    def getCalculationType(self) ->CalculationType:
        pass

    @abstractmethod
    def getAmount(self) ->float:
        pass

    @abstractmethod
    def getCount(self) ->int:
        pass