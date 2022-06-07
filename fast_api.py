from interfaces.enums            import ProductCategory, CampaignType, CalculationType, CampaignImplementationType
from objects.SimpleProduct       import SimpleProduct
from objects.CampaignCalculator  import CampaignCalculator
from objects.SimpleCampaign      import SimpleCampaign
from objects.request             import Request
from fastapi                     import FastAPI

app = FastAPI()

def readEnvDataAsDict(path: str) ->dict:
    envVars:dict = {}
    with open(path, 'r') as file:
        for line in file:
            if(line.startswith('#') or not line.strip()):
                continue
            key, value = line.strip().split('=',1)
            envVars[key] = value
    return envVars

@app.get("/login")
def login(userName:str, password:str):
    print(userName)
    print(password)
    response: dict= {"token": "61"}
    return response

@app.post("/register")
def register(userName:str, password:str):
    print(userName)
    print(password)
    response: dict= {"processCode": "1"}
    return response

@app.post("/logout")
def logout(userName:str):
    print(userName)
    response: dict= {"processCode": "1"}
    return response

@app.get("/campaign")
def campaign(data: dict):
    token: str                    = data.get("userToken")
    products: list[SimpleProduct] = []

    for product in data.get("products"):
        products.append(SimpleProduct(product.get("name"), product.get("price"), ProductCategory(product.get("category"))))

    campaign:SimpleCampaign = SimpleCampaign(data.get("campaign").get("name"),
                                             CampaignImplementationType(data.get("campaign").get("implementationType")),
                                             CampaignType(data.get("campaign").get("campaignType")),
                                             CalculationType(data.get("campaign").get("calculationType")),
                                             data.get("campaign").get("amount"),
                                             data.get("campaign").get("count"),
                                             data.get("campaign").get("productNameList"),
                                             list(map(lambda category: ProductCategory(category), data.get("campaign").get("productCategoryList"))))
    campaignCalculator  = CampaignCalculator()
    request             = Request()
    request.productList = products
    request.campaign    = campaign
    response            = campaignCalculator.calculate(request)
    return response