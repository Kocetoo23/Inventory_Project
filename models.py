class Inventory:
    def __init__(self):
        self.products = []

    # 1. Добавяне на продукт
    def add_product(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)

    # 2. Премахване на продукт
    def remove_product(self, name):
        self.products = [p for p in self.products if p["name"] != name]

    # 3. Търсене на продукт
    def search_product(self, name):
        for p in self.products:
            if p["name"].lower() == name.lower():
                return p
        return None

    # 4. Обновяване на количество
    def update_quantity(self, name, quantity):
        for p in self.products:
            if p["name"].lower() == name.lower():
                p["quantity"] = quantity

    # 5. Списък с всички продукти
    def list_products(self):
        return self.products

    # 6. Сортиране по цена
    def sort_by_price(self):
        return sorted(self.products, key=lambda x: x["price"])

    # 7. Сортиране по количество
    def sort_by_quantity(self):
        return sorted(self.products, key=lambda x: x["quantity"])

    # 8. Общата стойност на склада
    def total_value(self):
        total = 0
        for p in self.products:
            total += p["price"] * p["quantity"]
        return total

    # 9. Продукти с ниска наличност
    def low_stock(self, threshold=5):
        return [p for p in self.products if p["quantity"] <= threshold]

    # 10. Средна цена на продуктите
    def average_price(self):
        if not self.products:
            return 0
        return sum(p["price"] for p in self.products) / len(self.products)

    # 11. Изчистване на склада
    def clear_inventory(self):
        self.products = []

    # 12. Брой продукти
    def count_products(self):
        return len(self.products)