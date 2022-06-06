from objects.SimpleProduct      import SimpleProduct
from objects.SimpleCampaign     import SimpleCampaign
from objects.CampaignCalculator import CampaignCalculator
from interfaces.enums           import ProductCategory, CampaignImplementationType, CampaignType, CalculationType
from objects.request            import Request

def main():
    product1 = SimpleProduct("Jacobs Vanilya Aromalı", 80.1 , ProductCategory.C1)
    product2 = SimpleProduct("Mini Kakaolu Kek"      , 11.65, ProductCategory.C2)
    product3 = SimpleProduct("Jacobs Fındık Aromalı" , 80.1 , ProductCategory.C1)
    product4 = SimpleProduct("Nestle Fındık Aromalı" , 76.1 , ProductCategory.C1)
    product5 = SimpleProduct("Teksüt Kaşar Peyniri"  , 74.9 , ProductCategory.C3)
    product6 = SimpleProduct("Mini Vanilyalı Kek"    , 20.65, ProductCategory.C2)

    campaign1 = SimpleCampaign(name         = "2 kahve alana 3.sü bedava",
                        implementationType  = CampaignImplementationType.PRODUCT_CATEGORY,
                        campaignType        = CampaignType.SUBTRACT_PRICE,
                        calculationType     = CalculationType.LOWEST,
                        amount              = 0.0,
                        count               = 1,
                        productNameList     = [""],
                        productCategoryList = [ProductCategory.C1])
    campaign2 = SimpleCampaign("sepette %10 indirim",
                        CampaignImplementationType.PRODUCT_CATEGORY,
                        CampaignType.TOTAL_PRICE,
                        CalculationType.RATE,
                        10.0,
                        0,
                        [""],
                        [ProductCategory.CE])
    campaign3 = SimpleCampaign("keklerde %50 indirim",
                        CampaignImplementationType.PRODUCT_CATEGORY,
                        CampaignType.SUBTRACT_PRICE,
                        CalculationType.LOWEST,
                        0.0,
                        1,
                        [""],
                        [ProductCategory.C1])

    campaign4 = SimpleCampaign("sepette %10 indirim",
                        CampaignImplementationType.PRODUCT_CATEGORY,
                        CampaignType.EACH_PRICE,
                        CalculationType.RATE,
                        50.0,
                        0,
                        [""],
                        [ProductCategory.C2])

    campaign5 = SimpleCampaign("Teksüt Kaşar Peyniri sadece 10birim",
                        CampaignImplementationType.PRODUCT,
                        CampaignType.EACH_PRICE,
                        CalculationType.AMOUNT,
                        64.9,
                        1,
                        ["Teksüt Kaşar Peyniri"],
                        [ProductCategory.C1])

    campaign6 = SimpleCampaign("Seçili ürünler %20 indirimli",
                        CampaignImplementationType.PRODUCT,
                        CampaignType.EACH_PRICE,
                        CalculationType.RATE,
                        20,
                        1,
                        ["Teksüt Kaşar Peyniri", "Nestle Fındık Aromalı"],
                        [ProductCategory.C1])

    campaign7 = SimpleCampaign("Seçili ürünler %20 indirimli",
                        CampaignImplementationType.PRODUCT,
                        CampaignType.EACH_PRICE,
                        CalculationType.RATE,
                        20,
                        1,
                        ["Trabzon peyniri"],
                        [ProductCategory.C1])

    campaignCalculator                 = CampaignCalculator()
    productList: list[SimpleProduct]   = [product1, product2, product3, product4, product5, product6]
    campaignList: list[SimpleCampaign] = [campaign1, campaign2, campaign3, campaign4, campaign5, campaign6, campaign7]
    #request             = Request()
    #request.productList = productList
    #request.campaign    = campaign7
    #response            = campaignCalculator.calculate(request)
    response = campaignCalculator.findEligibleCampaigns(productList, campaignList)
    print(len(response))

if __name__ == '__main__':
    main()

