product_type = input()
quantity = int(input())

def summary (product_type,quantity):
    if product_type == "coffee":
        return quantity * 1.50
    elif product_type == "water":
        return quantity * 1
    elif product_type == "coke":
        return quantity * 1.40
    elif product_type == "snacks":
        return quantity * 2

print(f"{summary(product_type,quantity):.2f}")