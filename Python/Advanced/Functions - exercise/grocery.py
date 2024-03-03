def grocery_store(**grocery_data):
    new_grocery_data = sorted(grocery_data.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return "\n".join(f"{name}: {quantity}" for name, quantity in new_grocery_data)

print(grocery_store(bread=5,pasta=12,eggs=12,))
