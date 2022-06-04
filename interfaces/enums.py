from enum import Enum

class ProductCategory(Enum):
    C1 = 0
    C2 = 1
    C3 = 2
    C4 = 3
    C5 = 4
    CE = 5

class CampaignImplementationType(Enum):
    PRODUCT          = 0
    PRODUCT_CATEGORY = 1

class CampaignType(Enum):
    TOTAL_PRICE    = 0
    EACH_PRICE     = 1
    SUBTRACT_PRICE = 2

class CalculationType(Enum):
    AMOUNT = 0
    RATE   = 1
    BIGGEST= 2
    LOWEST = 3