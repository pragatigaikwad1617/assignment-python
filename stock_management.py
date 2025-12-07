stock = {"apple": 50, "banana": 30, "mango": 20}
stock["orange"] = 40
stock["banana"] = 45
del stock["mango"]
if "apple" in stock:
    print("Apple is available")
print(list(stock.keys()))
print(list(stock.values()))
print(len(stock))