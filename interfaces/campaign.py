from abc   import ABC, abstractmethod
from enums import CampaignImplementationType, CampaignType, CalculationType
class ICampaign(ABC):
    __name               : str
    __implementationType : CampaignImplementationType
    __compaignType       : CampaignType
    __calculationType    : CalculationType
    __amount             : float
    __count              : int
