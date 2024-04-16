


USDrate=27.5

"""def toPriceNew(priceList):
    return list(map(lambda x: x*USDrate, priceList))
"""
pricesUSD=[100.34,35,67.99,25.5]
#print(pricesUSD)
def changePriceDecorator_v1(myFunction):
    print("Hello! Let's change your prices...")
    def simpleWrapper(argList):
        print("I've got list of prices with {} elements. Function starts working...".format(len(argList)))
        result=myFunction(argList)
        print("Let's set a discount..")
        return result
    print("konec prniho volani")
    return simpleWrapper


#pricesToGRN = changePriceDecorator_v1(toPriceNew)
#print(pricesToGRN(pricesUSD))
#print(toPriceNew(pricesUSD))

@changePriceDecorator_v1
def toPriceNew(priceList):
    return list(map(lambda x: x*USDrate, priceList))


print(toPriceNew(pricesUSD))