shopping_dict = {}
command = input()

while command != "Go Shopping":
    store_parts = command.split("->")
    action = store_parts[0]
    store = store_parts[1]

    if action == "Add":
        items = store_parts[2].split(",")
        if store not in shopping_dict:
            shopping_dict[store] = set()
        shopping_dict[store].update(items)

    elif action == "Important":
        important_item = store_parts[2].strip()
        if important_item in shopping_dict:
            continue
        if store not in shopping_dict:
            shopping_dict[store] = set()
        shopping_dict[store].add(important_item)

    elif action == "Remove":
       if store in shopping_dict and not any(item in shopping_dict[store] for item in shopping_dict.values()):
           del shopping_dict[store]
    command = input()

for store,items in shopping_dict.items():
    print(f"{store}: ")
    for item in items:
        print(f" - {item}")