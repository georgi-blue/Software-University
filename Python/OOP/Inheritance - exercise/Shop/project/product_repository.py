from typing import List

from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Food, Drink] = []

    def add(self, product: Drink or Food) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Food or Drink:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join(f'{p.name}: {p.quantity}' for p in self.products)
