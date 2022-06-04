from enum import Enum

class CampaignImplementationType(Enum):
    PRODUCT      = 0
    PRODUCT_TYPE = 1

class CampaignType(Enum):
    TOTAL_PRICE    = 0
    EACH_PRICE     = 1
    SUBTRACT_PRICE = 2

class CalculationType(Enum):
    AMOUNT = 0
    RATE   = 1