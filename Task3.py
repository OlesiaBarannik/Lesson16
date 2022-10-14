class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.product_list = []
        self.income = 0

    def add(self, product, amount, markup = 0.3):
        product.price = round(product.price * (1 + markup), 2)
        self.product_list.append({"product": product, 'amount': amount})

    def set_discount(self, identifier, percent, identifier_type="name"):
        for p in self.product_list:
            if identifier_type == "type":
                if p["product"].type == identifier:
                    p["product"].price = round(p["product"].price * (1 - percent), 2)

            elif identifier_type == "name":
                if p["product"].name == identifier:
                    p["product"].price = round(p["product"].price * (1 - percent), 2)

    def sell_product(self, product_name, amount):
            for p in self.product_list:
                    if p["product"].name == product_name:
                        if p["amount"] >= amount:
                            p["amount"] -= amount
                            self.income += amount * p['product'].price

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.product_list

    def get_product_info(self):
        self.product_list1 = []
        for p in self.product_list:
            r = (p["product"].name + " " + str(p["amount"]))
            self.product_list1.append(r)
        self.product_list1 = tuple(self.product_list1)
        print (self.product_list1)


p1 = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)

store = ProductStore()
store.add(p1, 15)
store.add(p2, 40)
store.set_discount("Ramen", 0.2, "name")
store.sell_product("Ramen", 2)
store.get_all_products()
store.get_product_info()
products = store.get_all_products()
