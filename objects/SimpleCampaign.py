from interfaces.campaign import ICampaign
from interfaces.enums    import CampaignType, CampaignImplementationType, CalculationType

class SimpleCampaign(ICampaign):
    __name               : str
    __implementationType : CampaignImplementationType
    __campaignType       : CampaignType
    __calculationType    : CalculationType
    __amount             : float
    __count              : int

    def setName(self, name: str) ->None:
        self.__name = name

    def setImplementationType(self, implementationType: CampaignImplementationType) ->None:
        self.__implementationType = implementationType

    def setCampaignType(self, campaignType: CampaignType) ->None:
        self.__campaignType = campaignType

    def setCalculationType(self, calculationType: CalculationType) ->None:
        self.__calculationType = calculationType

    def setAmount(self, amount: float) ->None:
        self.__amount = amount

    def setCount(self, count: int) ->None:
        self.__count = count

    def getName(self) ->str:
        return  self.__name

    def getImplementationType(self) ->CampaignImplementationType:
        return  self.__implementationType

    def getCampaignType(self) ->CampaignType:
        return  self.__campaignType

    def getCalculationType(self) ->CalculationType:
        return  self.__calculationType

    def getAmount(self) ->float:
        return self.__amount

    def getCount(self) ->int:
        return  self.__count