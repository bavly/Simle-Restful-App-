class MacAddress:
    def __init__(self, data):
        if isinstance(data, (long, int)):
            self.numData = data
            self.strData = hex(data)
        elif isinstance(data, str):
            self.strData = data
            self.numData = long(data, 16)

    def __str__(self):
        return self.strData

    def __add__(self, other):
        if (isinstance(other, (long, int))):
            return MacAddress(self.numData + other)
        elif(isinstance(other, str)):
            return MacAddress(self.numData + long(other, 16))
        elif(isinstance(other, MacAddress)):
            return MacAddress(self.numData + other.numData)

ma = MacAddress(hex(165877805475328))
mb = MacAddress(165877805475328)

print("For the hex value:")
print(ma)
print("For the int value:")
print(mb)
print("Addition:")
print(ma + mb)
print(ma + hex(165877805475328))
print(ma + 165877805475328)

