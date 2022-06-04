from objects.SimpleProduct import SimpleProduct

class Response:
    productList: list[SimpleProduct]
    totalPrice : float

    def __str__(self):
        __response = ""
        for product in self.productList:
            __response = __response + str(product) + "\n"
        __response = __response + " price : " + str(self.totalPrice)
        return  __response