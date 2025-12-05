class Sneakers:
    def __init__(self, brand, size, color, price, quantity, material, number_of_sales):
        if not brand or not isinstance(brand, str):
            raise ValueError("бренд повинен бути непустим рядком")

        if not isinstance(size, (int, float)) or size <= 0:
            raise ValueError("розмір повинен бути додатнім числом")

        if not color or not isinstance(color, str):
            raise ValueError("колір повинен бути непустим рядком")

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("ціна не може бути від'ємною")

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("кількість не може бути від'ємною")

        if not material or not isinstance(material, str):
            raise ValueError("матеріал повинен бути непустим рядком")

        if not isinstance(number_of_sales, int) or number_of_sales < 0:
            raise ValueError("кількість продажів не може бути від'ємною")

        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.material = material
        self.numberOfSales = number_of_sales

    def set_brand(self, brand):
        if not brand or not isinstance(brand, str):
            raise ValueError("бренд повинен бути непустим рядком")
        self.brand = brand

    def set_size(self, size):
        if not isinstance(size, (int, float)) or size <= 0:
            raise ValueError("розмір повинен бути додатнім числом")
        self.size = size

    def set_color(self, color):
        if not color or not isinstance(color, str):
            raise ValueError("колір повинен бути непустим рядком")
        self.color = color

    def set_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("ціна не може бути від'ємною")
        self.price = price

    def set_quantity(self, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("кількість не може бути від'ємною")
        self.quantity = quantity

    def set_material(self, material):
        if not material or not isinstance(material, str):
            raise ValueError("матеріал повинен бути непустим рядком")
        self.material = material

    def set_numberOfSales(self, numberOfSales):
        if not isinstance(numberOfSales, int) or numberOfSales < 0:
            raise ValueError("кількість продажів не може бути від'ємною")
        self.numberOfSales = numberOfSales

    def get_brand(self):
        return self.brand

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_material(self):
        return self.material

    def get_numberOfSales(self):
        return self.numberOfSales

    def display_info(self):
        print(f"бренд: {self.brand}")
        print(f"розмір: {self.size}")
        print(f"колір: {self.color}")
        print(f"ціна: {self.price}")
        print(f"кількість: {self.quantity}")
        print(f"матеріал: {self.material}")
        print(f"продано: {self.numberOfSales}")

class SportShoesStore:
    def __init__(self):
        self.assortment = []

    def add_sneakers(self, sneakers):
        self.assortment.append(sneakers)

    def sort_by_price(self):
        return sorted(self.assortment, key=lambda s: s.get_price())

    def sort_by_sales(self):
        return sorted(self.assortment, key=lambda s: s.get_numberOfSales(), reverse=True)

    def top_popular(self, top_n=3):
        sorted_by_sales = self.sort_by_sales()
        return sorted_by_sales[:top_n]

    def display_assortment(self):
        for sneakers in self.assortment:
            sneakers.display_info()

    def filter_by_color_or_price(self):
        choice = input("введіть 'color' для пошуку за кольором або 'price' для пошуку за ціною: ").strip().lower()
        if choice == 'color':
            color_search = input("введіть колір англійською: ").strip()
            filtered = [s for s in self.assortment if s.get_color() == color_search]
        elif choice == 'price':
            try:
                max_price = float(input("введіть максимальну ціну: "))
            except ValueError:
                print("некоректна ціна.")
                return
            filtered = [s for s in self.assortment if s.get_price() <= max_price]
        else:
            print("невірний вибір.")
            return

        if filtered:
            print(f"знайдено {len(filtered)} кросівок:")
            for sneakers in filtered:
                sneakers.display_info()
                print()
        else:
            print("кросівок за заданим критерієм не знайдено.")

def main():
    store = SportShoesStore()

    store.add_sneakers(Sneakers("Nike", 42, "Black", 120, 10, "Synthetic", 150))
    store.add_sneakers(Sneakers("Adidas", 43, "White", 100, 15, "Leather", 200))
    store.add_sneakers(Sneakers("Puma", 41, "Blue", 80, 20, "Mesh", 120))
    store.add_sneakers(Sneakers("Reebok", 44, "Red", 90, 8, "Synthetic", 90))
    store.add_sneakers(Sneakers("Nike", 43, "Black", 130, 5, "Leather", 180))

    print("асортимент кросівок:")
    store.display_assortment()

    print("взуття відсортоване за ціною (зростаюче):")
    sorted_by_price = store.sort_by_price()
    for sneakers in sorted_by_price:
        sneakers.display_info()
        print()

    print("Топ 3 найпопулярніших кросівок:")
    top_sneakers = store.top_popular()
    for sneakers in top_sneakers:
        sneakers.display_info()
        print()

    store.filter_by_color_or_price()

if __name__ == "__main__":
    main()
