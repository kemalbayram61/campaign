from interfaces.campaign import ICampaign
from interfaces.enums    import CampaignType, CampaignImplementationType, CalculationType, ProductCategory

class SimpleCampaign(ICampaign):
    __name               : str
    __implementationType : CampaignImplementationType
    __campaignType       : CampaignType
    __calculationType    : CalculationType
    __amount             : float
    __count              : int
    __productNameList    : list[str]
    __productCategoryList: list[ProductCategory]

    def __init__(self, name: str, implementationType: CampaignImplementationType, campaignType: CampaignType, calculationType: CalculationType, amount: float, count: int, productNameList: list[str], productCategoryList: list[ProductCategory]):
        self.__name                = name
        self.__implementationType  = implementationType
        self.__campaignType        = campaignType
        self.__calculationType     = calculationType
        self.__amount              = amount
        self.__productNameList     = productNameList
        self.__productCategoryList = productCategoryList
        self.__count               = count


    def setProductNamelist(self, namelist: list[str]) ->None:
        self.__productNameList = namelist

    def setProductCategorylist(self, categoryList: list[ProductCategory]) ->None:
        self.__productCategoryList = categoryList

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

    def getProductNamelist(self) ->list[str]:
        return self.__productNameList

    def getProductCategorylist(self) ->list[ProductCategory]:
        return self.__productCategoryList

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