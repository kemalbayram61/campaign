from interfaces.enums            import ProductCategory, CampaignType, CalculationType, CampaignImplementationType
from objects.SimpleProduct       import SimpleProduct
from objects.CampaignCalculator  import CampaignCalculator
from objects.SimpleCampaign      import SimpleCampaign
from objects.request             import Request

import json
import flask

app = flask.Flask(__name__)

def readEnvDataAsDict(path: str) ->dict:
    envVars:dict = {}
    with open(path, 'r') as file:
        for line in file:
            if(line.startswith('#') or not line.strip()):
                continue
            key, value = line.strip().split('=',1)
            envVars[key] = value
    return envVars

@app.route("/login", methods=["GET"])
def login():
    userName: str = flask.request.form.get("userName")
    password: str = flask.request.form.get("password")
    response: dict= {"token": "61"}
    return flask.jsonify(response)

@app.route("/register", methods=["POST"])
def register():
    userName: str = flask.request.form.get("userName")
    password: str = flask.request.form.get("password")
    response: dict= {"processCode": "1"}
    return flask.jsonify(response)

@app.route("/logout", methods=["POST"])
def logout():
    userName: str = flask.request.form.get("userName")
    response: dict= {"processCode": "1"}
    return flask.jsonify(response)

@app.route("/campaign", methods=["GET"])
def campaign():
    token: str                    = flask.request.form.get("userToken")
    dataStr: str                  = flask.request.data.decode('utf-8').replace('\n', "")
    data: dict                    = json.loads(dataStr)
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
    return flask.jsonify(str(response))

if __name__ == '__main__':
    variables = readEnvDataAsDict('local.env')
    host      = variables.get("BASE_URL")
    port      = variables.get("PORT")
    app.run(host = host, port = port, debug= True)