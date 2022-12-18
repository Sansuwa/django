#ACCESS_MODIFIER

class Product:
    def __init__(self, name,sku, price):
        self.name = name
        self.sku = sku
        self.price = price
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price <= price:
            return
        self.__price = price
        
p = Product("Tshirt"."9876",1500)
#price (p.price)
p.price = 100
print(p.__dict__)           
        
        