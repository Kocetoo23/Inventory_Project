from models import Inventory

def main():
    inventory = Inventory()

    # Добавяне на продукти
    inventory.add_product("Laptop", 1500, 3)
    inventory.add_product("Mouse", 25, 20)
    inventory.add_product("Keyboard", 80, 10)
    inventory.add_product("Monitor", 300, 5)

    print("📦 Всички продукти:")
    print(inventory.list_products())

    print("\n🔎 Търсене на Mouse:")
    print(inventory.search_product("Mouse"))

    print("\n📊 Сортиране по цена:")
    print(inventory.sort_by_price())

    print("\n💰 Обща стойност на склада:")
    print(inventory.total_value())

    print("\n⚠️ Ниска наличност:")
    print(inventory.low_stock())

    print("\n📉 Средна цена:")
    print(inventory.average_price())

    print("\n🧾 Брой продукти:")
    print(inventory.count_products())

    # Обновяване
    inventory.update_quantity("Laptop", 2)
    print("\n🔄 След обновяване:")
    print(inventory.list_products())

    # Премахване
    inventory.remove_product("Mouse")
    print("\n❌ След премахване:")
    print(inventory.list_products())

if __name__ == "__main__":
    main()