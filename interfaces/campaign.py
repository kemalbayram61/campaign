from abc   import ABC, abstractmethod
from enums import CampaignImplementationType
class ICampaign(ABC):
    __name               : str
    __implementationType : CampaignImplementationType
    __compaignType       : str