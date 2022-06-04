from objects.SimpleProduct    import SimpleProduct
from interfaces.enums         import CampaignType, CampaignImplementationType, CalculationType, ProductCategory
from objects.request          import Request
from objects.response         import Response

class CampaignCalculator:
    def getProductsByCategory(self, productList: list[SimpleProduct], categoryList: list[ProductCategory]) ->list[SimpleProduct]:
        __responselist: list[SimpleProduct] = []
        for product in productList:
            if(product.getCategory() in categoryList or ProductCategory.CE in categoryList):
                __responselist.append(product)
        return  __responselist

    def getProductsByName(self, productList: list[SimpleProduct], namelist: list[str]) ->list[SimpleProduct]:
        __responselist: list[SimpleProduct] = []
        for product in productList:
            if(product.getName() in namelist):
                __responselist.append(product)
        return  __responselist

    def evaluatePriceOfTotalPriceByRate(self, productList: list[SimpleProduct], rate: float) ->float:
        __totalPrice: float = 0.0
        for product in productList:
            __totalPrice = __totalPrice + product.getPrice()

        return __totalPrice - __totalPrice * rate / 100

    def evaluatePriceOfTotalPriceByAmount(self, productList: list[SimpleProduct], amount: float) -> float:
        __totalPrice: float = 0.0
        for product in productList:
            __totalPrice = __totalPrice + product.getPrice()

        return __totalPrice - amount

    def evaluatePriceOfEachPriceByRate(self, productList: list[SimpleProduct], rate: float) ->list[SimpleProduct]:
        __totalPrice: float = 0.0
        for product in productList:
            __currentPrice = product.getPrice()
            product.setPrice(__currentPrice - __currentPrice * rate / 100)

        return productList

    def evaluatePriceOfEachPriceByAmount(self, productList: list[SimpleProduct], amount: float) ->list[SimpleProduct]:
        __totalPrice: float = 0.0
        for product in productList:
            __currentPrice = product.getPrice()
            product.setPrice(__currentPrice - amount)

        return productList

    #temporarily used bubble sort
    def sortProductsByPrice(self, productList: list[SimpleProduct]) ->list[SimpleProduct]:
        for i in range(len(productList)):
            for j in range(len(productList) - i - 1):
                if(productList[j].getPrice() > productList[j + 1].getPrice()):
                    __temp = productList[j]
                    productList[j]     = productList[j + 1]
                    productList[j + 1] = __temp

        return productList

    def evaluatePriceWithoutBiggest(self, productList: list[SimpleProduct], withoutCount: int) ->float:
        __response: float = 0.0
        for i in range(len(productList) - withoutCount):
            __response = __response + productList[i].getPrice()

        return __response

    def evaluatePriceWithoutLowest(self, productList: list[SimpleProduct], withoutCount: int) ->float:
        __response: float = 0.0
        for i in range(withoutCount, len(productList)):
            __response = __response + productList[i].getPrice()

        return __response

    def calculate(self, request: Request) ->Response:
        __productList: list[SimpleProduct] = []
        __totalPrice : float                = 0.0
        if(request.campaign.getImplementationType() == CampaignImplementationType.PRODUCT):
            __productList = self.getProductsByName(request.productList, request.campaign.getProductNamelist())
        elif(request.campaign.getImplementationType() == CampaignImplementationType.PRODUCT_CATEGORY):
            __productList = self.getProductsByCategory(request.productList, request.campaign.getProductCategorylist())

        if(request.campaign.getCampaignType() == CampaignType.TOTAL_PRICE):
            if(request.campaign.getCalculationType() == CalculationType.AMOUNT):
                __totalPrice = self.evaluatePriceOfTotalPriceByAmount(__productList, request.campaign.getAmount())
            elif(request.campaign.getCalculationType() == CalculationType.RATE):
                __totalPrice = self.evaluatePriceOfTotalPriceByRate(__productList, request.campaign.getAmount())
        elif(request.campaign.getCampaignType() == CampaignType.EACH_PRICE):
            if(request.campaign.getCalculationType() == CalculationType.AMOUNT):
                __productList = self.evaluatePriceOfEachPriceByAmount(__productList, request.campaign.getAmount())
            elif(request.campaign.getCalculationType() == CalculationType.RATE):
                __productList = self.evaluatePriceOfEachPriceByRate(__productList, request.campaign.getAmount())
        elif(request.campaign.getCampaignType() == CampaignType.SUBTRACT_PRICE):
            if(request.campaign.getCalculationType() == CalculationType.BIGGEST):
                __productList = self.sortProductsByPrice(__productList)
                __totalPrice  = self.evaluatePriceWithoutBiggest(__productList, request.campaign.getCount())
            elif(request.campaign.getCalculationType() == CalculationType.LOWEST):
                __productList = self.sortProductsByPrice(__productList)
                __totalPrice = self.evaluatePriceWithoutLowest(__productList, request.campaign.getCount())

        response = Response()
        response.totalPrice  = __totalPrice
        response.productList = __productList
        return response