class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        new_list = [product for product in self.products if product.startswith(first_letter)]
        return new_list

    def __repr__(self):
        returning_string = f"Items in the {self.name} catalogue:\n"
        returning_string += "\n" "".join(sorted(self.products))
        return returning_string

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
