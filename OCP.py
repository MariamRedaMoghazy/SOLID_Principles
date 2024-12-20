from abc import ABC, abstractmethod

# Base class for discount strategy
class DiscountStrategy(ABC):
    """Abstract class representing a discount strategy"""

    @abstractmethod
    def apply_discount(self, price):
        pass

# class for no discount
class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price

# class for percentage discount
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price - (price * self.percentage / 100)

# class for fixed amount discount
class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, price):
        return price - self.amount if price > self.amount else 0

# Context class for product
class Product:
    def __init__(self, name, price, discount_strategy: DiscountStrategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_price_after_discount(self):
        return self.discount_strategy.apply_discount(self.price)


    # Create products with different discount strategies
product1 = Product("Laptop", 1000, NoDiscount())
product2 = Product("Headphones", 200, PercentageDiscount(10))
product3 = Product("Keyboard", 50, FixedDiscount(20))

print(f"{product1.name} price after discount: ${product1.get_price_after_discount()}")
print(f"{product2.name} price after discount: ${product2.get_price_after_discount()}")
print(f"{product3.name} price after discount: ${product3.get_price_after_discount()}")