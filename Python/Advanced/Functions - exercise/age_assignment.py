def age_assignment(*names, **parameters):
    result = []

    for key, value in parameters.items():
        for name in names:
            if name.startswith(key):
                result.append(f"{name} is {value} years old.")
    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))